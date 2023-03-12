import pandas as pd
import matplotlib.pyplot as plt
import ipdb
import seaborn as sns
from matplotlib.patches import Patch

# Create a pandas dataframe with the scores
df = pd.DataFrame({
    'gender': ['male', 'male', 'male', 'female', 'female', 'female'],
    'attribute': ['Intellect', 'Appearance', 'Power'] * 2,
    'score': [0.14751535049359316, 0.03807869180845424, 0.041734025328270315,0.11592887413971524, 0.08072345087352319, 0.025754913207865597]
})

# Create a categorical plot for each attribute
for attribute in ['Intellect', 'Appearance', 'Power']:
    sns.catplot(x='gender', y='score', hue='gender', data=df[df['attribute'] == attribute],
                 kind="point", legend=True)
    plt.title(attribute)
    plt.ylabel('Score')
    plt.savefig(f"./pics2/{attribute}_by_gender.png")
