import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Add a new column 'handwashing_start' that labels rows as 'Before' or 'After' June 1847
df['handwashing_start'] = np.where(df['date'] < '1847-06-01', 'Before', 'After')

# Add the 'pct_deaths' column to calculate the percentage of deaths per birth
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Reorder the 'handwashing_start' column so 'Before' comes before 'After'
df['handwashing_start'] = pd.Categorical(df['handwashing_start'], categories=['Before', 'After'], ordered=True)

# Create a box plot using Matplotlib
plt.figure(figsize=(10, 6))
df.boxplot(column='pct_deaths', by='handwashing_start', grid=False)

# Add labels, title, and formatting
plt.title('Comparison of Death Rates Before and After Handwashing')
plt.suptitle('')  # Remove the automatic "Boxplot grouped by" title
plt.xlabel('Period')
plt.ylabel('Percentage of Deaths')

# Save the plot as a PNG file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\death_rate_comparison_matplotlib.png"
plt.savefig(output_path)

print(f"Box plot saved to {output_path}")
