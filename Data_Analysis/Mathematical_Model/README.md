# Theory: CSTR-PFR System with Axial Dispersion and Logistic Growth

## Governing Equations

### 1. CSTR Dynamics
The mass balance for the **CSTR** (Continuous Stirred-Tank Reactor) with logistic growth kinetics is:

$$
\frac{dX_{CSTR}}{dt} = \frac{F}{V} (X_{PFR,out} - X_{CSTR}) + \mu_{max} X_{CSTR} \left(1 - \frac{X_{CSTR}}{X_{max}}\right)
$$

**Terms:**
- **Flow term**: $\frac{F}{V} (X_{PFR,out} - X_{CSTR})$
- **Logistic growth**: $\mu_{max} X_{CSTR} \left(1 - \frac{X_{CSTR}}{X_{max}}\right)$

**Variables:**
- $X_{CSTR}$: Biomass concentration in CSTR (OD or g/L)
- $X_{PFR,out}$: Outlet concentration from PFR (inlet to CSTR)
- $F$: Flow rate (m³/s)
- $V$: CSTR volume (m³)
- $\mu_{max}$: Maximum specific growth rate (1/h)
- $X_{max}$: Maximum carrying capacity (OD or g/L)

---

### 2. PFR Dynamics
The **PFR** (Plug Flow Reactor) with axial dispersion and logistic growth:

$$
\frac{\partial X}{\partial t} + u \frac{\partial X}{\partial z} = D \frac{\partial^2 X}{\partial z^2} + \mu_{max} X \left(1 - \frac{X}{X_{max}}\right)
$$

**Terms:**
- **Axial dispersion**: $D \frac{\partial^2 X}{\partial z^2}$
- **Logistic growth**: $\mu_{max} X \left(1 - \frac{X}{X_{max}}\right)$

**Variables:**
- $X(z,t)$: Biomass concentration at position $z$ and time $t$
- $u$: Superficial velocity (m/s)
- $D$: Axial dispersion coefficient (m²/s)

---

### 3. Boundary Conditions
#### Inlet of PFR ($z = 0$):
$$
u X_{CSTR}(t) = u X(0,t) - D \left. \frac{\partial X}{\partial z} \right|_{z=0}
$$

#### Outlet of PFR ($z = L$):
$$
\left. \frac{\partial X}{\partial z} \right|_{z=L} = 0
$$

---

### 4. Cyclic Boundary Conditions (Recycle System)
For a **closed-loop system**:
1. PFR inlet = CSTR outlet:  
   $X(0,t) = X_{CSTR}(t)$
2. CSTR inlet = PFR outlet:  
   $X_{PFR,out}(t) = X(L,t)$

---

## Numerical Implementation
- Solved using **Method of Lines** (spatial discretization + ODE solver)
- Parameters optimized to fit experimental data for $X_{CSTR}(t)$ and $X_{PFR,out}(t)$

---

## Key Assumptions
1. **Logistic growth**: Biomass growth saturates at $X_{max}$
2. **Well-mixed CSTR**: Uniform concentration in tank
3. **Axial dispersion**: Accounts for diffusion in PFR
