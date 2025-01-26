import math

from scipy.stats import norm


def calculate_d1(spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float,
                 volatility: float) -> float:
    d1 = (math.log(spot_price / strike_price) + (risk_free_rate + (volatility ** 2) / 2) * time_to_maturity) / (
        volatility * math.sqrt(time_to_maturity))
    return d1


def calculate_d2(d1: float, volatility: float, time_to_maturity: float) -> float:
    d2 = d1 - volatility * math.sqrt(time_to_maturity)
    return d2


def call_option_price(spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float,
                      volatility: float) -> float:
    d1 = calculate_d1(spot_price, strike_price, time_to_maturity, risk_free_rate, volatility)
    d2 = calculate_d2(d1, volatility, time_to_maturity)
    return spot_price * norm.cdf(d1) - strike_price * math.exp(-risk_free_rate * time_to_maturity) * norm.cdf(d2)


def put_option_price(spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float,
                     volatility: float) -> float:
    d1 = calculate_d1(spot_price, strike_price, time_to_maturity, risk_free_rate, volatility)
    d2 = calculate_d2(d1, volatility, time_to_maturity)
    return strike_price * math.exp(-risk_free_rate * time_to_maturity) * norm.cdf(-d2) - spot_price * norm.cdf(-d1)
