# Theory: CSTR-PFR System with Axial Dispersion and Logistic Growth

## Governing Equations

### 1. CSTR Dynamics
The mass balance for the **CSTR** (Continuous Stirred-Tank Reactor) with logistic growth kinetics is:

$$
\frac{dX_{\text{CSTR}}}{dt} = \underbrace{\frac{F}{V} (X_{\text{PFR, out}} - X_{\text{CSTR}})}_{\text{Flow term}} + \underbrace{\mu_{\text{max}} X_{\text{CSTR}} \left(1 - \frac{X_{\text{CSTR}}}{X_{\text{max}}}\right)}_{\text{Logistic growth}}
$$

Where:
- $X_{\text{CSTR}}$: Biomass concentration in the CSTR (OD or g/L).
- $X_{\text{PFR, out}}$: Outlet concentration from the PFR (inlet to CSTR).
- $F$: Flow rate (m³/s).
- $V$: CSTR volume (m³).
- $\mu_{\text{max}}$: Maximum specific growth rate (1/h).
- $X_{\text{max}}$: Maximum carrying capacity (OD or g/L).

---

### 2. PFR Dynamics
The **PFR** (Plug Flow Reactor) with axial dispersion and logistic growth is modeled by:

$$
\frac{\partial X}{\partial t} + u \frac{\partial X}{\partial z} = \underbrace{D \frac{\partial^2 X}{\partial z^2}}_{\text{Axial dispersion}} + \underbrace{\mu_{\text{max}} X \left(1 - \frac{X}{X_{\text{max}}}\right)}_{\text{Logistic growth}}
$$

Where:
- $X(z, t)$: Biomass concentration at position $z$ and time $t$.
- $u$: Superficial velocity (m/s).
- $D$: Axial dispersion coefficient (m²/s).

---

### 3. Boundary Conditions
#### Inlet of PFR ($z = 0$):
$$
u X_{\text{CSTR}}(t) = u X(0, t) - D \frac{\partial X}{\partial z} \bigg|_{z=0}
$$
Ensures continuity between CSTR outlet and PFR inlet.

#### Outlet of PFR ($z = L$):
$$
\frac{\partial X}{\partial z} \bigg|_{z=L} = 0
$$
Zero-gradient condition (no flux out of the reactor).

---

### 4. Cyclic Boundary Conditions (Recycle System)
For a **closed-loop system** (PFR outlet → CSTR inlet → PFR inlet):
1. **PFR inlet** = CSTR outlet:  
   $X(0, t) = X_{\text{CSTR}}(t)$.
2. **CSTR inlet** = PFR outlet:  
   $X_{\text{PFR, out}}(t) = X(L, t)$.

---

## Numerical Implementation
- Solved using **Method of Lines** (spatial discretization of PFR + ODE solver).
- Parameters optimized to fit experimental data for $X_{\text{CSTR}}(t)$ and $X_{\text{PFR, out}}(t)$.

---

## Key Assumptions
1. **Logistic growth**: Biomass growth saturates at $X_{\text{max}}$.
2. **Well-mixed CSTR**: Uniform concentration in the tank.
3. **Axial dispersion**: Accounts for diffusion in the PFR.
