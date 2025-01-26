import math

import numpy as np
from scipy.stats import norm


def calculate_1d_shift(previous_day_market_rate: float, current_day_market_rate: float) -> float:
    return math.exp(math.log(previous_day_market_rate / current_day_market_rate)) - 1


def calculate_pnl_vector_1d(one_day_shift: float, portfolio_value: float) -> float:
    return one_day_shift * portfolio_value


def calculate_historical_var_1d(historical_total_pnl_values: np.ndarray, confidence_level: float) -> float:
    return float(
        round(
            np.percentile(historical_total_pnl_values, (1 - confidence_level) * 100),
            2
        ))


def calculate_parametric_var_1d(historical_total_pnl_values: np.ndarray, confidence_level: float) -> float:
    z_value = norm.ppf(1 - confidence_level)
    return float(
        round(
            np.std(historical_total_pnl_values, ddof=1) * round(z_value, 2),
            2
        ))


def calculate_total_var_1d(historical_total_pnl_values: np.ndarray) -> float:
    return round(
        0.4 * float(sorted(historical_total_pnl_values)[1]) + 0.6 * float(sorted(historical_total_pnl_values)[2]),
        2
    )
