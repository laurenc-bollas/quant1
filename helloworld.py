import numpy as np

# Given values
S_t = 1.20  # Spot price in dollars
r = 0.02  # Risk-free rate (2%)
d = 0.01  # Storage cost (1%)
T = 0.5  # Time to maturity in years

# Calculating futures price
F_t = S_t * np.exp((r + d) * T)
print(f"The fair price of the coffee futures contract is ${F_t:.3f} per pound.")
