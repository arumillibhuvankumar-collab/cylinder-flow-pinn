# LESSON 2 EXERCISE: Steady Cylinder Re=20

# Physics parameters for water
U = 2.0                    # Inflow velocity (m/s)
D = 0.05                   # Cylinder diameter (m)
nu = 0.000001              # Kinematic viscosity (m²/s)
rho = 1000.0               # Density (kg/m³)

# Compute Reynolds number
Re = U * D / nu

# Mesh info
num_x = 50
num_y = 50

# Case name
case_name = "cylinder_re20_steady"

# Steady state flag
is_steady = True

# Print all values
print("="*50)
print("CYLINDER FLOW SIMULATION SETUP")
print("="*50)
print(f"Case name: {case_name}")
print(f"Reynolds number: {Re}")
print(f"Velocity U: {U} m/s")
print(f"Diameter D: {D} m")
print(f"Kinematic viscosity nu: {nu} m²/s")
print(f"Density rho: {rho} kg/m³")
print(f"Grid points (x, y): {num_x} × {num_y}")
print(f"Is steady state: {is_steady}")

# Stretch goal: Compute dynamic viscosity
mu = rho * nu
print(f"\nDynamic viscosity mu: {mu} kg/(m·s)")
print("="*50)
