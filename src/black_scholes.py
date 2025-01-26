import math

from scipy.stats import norm


def calculate_d1(spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float, volatility: float):
    """
    :param spot_price: (float) Current price of the underlying asset (spot price).
    :param strike_price: (float) strike price of the option.
    :param time_to_maturity: (float) Time to maturity (in years).
    :param risk_free_rate: (float) Risk-free interest rate (annualized).
    :param volatility: (float) Volatility of the underlying asset (annualized).
    :return: (float) Value of d1.
    """
    d1 = (math.log(spot_price / strike_price) + (risk_free_rate + (volatility ** 2) / 2) * time_to_maturity) / (
            volatility * math.sqrt(time_to_maturity))
    return d1


def calculate_d2(d1: float, volatility: float, time_to_maturity: float):
    """
    :param d1: (float) Value of d1.
    :param time_to_maturity: (float) Time to maturity (in years).
    :param volatility: (float) Volatility of the underlying asset (annualized).
    :return: (float) Value of d2.
    """
    d2 = d1 - volatility * math.sqrt(time_to_maturity)
    return d2


def call_option_price(spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float, volatility: float):
    """
    :param spot_price: (float) Current price of the underlying asset (spot price).
    :param strike_price: (float) trike price of the option.
    :param time_to_maturity: (float) Time to maturity (in years).
    :param risk_free_rate: (float) Risk-free interest rate (annualized).
    :param volatility: (float) Volatility of the underlying asset (annualized).
    :return: (float) Price of the call option.
    """
    d1 = calculate_d1(spot_price, strike_price, time_to_maturity, risk_free_rate, volatility)
    d2 = calculate_d2(d1, volatility, time_to_maturity)
    return spot_price * norm.cdf(d1) - strike_price * math.exp(-risk_free_rate * time_to_maturity) * norm.cdf(d2)


def put_option_price(spot_price: float, strike_price: float, time_to_maturity: float, risk_free_rate: float, volatility: float):
    """
    :param spot_price: (float) Current price of the underlying asset (spot price).
    :param strike_price: (float) trike price of the option.
    :param time_to_maturity: (float) Time to maturity (in years).
    :param risk_free_rate: (float) Risk-free interest rate (annualized).
    :param volatility: (float) Volatility of the underlying asset (annualized).
    :return: (float) Price of the put option.
    """
    d1 = calculate_d1(spot_price, strike_price, time_to_maturity, risk_free_rate, volatility)
    d2 = calculate_d2(d1, volatility, time_to_maturity)
    return strike_price * math.exp(-risk_free_rate * time_to_maturity) * norm.cdf(-d2) - spot_price * norm.cdf(-d1)
