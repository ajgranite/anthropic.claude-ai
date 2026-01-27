# CLAUDE.md - AI Assistant Guide

## Repository Overview

**Name:** Clawdbot - NH Data Scraper
**Purpose:** Data collection and analysis repository for New Hampshire wage, budget, and state employee compensation statistics.

This repository contains curated data and analysis supporting labor advocacy for NH state employees, particularly regarding wage/COLA (Cost of Living Adjustment) negotiations.

## Repository Structure

```
/
├── README.md                    # Project overview with data summaries
├── CLAUDE.md                    # This file - AI assistant guide
└── data/
    ├── nh_wage_data.json        # NH employment and wage statistics (BLS data)
    ├── nh_budget_data.json      # NH state budget data FY 2026-2027
    ├── nh_state_employee_wage_increase_arguments.md   # Advocacy arguments
    ├── nh_state_employee_purchasing_power_analysis.md # Purchasing power analysis
    └── sea_1984_contract_2025-2027.md                 # Union contract reference
```

## File Descriptions

### Data Files (JSON)

| File | Description | Key Metrics |
|------|-------------|-------------|
| `nh_wage_data.json` | BLS wage/employment data | Average hourly wage ($33.08), county wages, occupational data |
| `nh_budget_data.json` | State budget FY 2026-2027 | Total budget (~$15.4B), revenue projections, appropriations |

### Analysis Documents (Markdown)

| File | Description | Purpose |
|------|-------------|---------|
| `nh_state_employee_wage_increase_arguments.md` | Arguments supporting wage increases | Labor advocacy reference |
| `nh_state_employee_purchasing_power_analysis.md` | Purchasing power loss analysis 2023-2026 | Quantifies inflation impact |
| `sea_1984_contract_2025-2027.md` | SEA/SEIU Local 1984 contract guide | Quick reference for contract provisions |

## Key Data Points for Quick Reference

### Wage Context
- NH average hourly wage: $33.08 (June 2025)
- State employee average salary: $60,054
- Private sector pay gap: ~20% higher than state positions
- Minimum wage: $7.25 (federal, lowest in New England)

### Cost of Living
- Housing costs: +113% since 2015
- Cost of living: 12-15% above national average
- Northeast inflation (2025): 3.3% vs national 2.7%

### State Workforce Issues
- Vacancy rate: ~19% (vs 11% historical average)
- Temporary staffing budget: $11.5M (tripled from $3.8M)
- 31% of labor force age 55+

### State Budget (FY 2026-2027)
- Total biennium budget: ~$15.4 billion
- Federal funding: $5.23B (~1/3 of total)
- DHHS allocation: $7.1 billion (largest category)

## Conventions

### Data Sources
Data is compiled from authoritative sources:
- U.S. Bureau of Labor Statistics (BLS)
- NH Employment Security
- NH Department of Administrative Services
- NH Fiscal Policy Institute
- SEA/SEIU Local 1984 official documents

### JSON Schema Pattern
JSON data files follow a consistent structure:
```json
{
  "metadata": {
    "source": "...",
    "last_updated": "...",
    "scraped_date": "..."
  },
  "data_sections": { ... },
  "data_sources": [ ... ]
}
```

### Markdown Documents
Analysis documents include:
- Executive summary at top
- Section headers with `---` separators
- Data tables in GitHub-flavored markdown
- Source citations with URLs

## Working with This Repository

### For Data Updates
1. Update JSON files with new data
2. Update `metadata.scraped_date` and `metadata.last_updated`
3. Add new data sources to `data_sources` array
4. Update README.md summary tables if key metrics change

### For New Analysis Documents
1. Create in `data/` directory
2. Use consistent markdown formatting
3. Include executive summary, data tables, and sources
4. Update README.md to reference new files

### Data Limitations
- Some government sources block direct web scraping (403 errors)
- Data may be compiled from search results when direct access fails
- Always verify against primary sources for critical decisions

## Union Contract Reference

The `sea_1984_contract_2025-2027.md` file is a comprehensive reference guide for the SEA/SEIU Local 1984 collective bargaining agreement. Key sections:

| Topic | Reference |
|-------|-----------|
| Wages | Article XIX |
| Work Schedules | Article VI |
| Overtime | Article VII |
| Holidays | Article IX |
| Annual Leave | Article X |
| Sick Leave | Article XI |
| Health Insurance | Article 19.8 |
| Grievance Procedure | Article XIV |

### Important Contract Dates
- FY 2027 wage reopener deadline: January 30, 2026
- Contract expiration: June 30, 2027
- Renegotiation notice deadline: October 18, 2026

## AI Assistant Guidelines

### When Answering Questions About This Data
1. Cite specific data points with source files
2. Note data currency (check `scraped_date` in JSON metadata)
3. Provide context for statistics (e.g., comparisons to private sector, national averages)

### When Updating Data
1. Preserve JSON schema structure
2. Maintain source attribution
3. Update both data files AND summary documents
4. Keep markdown tables consistent with JSON data

### Topics This Repository Addresses
- NH state employee compensation analysis
- Cost of living impacts on workers
- State budget allocation and trends
- Labor contract provisions (SEA/SEIU Local 1984)
- Arguments for wage/COLA increases

### This Repository Does NOT Contain
- Executable code or scripts
- Automated scraping tools (blocked by source protections)
- Personal employee data
- Confidential negotiation materials
