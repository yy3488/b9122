from sklearn.linear_model import LinearRegression

import pandas as pd

import exercise1
import data_tools


def get_capm_data(tickers):
    rates = data_tools.get_risk_free_and_market_rates()

    stock_data = exercise1.download_and_merge(tickers)

    for ticker in tickers:
        stock_data[ticker] = stock_data[ticker].pct_change()

    merged = pd.merge(stock_data,
                      rates,
                      how="inner",
                      left_index=True,
                      right_index=True)

    merged.dropna(inplace=True)
    for rate in tickers + [data_tools.MARKET_RATE]:
        merged[rate] = merged[rate] - merged[data_tools.RISK_FREE]

    return merged


def run_capm_regression(tickers):

    data = get_capm_data(tickers)
    x = data["market_rate"].values.reshape(-1, 1)
    alphas = {}
    betas = {}

    for ticker in tickers:

        y = data[ticker].values.reshape(-1, 1)
        reg = LinearRegression().fit(x, y)
        alphas[ticker] = float(reg.intercept_[0])
        betas[ticker] = float(reg.coef_[0, 0])

    # print("alphas = ", alphas, "betas = ", betas, sep="\n")
    return alphas, betas


if "__main__" == __name__:
    print(run_capm_regression(["NVDA", "GOOG", "BRK-B"]))
