import streamlit as st

from utils.navigation import render_top_navigation
from utils.ui import (
    apply_global_styles,
    page_footer,
    page_header,
)


# --------------------------------------------------
# Application configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# --------------------------------------------------
# Register application pages
# --------------------------------------------------
home_page = st.Page(
    "pages/0_Home.py",
    title="Home",
    icon="🏠",
    default=True,
)

overview_page = st.Page(
    "pages/1_Data_Overview.py",
    title="Data Overview",
    icon="📋",
    url_path="data-overview",
)

sales_page = st.Page(
    "pages/2_Sales_Analysis.py",
    title="Sales Analysis",
    icon="📈",
    url_path="sales-analysis",
)

profit_page = st.Page(
    "pages/3_Profit_Analysis.py",
    title="Profit Analysis",
    icon="💰",
    url_path="profit-analysis",
)

upload_page = st.Page(
    "pages/4_Upload_Data.py",
    title="Upload Data",
    icon="📤",
    url_path="upload-data",
)


# --------------------------------------------------
# Create hidden Streamlit navigation
# --------------------------------------------------
current_page = st.navigation(
    [
        home_page,
        overview_page,
        sales_page,
        profit_page,
        upload_page,
    ],
    position="hidden",
)


# --------------------------------------------------
# Header details for each page
# --------------------------------------------------
page_metadata = {
    "Home": {
        "title": "Sales Analytics Dashboard",
        "subtitle": (
            "Explore sales performance, profitability, data quality, "
            "and business trends through one interactive workspace."
        ),
        "icon": "📊",
        "eyebrow": "Business Intelligence",
    },
    "Data Overview": {
        "title": "Data Overview",
        "subtitle": (
            "Understand the structure, quality, and contents "
            "of the active sales dataset."
        ),
        "icon": "📋",
        "eyebrow": "Dataset Inspection",
    },
    "Sales Analysis": {
        "title": "Sales Analysis",
        "subtitle": (
            "Explore sales performance across products, regions, "
            "customers, and time periods."
        ),
        "icon": "📈",
        "eyebrow": "Sales Intelligence",
    },
    "Profit Analysis": {
        "title": "Profit Analysis",
        "subtitle": (
            "Analyze profitability, margins, products, "
            "regions, and profit trends."
        ),
        "icon": "💰",
        "eyebrow": "Profitability Insights",
    },
    "Upload Data": {
        "title": "Upload Data",
        "subtitle": (
            "Upload, validate, preview, and activate "
            "a custom sales CSV dataset."
        ),
        "icon": "📤",
        "eyebrow": "Data Management",
    },
}


# Get metadata for the currently selected page
metadata = page_metadata[current_page.title]


# --------------------------------------------------
# Shared application layout
# --------------------------------------------------
apply_global_styles()

page_header(
    title=metadata["title"],
    subtitle=metadata["subtitle"],
    icon=metadata["icon"],
    eyebrow=metadata["eyebrow"],
)

render_top_navigation()

current_page.run()

page_footer()