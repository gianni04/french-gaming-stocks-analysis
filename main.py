import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === Create output folder first ===
os.makedirs("output", exist_ok=True)

# === 10 French & Gaming-related stocks ===
# Replaced delisted: GFT.PA, ATA.PA, DLT.PA, ALVIV.PA
# with: METAV.PA (XR Metaverse), HO.PA (Thales), ORA.PA (Orange), SGO.PA (Saint-Gobain)
tickers = {
    "UBI.PA":   "Ubisoft",
    "NACON.PA": "Nacon",
    "BIG.PA":   "Bigben Interactive",
    "ALDNE.PA": "Dontnod Entertainment",
    "GUI.PA":   "Guillemot",
    "FNAC.PA":  "Fnac Darty",
    "HO.PA":    "Thales",
    "ORA.PA":   "Orange",
    "SGO.PA":   "Saint-Gobain",
    "RNO.PA":   "Renault"
}

START = "2022-01-01"
END   = "2024-12-31"
INVESTMENT = 10_000  # EUR
RISK_FREE  = 0.03    # 3% annual risk-free rate (ECB reference)

# === Download data ===
print("Downloading data...")
raw = yf.download(list(tickers.keys()), start=START, end=END)["Close"]
raw.columns = [tickers[t] for t in raw.columns]
raw.dropna(axis=1, how="all", inplace=True)

# === Daily returns ===
returns = raw.pct_change().dropna()

# === Metrics ===
results = []
for col in returns.columns:
    r = returns[col].dropna()
    ann_return = r.mean() * 252
    ann_vol    = r.std() * np.sqrt(252)
    sharpe     = (ann_return - RISK_FREE) / ann_vol if ann_vol != 0 else np.nan
    var95      = np.percentile(r, 5) * INVESTMENT
    var99      = np.percentile(r, 1) * INVESTMENT
    results.append({
        "Stock":          col,
        "Ann. Return (%)": round(ann_return * 100, 2),
        "Volatility (%)": round(ann_vol    * 100, 2),
        "Sharpe Ratio":   round(sharpe,            3),
        "VaR 95% (EUR)":  round(var95,             2),
        "VaR 99% (EUR)":  round(var99,             2)
    })

df = pd.DataFrame(results).sort_values("Sharpe Ratio", ascending=False)
print("\n=== Portfolio Metrics ===")
print(df.to_string(index=False))
df.to_csv("output/metrics.csv", index=False)
print("Metrics saved.")

# === Chart 1: Cumulative Returns ===
cumulative = (1 + returns).cumprod()
plt.figure(figsize=(14, 7))
for col in cumulative.columns:
    plt.plot(cumulative[col], label=col)
plt.title("Cumulative Returns (2022-2024)", fontsize=15)
plt.xlabel("Date")
plt.ylabel("Cumulative Return (base 1)")
plt.legend(fontsize=8)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("output/cumulative_returns.png", dpi=150)
plt.close()
print("Chart 1 saved.")

# === Chart 2: Sharpe Ratio Bar Chart ===
df_sorted = df.sort_values("Sharpe Ratio")
colors = ["#2ecc71" if x > 0 else "#e74c3c" for x in df_sorted["Sharpe Ratio"]]
plt.figure(figsize=(10, 6))
plt.barh(df_sorted["Stock"], df_sorted["Sharpe Ratio"], color=colors)
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Sharpe Ratio by Stock", fontsize=15)
plt.xlabel("Sharpe Ratio")
plt.grid(True, axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig("output/sharpe_ratio.png", dpi=150)
plt.close()
print("Chart 2 saved.")

# === Chart 3: Correlation Heatmap ===
plt.figure(figsize=(10, 8))
sns.heatmap(returns.corr(), annot=True, fmt=".2f", cmap="RdYlGn",
            linewidths=0.5, square=True, vmin=-1, vmax=1)
plt.title("Correlation Matrix of Daily Returns", fontsize=15)
plt.tight_layout()
plt.savefig("output/correlation_heatmap.png", dpi=150)
plt.close()
print("Chart 3 saved.")

print("\nAll charts and metrics saved in /output folder.")
