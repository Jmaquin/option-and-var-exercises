import math

import pytest
from numpy.ma.testutils import assert_equal
from scipy.stats import norm

from src.black_scholes import calculate_d1, calculate_d2, call_option_price, put_option_price

# Given
test_params = {
    "spot_price": 100,
    "strike_price": 100,
    "time_to_maturity": 1,
    "risk_free_rate": 0.05,
    "volatility": 0.2,
}


def test_calculate_d1():
    # When
    result = calculate_d1(
        test_params["spot_price"],
        test_params["strike_price"],
        test_params["time_to_maturity"],
        test_params["risk_free_rate"],
        test_params["volatility"],
    )

    # Then
    expected_d1 = (math.log(test_params["spot_price"] / test_params["strike_price"]) +
                   (test_params["risk_free_rate"] + (test_params["volatility"] ** 2) / 2) *
                   test_params["time_to_maturity"]) / (
                      test_params["volatility"] * math.sqrt(test_params["time_to_maturity"]))
    assert_equal(result, expected_d1)


def test_calculate_d2():
    # Given
    d1 = 0.5

    # When
    result = calculate_d2(d1, test_params["volatility"], test_params["time_to_maturity"])

    # Then
    expected_d2 = d1 - test_params["volatility"] * math.sqrt(test_params["time_to_maturity"])
    assert_equal(result, expected_d2)


def test_call_option_price():
    # Given
    d1 = calculate_d1(
        test_params["spot_price"],
        test_params["strike_price"],
        test_params["time_to_maturity"],
        test_params["risk_free_rate"],
        test_params["volatility"],
    )
    d2 = calculate_d2(d1, test_params["volatility"], test_params["time_to_maturity"])

    # When
    result = call_option_price(**test_params)

    # Then
    expected_call_price = (test_params["spot_price"] * norm.cdf(d1) -
                           test_params["strike_price"] * math.exp(
            -test_params["risk_free_rate"] * test_params["time_to_maturity"]) * norm.cdf(d2))
    assert_equal(result, expected_call_price)


def test_put_option_price():
    # Given
    d1 = calculate_d1(
        test_params["spot_price"],
        test_params["strike_price"],
        test_params["time_to_maturity"],
        test_params["risk_free_rate"],
        test_params["volatility"],
    )
    d2 = calculate_d2(d1, test_params["volatility"], test_params["time_to_maturity"])

    # When
    result = put_option_price(**test_params)

    # Then
    expected_put_price = (test_params["strike_price"] * math.exp(
        -test_params["risk_free_rate"] * test_params["time_to_maturity"]) * norm.cdf(-d2) -
                          test_params["spot_price"] * norm.cdf(-d1))
    assert_equal(result, expected_put_price)


def test_d1_with_zero_volatility():
    with pytest.raises(ZeroDivisionError):
        calculate_d1(
            test_params["spot_price"],
            test_params["strike_price"],
            test_params["time_to_maturity"],
            test_params["risk_free_rate"],
            0,
        )


def test_d2_with_zero_volatility():
    # Given
    d1 = 0.5
    volatility = 0

    # When
    result = calculate_d2(d1, volatility, test_params["time_to_maturity"])

    # Then
    expected_d2 = d1
    assert_equal(result, expected_d2)
