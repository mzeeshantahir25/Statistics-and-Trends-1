import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Global_Education.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Set a commonly available style
plt.style.use("ggplot")

# Define functions for each plot with bold text and legends

def scatter_plot():
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(data['Youth_15_24_Literacy_Rate_Male'],
                          data['Youth_15_24_Literacy_Rate_Female'],
                          c=data['Gross_Primary_Education_Enrollment'], cmap='viridis', alpha=0.7)
    colorbar = plt.colorbar(scatter)
    colorbar.set_label('Gross Primary Education Enrollment', fontsize=12, fontweight='bold')
    plt.title('Youth Literacy Rate (Male vs Female)', fontsize=14, fontweight='bold')
    plt.xlabel('Literacy Rate Male (15-24)', fontsize=12, fontweight='bold')
    plt.ylabel('Literacy Rate Female (15-24)', fontsize=12, fontweight='bold')
    plt.grid(True)
    plt.show()

def box_plot():
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=[data['Youth_15_24_Literacy_Rate_Male'], data['Youth_15_24_Literacy_Rate_Female']])
    plt.xticks([0, 1], ['Male Literacy Rate', 'Female Literacy Rate'], fontsize=12, fontweight='bold')
    plt.title('Distribution of Literacy Rates (Male vs Female)', fontsize=14, fontweight='bold')
    plt.ylabel('Literacy Rate (15-24)', fontsize=12, fontweight='bold')
    plt.show()

def bar_plot():
    top_10_unemployment = data[['Countries and areas', 'Unemployment_Rate']].sort_values(by='Unemployment_Rate', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Unemployment_Rate', y='Countries and areas', data=top_10_unemployment, palette="viridis")
    plt.title('Top 10 Countries by Unemployment Rate', fontsize=14, fontweight='bold')
    plt.xlabel('Unemployment Rate', fontsize=12, fontweight='bold')
    plt.ylabel('Country', fontsize=12, fontweight='bold')
    plt.show()

def pie_chart():
    # Pie chart for categories of Youth Literacy Rate (Male)
    literacy_groups = pd.cut(data['Youth_15_24_Literacy_Rate_Male'], bins=[0, 50, 75, 100], labels=['Low', 'Medium', 'High'])
    literacy_counts = literacy_groups.value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(literacy_counts, labels=literacy_counts.index, autopct='%1.1f%%', startangle=140, 
            colors=['#ff9999','#66b3ff','#99ff99'], textprops={'fontsize': 12, 'fontweight':'bold'})
    plt.title('Distribution of Youth Literacy Rate (Male)', fontsize=14, fontweight='bold')
    plt.show()

def line_plot():
    # Line plot of Gross Primary and Tertiary Education Enrollment for top 15 countries by Primary Enrollment
    top_15_countries = data.nlargest(15, 'Gross_Primary_Education_Enrollment')
    
    plt.figure(figsize=(12, 6))
    plt.plot(top_15_countries['Countries and areas'], 
             top_15_countries['Gross_Primary_Education_Enrollment'], 
             label='Primary Education Enrollment', marker='o', linewidth=2)
    plt.plot(top_15_countries['Countries and areas'], 
             top_15_countries['Gross_Tertiary_Education_Enrollment'], 
             label='Tertiary Education Enrollment', marker='o', linewidth=2, linestyle='--')
    
    plt.xticks(rotation=45, fontsize=10, ha='right', fontweight='bold')
    plt.title('Gross Primary vs Tertiary Education Enrollment (Top 15 Countries by Primary Enrollment)', fontsize=14, fontweight='bold')
    plt.xlabel('Countries', fontsize=12, fontweight='bold')
    plt.ylabel('Enrollment Percentage', fontsize=12, fontweight='bold')
    plt.legend(fontsize=12, loc='upper right', frameon=True, fancybox=True, borderpad=1, title='Enrollment Type')
    plt.setp(plt.gca().get_legend().get_texts(), fontweight='bold')  # Set legend text to bold
    plt.setp(plt.gca().get_legend().get_title(), fontweight='bold')  # Set legend title to bold
    plt.show()

# Call each updated plot function
scatter_plot()
box_plot()
bar_plot()
pie_chart()
line_plot()

# Statistical summaries
# Describe: General summary of numerical columns
stats_description = data.describe()

# Correlation matrix: Pairwise correlation of columns
correlation_matrix = data.corr(numeric_only=True)

# Skewness: Measure of asymmetry of the distribution of values
skewness = data.skew(numeric_only=True)

# Kurtosis: Measure of "tailedness" of the distribution
kurtosis = data.kurtosis(numeric_only=True)

# Display statistical results
stats_description, correlation_matrix, skewness, kurtosis