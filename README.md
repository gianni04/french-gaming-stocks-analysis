# French Gaming Stocks — Portfolio Analysis

> A quantitative finance project analyzing 10 French and gaming-related stocks listed on Euronext Paris.
> Built with Python as part of a personal finance project portfolio.

---

## Stocks Analyzed

| Ticker | Company | Sector |
|--------|---------|--------|
| UBI.PA | Ubisoft Entertainment | Gaming |
| NACON.PA | Nacon | Gaming / Accessories |
| BIG.PA | Bigben Interactive | Gaming / Accessories |
| ALDNE.PA | Dontnod Entertainment | Indie Gaming |
| GUI.PA | Guillemot | Gaming Hardware |
| GFT.PA | Gameloft | Mobile Gaming |
| ATA.PA | Atari | Gaming (Historical) |
| FNAC.PA | Fnac Darty | Tech Distribution |
| DLT.PA | Dalet | Media Technology |
| ALVIV.PA | Visiativ | Software / Tech FR |

---

## Methodology

- **Period**: January 2022 — December 2024
- **Data source**: Yahoo Finance via `yfinance`
- **Risk-free rate**: 3% per annum (ECB reference)
- **Investment base**: €10,000 (for VaR calculation)

### Metrics computed

| Metric | Formula |
|--------|---------|
| Annualized Return | `mean(daily returns) × 252` |
| Annualized Volatility | `std(daily returns) × √252` |
| Sharpe Ratio | `(Ann. Return − Rf) / Ann. Volatility` |
| VaR 95% | `5th percentile of daily returns × investment` |
| VaR 99% | `1st percentile of daily returns × investment` |

---

## Output

All charts and metrics are saved in the `output/` folder:

- `metrics.csv` — full metrics table
- `cumulative_returns.png` — cumulative performance of all 10 stocks
- `sharpe_ratio.png` — horizontal bar chart ranked by Sharpe ratio
- `correlation_heatmap.png` — correlation matrix of daily returns

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## Author

**Gianni Pilotti** — Finance Student, University of Luxembourg  
AMF Certified | [LinkedIn](https://linkedin.com/in/giannipilots) | [GitHub](https://github.com/gianni04)

---

*This project is for educational and portfolio purposes only. Not financial advice.*
