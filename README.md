# Realtime Hydrodynamic study of Coiled flow inverter Bioreactor

## Workflow
1. **Experiment**: Run `Experiment/RT_RTD_3.py` to collect data using a feed from webcam at the outlet of the Reactor.
2. **Analyze**:
   - Hydrodynamics: See `Data_Analysis/Hydrodynamic_Study/`
   - Microbial Kinetics: See `Data_Analysis/Microbial_Study/`

## Folder Structure
- `Experiment/`: OpenCV-based tracer tracking.
- `Data_Analysis/`: 
  - `Hydrodynamic_Study/`: Residence time Distribution, mixing behaviour, hydrodynamic characteristics.
  - `Microbial_Study/`: Growth models, Growth constants, mathematical modeling of STR and CFIR system.
