# Microbial Growth Dynamics Anaöysis

Parameter estimation and modeling of CSTR-PFR bioreactor systems using optical density (OD) data

## Purpose
This script analyzes microbial growth in bioreactors by:
- Processing experimental OD measurements from CSTR and PFR reactors
- Estimating growth parameters (`μ_max`, `X_max`) via optimization
- Simulating coupled CSTR-PFR dynamics with axial dispersion

## Installation

### Prerequisites
- Python 3.x
- Jupyter Notebook

### Dependencies
- Python 3.x
- Required libraries:
  - NumPy
  - Pandas
  - Matplotlib
  - SciPy
  - sympy


## Key Features
- Data Processing
    - Time-series OD data cleaning and interpolation
    - Statistical aggregation (mean ± SD)
    - Visualization with error bars
- Growth Modeling
    - Logistic growth kinetics fitting
    - Coupled CSTR-PFR system simulation
    - Parameter estimation via L-BFGS-B optimization
- Visualization
    - Experimental vs. model prediction plots
    - Multi-panel comparison of CSTR/PFR dynamics

## Usage
## Inpur Data Format:
Required CSV columns:
- `Zeit`: Time stamps (Format `HHMM`)
- `OD_IN_RAW`: Inlet optical density
- `OD_OUT_RAW`: Outlet optical density

Example:
```csv
Zeit;OD_IN_RAW;OD_OUT_RAW
0945;0.12;0.08
1000;0.15;0.10
```

## Run Analysis
```python 
# Load and preprocess data
df = pd.read_csv('Microbial_growth_data.csv', sep=';', decimal=',')

# Fit growth parameters
params_initial = [0.5, 20.0]  # μ_max (1/h), X_max (OD)
result = minimize(objective, params_initial, method='L-BFGS-B')
mu_max_opt, X_max_opt = result.x

# Simulate coupled system
sol = solve_ivp(coupled_system, t_span, y0, args=(mu_max_opt, X_max_opt))
```

## Key Outputs
| Output | Function/Method | Example Result |
|--------|-----------------|----------------|
| Growth rate (`μ_max`) | `minimize(objective,...)` | `0.78 ± 0.05 1/h` |
| Max OD (`X_max`) | `solve_ivp()` | `18.2 ± 1.3 OD` |
| CSTR/PFR profiles | `coupled_system()`| Plots + CSV exports |

## Function Overview
| Function | Purpose |
|----------|---------|
| `cstr_ode()` | Solves CSTR mass balance with growth term |
| `pfr_model()` | Axial dispersion PFR with growth kinetics |
| `coupled_system()` | 	Links CSTR and PFR dynamics |
| `objective()` | Optimization target for parameter fitting |

## Example Workflow

### Preprocess Data
```python 
df['Elapsed_Time'] = (df['Zeit'] - df['Zeit'].iloc[0]).dt.total_seconds() / 60
``` 
### Fit Parameters
```python
result = minimize(objective, [0.5, 20.0], method='L-BFGS-B')
```
### Simulate and Plot
```python
plt.plot(t_exp, X_CSTR_model, label='CSTR Prediction')
```

## Troubleshooting
- Convergence Issues:
    - Adjust initial guesses (`params_initial`)
    - Scale time units (hours vs minutes)