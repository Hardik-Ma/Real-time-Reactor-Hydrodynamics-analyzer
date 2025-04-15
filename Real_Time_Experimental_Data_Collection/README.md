# Real Time Experimental Data Collection from CFI Bioreactor Tracer Studies

Using OpenCV and Resazurin Dye for Hydrodynamic Characterization and understanding the Dynamics of Coiled flow inverter Bioreactor

## Purpose

This module captures real-time tracer (Resazurin dye) dispersion in a Coiled Flow Inverter (CFI) bioreactor via webcam, recording:
- Luma intensity (proxy for dye concentration)
- RGB channel averages (Dependeing on the dye used the weightage of the RGB Values can be changed)
- Timestamped rate-of-change data

## Hardware Setup

### Critical Components

| Item | Specification | Note |
|------|---------------|------|
| Webcam | 1080p External webcam | The Camera is mounted ~ 30 cm away from the Reactor outlet |
| CFI Bioreactor | Inner Diameter: 6 mm, Total Length: 14 m | - |
| Manual Dye Injection System | Manual Syringe (5 ml) | Only 2ml of dye was used for the tracer experiments |
| Automated Dye Injection System | Peristaltic pump in combination with 3 way valve | This method was only used for low flowrates |

### Hardware Set Up Schematic 
Images/Manual_Dye_Injection_Schematic.png
*Fig 1: Manual Dye Injection Schematic

Images/Automatic_Dye_Injection_System.png
*Fig 2: Automatic Dye Injection Schematic

## Software Dependencies
### Core packages  
- Python 3.x
- Required libraries:
    - Open cv
    - numpy
    - pandas 
    - matplotlib

## Configuration
### Key Parameters in `RT_RTD_3.py`

| Variable | Default Value | Description |
|----------|---------------|-------------|
| `camera_index` | `1` | Change to `0` for built-in webcam |
| `x, y` | `270, 180` | ROI top-left corner (pixels) |
| `width, height` | `8, 8` | ROI size (adjust such that one point is covered) |
| `delay_duration` | `30` | Delay before the Data recording is started (sec) |

## Execution

### Command
```bash
python RT_RTD_3.py
```

### Runtime controls

| Key | Action |
|-----|--------|
| `s` | Starts Data Recording (after 30s delay) |
| `e` | Stop Data Recording |
| `q` | Quit the program |

### Output:
- Real-time plot of luma vs time(s).
- `luma_data.csv` saved in the same directory.

## Output Data Format

`luma_data.csv` columns:

| Column | Units | Description |
|--------|-------|-------------|
| `Timestamp` | YYYY-MM-DD HH:MM:SS.ms | Acquisition time |
| `Time (S)` | Seconds | Elapsed time since recording started |
| `Luma Value` | 0-255 | Grayscale intensity of ROI |
| `Avg R/G/B` | 0-255 | Mean RGB channels |
| `Rate Of Change of Luma` | ΔLuma/sec | First derivative of luma |

### Example Data:
```csv
Timestamp,Time (s),Luma Value,Avg R,Avg G,Avg B,Rate of Change  
2024-05-15 14:30:05.123,0.0,142.3,150.1,140.2,130.5,0.0  
2024-05-15 14:30:05.456,0.333,145.7,153.8,143.1,132.9,10.2 
```

## Troubleshooting
Common errors that occor in the code and also with the apparatus while running the code are mentioned below

| Issue | Solutions |
|-------|-----------|
| "Could not open the webcam" error | Check the `Camera_index` change from internal webcam 0 to external webcam 1 |
| Flickering ROI values | Shield the reactor outlet sampling port from the ambient light |
| CSV file not saving | Ensure you pressed `e` before quitting |
| Data Recording / Delay countdown not starting | Make sure you press the `s` a couple of times to start the recording |

## Next Steps
Procees to data analysis:
- Hydrodynamic analysis
- Microbial Models 
