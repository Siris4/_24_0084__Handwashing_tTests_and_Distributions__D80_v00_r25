import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Add the 'pct_deaths' column to calculate the percentage of deaths per birth
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Create a histogram using Plotly Express to show the distribution of monthly death percentages
fig = px.histogram(df,
                   x='pct_deaths',
                   nbins=20,  # Adjust the number of bins as needed
                   title='Distribution of Monthly Death Percentages',
                   labels={'pct_deaths': 'Percentage of Deaths'},
                   opacity=0.75)

# Customize the layout and style
fig.update_layout(
    xaxis_title="Percentage of Deaths",
    yaxis_title="Count of Months",
    bargap=0.1,  # Adjust the gap between bars
    bargroupgap=0.1  # Adjust the gap between groups
)

# Display the plot
fig.show()
