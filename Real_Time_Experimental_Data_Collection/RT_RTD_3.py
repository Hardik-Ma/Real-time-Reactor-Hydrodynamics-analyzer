import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import deque
from datetime import datetime, timedelta

# Function to calculate the average luma value and RGB values of a region
def calculate_luma_and_rgb(region):
    # Convert the region to grayscale (luma is the same as grayscale intensity)
    gray_region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    luma_value = np.mean(gray_region)

    # Calculate the average RGB values
    avg_r = np.mean(region[:, :, 2])  # Red channel
    avg_g = np.mean(region[:, :, 1])  # Green channel
    avg_b = np.mean(region[:, :, 0])  # Blue channel

    return luma_value, avg_r, avg_g, avg_b

# Function to apply a moving average filter
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

# Open a connection to the webcam (use the correct camera index or URL)
camera_index = 1  # Change this to the correct index for your external camera (The current camera_index is for external camera)
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define the region of interest (ROI) coordinates (x, y, width, height)
x, y, width, height = 270, 180, 8, 8 # Single region

# Set up circular buffers to store luma values and rate of change for real-time plotting
max_length = 100  # Number of values to store
luma_buffer = deque(maxlen=max_length)
rate_of_change_buffer = deque(maxlen=max_length)
time_buffer = deque(maxlen=max_length)  # Store timestamps for rate of change calculation

# Initialize the plot
plt.ion()  # Turn on interactive mode
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
line1, = ax1.plot([], [], 'b-', label="Luma Value")
line2, = ax2.plot([], [], 'r-', label="Rate of Change of Luma")
ax1.set_xlim(0, max_length)
ax1.set_ylim(0, 255)  # Luma values range from 0 to 255
ax1.set_ylabel("Luma Value")
ax1.legend()
ax2.set_xlim(0, max_length)
ax2.set_ylim(-10, 10)  # Initial range for rate of change
ax2.set_xlabel("Time")
ax2.set_ylabel("Rate of Change")
ax2.legend()

# Initialize variables for recording
recording = False
recording_started = False
luma_data = []  # List to store (timestamp, time_elapsed, luma_value, avg_r, avg_g, avg_b, rate_of_change) tuples
start_time = None  # Timestamp when recording starts
delay_duration = 30  # Delay before recording starts after pressing 's_button' = 30 seconds
delay_start_time = None  # Timestamp when delay starts

# Smoothing parameters
smoothing_window_size = 5  # Size of the moving average window

# Function to update the plot
def update_plot():
    line1.set_xdata(np.arange(len(luma_buffer)))
    line1.set_ydata(luma_buffer)
    ax1.relim()
    ax1.autoscale_view()

    # Smooth the rate of change values
    if len(rate_of_change_buffer) >= smoothing_window_size:
        smoothed_rate_of_change = moving_average(rate_of_change_buffer, smoothing_window_size)
        line2.set_xdata(np.arange(len(smoothed_rate_of_change)))
        line2.set_ydata(smoothed_rate_of_change)
    else:
        line2.set_xdata(np.arange(len(rate_of_change_buffer)))
        line2.set_ydata(rate_of_change_buffer)

    # Dynamically adjust the y-axis range for the rate of change plot
    if len(rate_of_change_buffer) > 0:
        ax2.set_ylim(min(rate_of_change_buffer) - 5, max(rate_of_change_buffer) + 5)

    fig.canvas.draw()
    fig.canvas.flush_events()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Extract the region of interest (ROI) from the color frame
    roi = frame[y:y+height, x:x+width]

    # Calculate the average luma value and RGB values of the ROI
    luma_value, avg_r, avg_g, avg_b = calculate_luma_and_rgb(roi)

    # Get the current time
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Truncate microseconds to 3 digits

    # Calculate the rate of change of luma
    if len(luma_buffer) > 0:
        time_diff = (current_time - time_buffer[-1]).total_seconds()
        if time_diff > 0:  # Avoid division by zero
            rate_of_change = (luma_value - luma_buffer[-1]) / time_diff
        else:
            rate_of_change = 0
    else:
        rate_of_change = 0

    # Add the luma value and rate of change to the buffers for real-time plotting
    luma_buffer.append(luma_value)
    rate_of_change_buffer.append(rate_of_change)
    time_buffer.append(current_time)

    # Check if recording is active and if the delay has passed
    if recording and not recording_started:
        if delay_start_time is None:
            delay_start_time = current_time  # Set the delay start time
        elif (current_time - delay_start_time).total_seconds() >= delay_duration:
            recording_started = True  # Start recording after the delay
            start_time = current_time  # Set the start time for recording
            print("Recording started after delay...")

    # If recording has started, store the luma value, RGB values, timestamp, and elapsed time
    if recording_started:
        elapsed_time = (current_time - start_time).total_seconds()  # Calculate elapsed time in seconds
        luma_data.append((timestamp, elapsed_time, luma_value, avg_r, avg_g, avg_b, rate_of_change))
    else:
        elapsed_time = 0.0  # Reset elapsed time when not recording

    # Display the luma value, RGB values, timestamp, and elapsed time on the frame
    cv2.putText(frame, f"Luma: {luma_value:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"R: {avg_r:.2f}, G: {avg_g:.2f}, B: {avg_b:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"Timestamp: {timestamp}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"Elapsed Time: {elapsed_time:.2f} s", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"Rate of Change: {rate_of_change:.2f}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display a countdown or recording status
    if recording and not recording_started:
        remaining_delay = delay_duration - (current_time - delay_start_time).total_seconds()
        cv2.putText(frame, f"Recording starts in: {remaining_delay:.1f} s", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    elif recording_started:
        cv2.putText(frame, "Recording...", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Draw a rectangle around the ROI (single_ROI)
    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Webcam Luma Analysis', frame)

    # Update the plot
    update_plot()

    # Check for key presses
    key = cv2.waitKey(30)  # Increase delay to 30ms for better key press detection (This can be changes on the required sensitivity)
    if key == ord('s'):  # Start recording (with delay)
        recording = True
        luma_data = []  # Reset the data when starting a new recording
        start_time = None  # Reset the start time
        delay_start_time = None  # Reset the delay start time
        recording_started = False  # Reset the recording started flag
        print("Recording will start after delay...")
    elif key == ord('e'):  # End recording
        recording = False
        recording_started = False
        print("Recording stopped.")
    elif key == ord('q'):  # Quit the program (Pressing the Q button will stop the data recording)
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
plt.close()

# Convert the recorded data to a DataFrame
if luma_data:
    df = pd.DataFrame(luma_data, columns=["Timestamp", "Time (s)", "Luma Value", "Avg R", "Avg G", "Avg B", "Rate of Change"])
    print("Recorded Data:")
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv("luma_data.csv", index=False)
    print("Data saved to 'luma_data.csv'.")
else:
    print("No data recorded.")