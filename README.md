# Clawdbot - NH Data Scraper

Data collection for New Hampshire wage and budget statistics.

## Data Files

- `data/nh_wage_data.json` - NH employment and wage statistics
- `data/nh_budget_data.json` - NH state budget data for FY 2026-2027
- `data/nh_state_employee_wage_increase_arguments.md` - Arguments supporting wage/COLA increases for NH state employees
- `data/nh_state_employee_purchasing_power_analysis.md` - Purchasing power loss analysis (2023-2026)

## NH Wage Data Summary

| Metric | Value |
|--------|-------|
| Average Hourly Wage | $33.08 (June 2025) |
| Total Employment | 683,160 |
| Minimum Wage | $7.25 (federal) |
| National Avg Weekly Wage | $1,589 |

### County Weekly Wages (Q1 2025)

| County | Weekly Wage | vs National Avg |
|--------|-------------|-----------------|
| Hillsborough | $1,652 | Above |
| Rockingham | $1,538 | Below |
| Grafton | $1,512 | Below |
| Merrimack | $1,319 | Below |
| Carroll | $959 | Below (lowest) |

## NH Budget Data Summary (FY 2026-2027)

| Metric | Value |
|--------|-------|
| Total Biennium Budget | ~$15.4 billion |
| DHHS Allocation | $7.1 billion |
| Federal Funding | $5.23 billion (~1/3 of total) |

### Revenue Projections

| Revenue Source | FY 2026 | FY 2027 |
|----------------|---------|---------|
| Business Taxes | $1,209.2M | $1,245.5M |
| Meals & Rentals Tax | $353.2M | $370.9M |
| Real Estate Transfer Tax | $214.0M | $231.1M |

## Data Sources

### Wage Data
- [BLS County Employment and Wages - NH](https://www.bls.gov/regions/northeast/news-release/countyemploymentandwages_newhampshire.htm)
- [NH Employment Security ELMI](https://www.nhes.nh.gov/elmi/products/oes-prod.htm)
- [BLS Economy at a Glance - NH](https://www.bls.gov/eag/eag.nh.htm)

### Budget Data
- [Governor's Executive Budget Summary FY 2026-2027](https://www.das.nh.gov/budget/Budget2026-2027/Governor_Executive_Summary_FY_2026-2027.pdf)
- [NHFPI State Budget Analysis](https://nhfpi.org/resource/the-state-budget-for-fiscal-years-2026-and-2027/)
- [Governor Kelly Ayotte's Budget Address](https://www.governor.nh.gov/news/2025-budget-address)

## Notes

Direct web scraping was blocked by site protections (403 errors) from official government sources. Data was compiled from search result summaries. For complete datasets, access the source URLs directly.
