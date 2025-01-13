import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Football Players Data Analysis", layout="wide")

# Title
st.title("Football Players Data Analysis")

# File Upload
# uploaded_file = st.file_uploader("Upload the dataset (CSV format):", type="csv")
if True:
    df = pd.read_csv('./players.csv')

    # Sidebar Options
    st.sidebar.header("Navigation")
    option = st.sidebar.radio(
        "Select a section:",
        ("Dataset Overview", "Statistics", "Visualizations", "Key Insights")
    )

    # Display Dataset
    if option == "Dataset Overview":
        st.subheader("Dataset Overview")
        st.write(df)

    # Dataset Statistics
    elif option == "Statistics":
        st.subheader("Statistics")

        st.markdown("### Basic Information")
        st.write(f"**Number of Rows:** {df.shape[0]}")
        st.write(f"**Number of Columns:** {df.shape[1]}")

        st.markdown("### Column Data Types")
        st.write(df.dtypes)

        st.markdown("### Missing Values")
        st.write(df.isnull().sum())

        st.markdown("### Descriptive Statistics")
        st.write(df.describe())

    # Visualizations
    elif option == "Visualizations":
        st.subheader("Visualizations")

        # Market Value by Position
        st.markdown("### Market Value by Position")
        if 'Market_value' in df.columns and 'Position' in df.columns:
            position_value = df.groupby('Position').Market_value.mean().sort_values(ascending=False)
            fig, ax = plt.subplots(figsize=(10, 5))
            sb.barplot(x=position_value.index, y=position_value.values, ax=ax)
            ax.set_title('Average Market Value by Position')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            st.pyplot(fig)

        # Players' Age Distribution
        st.markdown("### Age Distribution")
        if 'Age' in df.columns:
            fig, ax = plt.subplots(figsize=(10, 5))
            sb.histplot(df['Age'], kde=True, color="blue", ax=ax)
            ax.set_title('Age Distribution of Players')
            ax.set_xlabel('Age')
            ax.set_ylabel('Count')
            st.pyplot(fig)

        # Top Clubs by Market Value
        st.markdown("### Top Clubs by Total Market Value")
        if 'Club' in df.columns and 'Market_value' in df.columns:
            top_clubs = df.groupby('Club').Market_value.sum().sort_values(ascending=False).head(10)
            fig, ax = plt.subplots(figsize=(10, 5))
            sb.barplot(x=top_clubs.index, y=top_clubs.values, ax=ax)
            ax.set_title('Top 10 Clubs by Total Market Value')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            st.pyplot(fig)

        # Top Players by Market Value
        st.markdown("### Top Players by Market Value")
        if 'Name' in df.columns and 'Market_value' in df.columns:
            top_players = df[['Name', 'Market_value']].sort_values(by='Market_value', ascending=False).head(10)
            fig, ax = plt.subplots(figsize=(10, 5))
            sb.barplot(x=top_players['Name'], y=top_players['Market_value'], ax=ax)
            ax.set_title('Top 10 Players by Market Value')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            st.pyplot(fig)

    # Insights Section
    elif option == "Key Insights":
        st.subheader("Key Insights")
        st.markdown(
            """
            - **Top Market Value Players**: Players like Kylian Mbappé and Erling Haaland lead the market.
            - **Positions Analysis**: Forwards have the highest average market value, followed by midfielders.
            - **Club Insights**: Manchester City leads in total market value.
            - **Age Analysis**: The majority of players are in the 20-30 age range.
            """
        )
else:
    st.info("Please upload a dataset to proceed.")
