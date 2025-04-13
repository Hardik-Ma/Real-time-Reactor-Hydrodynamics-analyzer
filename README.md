# Realtime Hydrodynamic study of Coiled flow inverter Bioreactor

## Workflow
1. **Experiment**: Run `Experiment/RT_RTD_3.py` to collect data using a feed from webcam at the outlet of the Reactor.
2. **Analyze**:
   - Hydrodynamics: See `Data_Analysis/Hydrodynamic_Analysis/`
   - Microbial Kinetics: See `Data_Analysis/Microbial_Analysis/`

## Folder Structure
- `Experiment/`: OpenCV-based tracer tracking.
- `Data_Analysis/`: 
  - `Hydrodynamic_Analysis/`: Residence time Distribution, mixing behaviour, hydrodynamic characteristics.
  - `Microbial_Analysis/`: Growth models, Growth constants, mathematical modeling of STR and CFIR system.
