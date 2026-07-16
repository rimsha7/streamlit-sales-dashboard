import pandas as pd
import streamlit as st


def render_dashboard_filters(
    dataframe: pd.DataFrame,
    key_prefix: str,
) -> pd.DataFrame:
    """
    Render a filter panel and return the filtered dataframe.

    Empty Region, Product, and Customer selections mean all values.
    """

    if dataframe.empty:
        return dataframe.copy()

    filtered_data = dataframe.copy()

    minimum_date = dataframe["Order_Date"].min().date()
    maximum_date = dataframe["Order_Date"].max().date()

    minimum_sales = int(dataframe["Sales"].min())
    maximum_sales = int(dataframe["Sales"].max())

    minimum_profit = int(dataframe["Profit"].min())
    maximum_profit = int(dataframe["Profit"].max())

    date_key = f"{key_prefix}_date"
    region_key = f"{key_prefix}_region"
    product_key = f"{key_prefix}_product"
    customer_key = f"{key_prefix}_customer"
    sales_key = f"{key_prefix}_sales"
    profit_key = f"{key_prefix}_profit"

    with st.container(border=True):
        filter_heading, reset_column = st.columns([5, 1])

        with filter_heading:
            st.markdown("### 🔎 Filter Dashboard Data")
            st.caption(
                "Leave Region, Product, or Customer empty "
                "to include every value."
            )

        with reset_column:
            st.write("")

            if st.button(
                "Reset",
                icon="🔄",
                width="stretch",
                key=f"{key_prefix}_reset",
            ):
                filter_keys = [
                    date_key,
                    region_key,
                    product_key,
                    customer_key,
                    sales_key,
                    profit_key,
                ]

                for key in filter_keys:
                    st.session_state.pop(key, None)

                st.rerun()

        first_column, second_column, third_column = st.columns(3)

        with first_column:
            selected_dates = st.date_input(
                "Date range",
                value=(minimum_date, maximum_date),
                min_value=minimum_date,
                max_value=maximum_date,
                key=date_key,
            )

        with second_column:
            selected_regions = st.multiselect(
                "Region",
                options=sorted(
                    dataframe["Region"]
                    .dropna()
                    .unique()
                    .tolist()
                ),
                placeholder="All regions",
                key=region_key,
            )

        with third_column:
            selected_products = st.multiselect(
                "Product",
                options=sorted(
                    dataframe["Product"]
                    .dropna()
                    .unique()
                    .tolist()
                ),
                placeholder="All products",
                key=product_key,
            )

        fourth_column, fifth_column, sixth_column = st.columns(3)

        with fourth_column:
            selected_customers = st.multiselect(
                "Customer",
                options=sorted(
                    dataframe["Customer"]
                    .dropna()
                    .unique()
                    .tolist()
                ),
                placeholder="All customers",
                key=customer_key,
            )

        with fifth_column:
            if minimum_sales < maximum_sales:
                selected_sales_range = st.slider(
                    "Sales range",
                    min_value=minimum_sales,
                    max_value=maximum_sales,
                    value=(minimum_sales, maximum_sales),
                    key=sales_key,
                )
            else:
                selected_sales_range = (
                    minimum_sales,
                    maximum_sales,
                )

                st.number_input(
                    "Sales",
                    value=minimum_sales,
                    disabled=True,
                )

        with sixth_column:
            if minimum_profit < maximum_profit:
                selected_profit_range = st.slider(
                    "Profit range",
                    min_value=minimum_profit,
                    max_value=maximum_profit,
                    value=(minimum_profit, maximum_profit),
                    key=profit_key,
                )
            else:
                selected_profit_range = (
                    minimum_profit,
                    maximum_profit,
                )

                st.number_input(
                    "Profit",
                    value=minimum_profit,
                    disabled=True,
                )

    if len(selected_dates) == 2:
        start_date = pd.to_datetime(selected_dates[0])
        end_date = pd.to_datetime(selected_dates[1])

        filtered_data = filtered_data[
            (filtered_data["Order_Date"] >= start_date)
            & (filtered_data["Order_Date"] <= end_date)
        ]

    if selected_regions:
        filtered_data = filtered_data[
            filtered_data["Region"].isin(selected_regions)
        ]

    if selected_products:
        filtered_data = filtered_data[
            filtered_data["Product"].isin(selected_products)
        ]

    if selected_customers:
        filtered_data = filtered_data[
            filtered_data["Customer"].isin(selected_customers)
        ]

    filtered_data = filtered_data[
        (
            filtered_data["Sales"]
            >= selected_sales_range[0]
        )
        & (
            filtered_data["Sales"]
            <= selected_sales_range[1]
        )
        & (
            filtered_data["Profit"]
            >= selected_profit_range[0]
        )
        & (
            filtered_data["Profit"]
            <= selected_profit_range[1]
        )
    ]

    st.caption(
        f"Showing **{len(filtered_data):,}** "
        f"of **{len(dataframe):,}** records."
    )

    return filtered_data.reset_index(drop=True)