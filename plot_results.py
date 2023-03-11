import pandas as pd
import matplotlib.pyplot as plt
import ipdb
import seaborn as sns
from matplotlib.patches import Patch

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('comet_median.csv')
results = pd.DataFrame(columns=['Gender', 'Type', 'Dimension', 'Median', 'Mean', 'CI'])
# Loop through each group of 6 rows in the original DataFrame
for i in range(0, len(df), 3):
    # Extract the gender and type from the category column
    category = df.loc[i, 'category']
    gender = category.split('_')[0]
    type = "_".join(category.split('_')[1:])

    # Loop through each dimension in the group
    for j in range(3):
        dim = df.loc[i+j, 'dimension']
        median = df.loc[i+j, 'median']
        mean = df.loc[i+j, 'mean']
        ci = df.loc[i+j, 'ci']
        
        # Append the results to the new DataFrame
        results = results.append({'Category': category, 'Gender': gender, 'Type': type, 'Dimension': dim, 'Median': median, 'Mean': mean, 'CI': ci}, ignore_index=True)


# set the style of the plot
sns.set_style("whitegrid")

for dimension in ['valence', 'arousal', 'dominance']:
    # loop through each type
    for t in ['at', 'xr', 'or_obj', 'or_subj']:
        data = results[(results['Dimension']==dimension) & (results['Type']==t)]
        ax = sns.catplot(x="Gender", y="Median", hue="Gender", data=data, kind="point")

        ax.fig.suptitle(f"{t.upper()} {dimension.capitalize()} by Gender")
        ax.set_ylabels(f"Median {dimension.capitalize()}")
        plt.savefig(f"./pics/{t}_{dimension}_median_by_gender.png")

        ax = sns.catplot(x="Gender", y="Mean", hue="Gender", data=data, kind="point")

        ax.fig.suptitle(f"{t.upper()} {dimension.capitalize()} by Gender")
        ax.set_ylabels(f"Mean {dimension.capitalize()}")
        plt.savefig(f"./pics/{t}_{dimension}_mean_by_gender.png")

        ax = sns.catplot(x="Gender", y="CI", hue="Gender", data=data, kind="point")

        ax.fig.suptitle(f"{t.upper()} {dimension.capitalize()} by Gender")
        ax.set_ylabels(f"CI {dimension.capitalize()}")
        plt.savefig(f"./pics/{t}_{dimension}_CI_by_gender.png")
   