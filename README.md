# Sales Analytics Dashboard

A professional, interactive, multipage sales analytics application built with **Streamlit**, **Pandas**, and **Plotly**.

The dashboard allows users to explore sales and profit performance, inspect data quality, apply advanced filters, upload custom CSV datasets, and download filtered results.

---

## Overview

The Sales Analytics Dashboard provides a user-friendly workspace for analyzing business data without writing SQL or Python code.

It includes dedicated pages for:

- Dashboard overview
- Data profiling and quality checks
- Sales analysis
- Profit analysis
- CSV upload and validation
- Filtered data export

The application uses a reusable component-based structure so that styling, navigation, filtering, formatting, and data handling remain consistent across all pages.

---

## Features

### Professional Multipage Interface

- Shared header and footer
- Horizontal navigation bar
- Responsive dashboard layout
- Reusable KPI cards
- Consistent dark theme
- User-friendly empty states and information panels

### Data Overview

- Total rows and columns
- Missing-value count
- Duplicate-row count
- Friendly column data types
- Column-level quality information
- Dataset preview
- Numerical summary statistics

### Sales Analysis

- Total sales
- Average sale value
- Unique order count
- Top-performing region
- Monthly sales trend
- Sales by region
- Sales by product
- Customer sales analysis

### Profit Analysis

- Total profit
- Average profit
- Profit margin
- Top-performing product
- Monthly profit trend
- Profit by product
- Profit share by region
- Sales-versus-profit relationship

### Interactive Filters

Users can filter the active dataset by:

- Date range
- Region
- Product
- Customer
- Sales range
- Profit range

Filters automatically update KPIs, tables, and charts.

### CSV Upload and Validation

Users can upload a custom CSV file directly from the dashboard.

The application:

- Validates required columns
- Converts dates and numeric values
- Removes invalid records
- Removes duplicate rows
- Displays upload statistics
- Previews cleaned data
- Makes the uploaded dataset available across all pages

### Data Export

Users can download filtered sales and profit records as CSV files.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application language |
| Streamlit | Dashboard interface and multipage application |
| Pandas | Data loading, cleaning, filtering, and aggregation |
| Plotly | Interactive charts and visualizations |
| HTML/CSS | Reusable professional styling |

---

## Required CSV Columns

Uploaded datasets must contain the following columns:

| Column | Description |
|---|---|
| `Order_ID` | Unique order identifier |
| `Order_Date` | Date of the order |
| `Region` | Sales region |
| `Product` | Product name |
| `Customer` | Customer name |
| `Sales` | Sales amount |
| `Profit` | Profit amount |

Example:

```csv
Order_ID,Order_Date,Region,Product,Customer,Sales,Profit
1001,2025-01-05,North,Laptop,Customer A,4500,1200
1002,2025-01-07,West,Mobile,Customer B,2100,550
1003,2025-01-10,East,Monitor,Customer C,1750,410
```

---

## Project Structure

```text
streamlit-project/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── sales_bulk_data.csv
│
├── pages/
│   ├── 0_Home.py
│   ├── 1_Data_Overview.py
│   ├── 2_Sales_Analysis.py
│   ├── 3_Profit_Analysis.py
│   └── 4_Upload_Data.py
│
├── scripts/
│   └── generate_bulk_data.py
│
└── utils/
    ├── __init__.py
    ├── components.py
    ├── data_loader.py
    ├── export.py
    ├── filters.py
    ├── formatters.py
    ├── navigation.py
    └── ui.py
```

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/rimsha7/streamlit-sales-dashboard.git
cd streamlit-sales-dashboard
```

### 2. Create a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

---

## Generate Sample Bulk Data

The repository includes a script for generating sample sales records.

Run:

```powershell
python scripts/generate_bulk_data.py
```

The generated file will be saved as:

```text
data/sales_bulk_data.csv
```

The number of generated rows can be changed inside:

```text
scripts/generate_bulk_data.py
```

---

## Application Workflow

1. The dashboard loads the default bulk sales CSV.
2. Users can explore the Home and Data Overview pages.
3. Filters can be applied on the Home, Sales Analysis, and Profit Analysis pages.
4. Users can upload another valid CSV file from the Upload Data page.
5. The cleaned uploaded dataset becomes active across the application.
6. Users can return to the default dataset at any time.
7. Filtered results can be exported as CSV files.

---

## Security and Repository Notes

The following files should not be committed:

```text
.venv/
.env
.streamlit/secrets.toml
__pycache__/
```

The project theme configuration should remain committed:

```text
.streamlit/config.toml
```

---

## Screenshots

Add application screenshots here after uploading them to a folder such as `assets/`.

Example:

```markdown
![Dashboard Home](assets/dashboard-home.png)
![Sales Analysis](assets/sales-analysis.png)
![Profit Analysis](assets/profit-analysis.png)
```

---

## Future Enhancements

- Snowflake database integration
- User authentication
- Role-based access
- Pagination for large tables
- Additional business KPIs
- Automated data refresh
- Excel and PDF export
- Streamlit Community Cloud deployment
- Docker deployment
- Automated testing and CI/CD

---

## Author

**Rimsha Tehreem**

GitHub: [rimsha7](https://github.com/rimsha7)

---
