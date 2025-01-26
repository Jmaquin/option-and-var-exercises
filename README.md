# Option and Value at Risk exercises
## 1)Option
Implement the Black and Scholes model for Call and Put option pricing

### a)Call Option Pricing Formula (Black-Scholes)
The Black-Scholes formula for pricing a European Call Option is:

$$ C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2) $$

#### where:
$$ d_1 = \frac{\ln(S / K) + (r + \sigma^2 / 2)T}{\sigma \sqrt{T}} $$
$$ d_2 = d_1 - \sigma \sqrt{T} $$

### b)Put Option Pricing Formula (Black-Scholes)
The Black-Scholes formula for pricing a European Put Option is:

$$ P = K \cdot e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1) $$

#### where:
$$ d_1 = \frac{\ln(S / K) + (r + \sigma^2 / 2)T}{\sigma \sqrt{T}} $$
$$ d_2 = d_1 - \sigma \sqrt{T} $$

#### Parameters:

- **S**: Current stock price at the time of pricing(spot price).
- **K**: Strike price — the price at which the option can be exercised.
- **r**: Risk-free interest rate, expressed as a decimal.
- **T**: Time to expiration, in years.
- **σ (sigma)**: Volatility of the stock, expressed as a decimal.
- **N(x)**: The cumulative distribution function of the standard normal distribution.

## 2)Value at Risk
Implement Value at Risk methodology as describe in the Exercises.xlsx file

N.B: 
The implementation of this exercise was done considering a sensitivity of 1 and 1 day of horizon without passing these values as parameters.
