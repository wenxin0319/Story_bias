import json
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# load data from JSON files
with open("female_result.json", "r") as f:
    female_dict = json.load(f)

with open("male_result.json", "r") as f:
    male_dict = json.load(f)

# extract emotions from dictionaries
emotions = ["sadness", "joy", "love", "anger", "fear", "surprise"]
female_scores = [female_dict[emotion] for emotion in emotions]
male_scores = [male_dict[emotion] for emotion in emotions]

# perform paired t-tests and print results
for emotion, female, male in zip(emotions, female_scores, male_scores):
    result = stats.ttest_rel(a=np.array(female), b=np.array(male))
    print(f"{emotion.capitalize()} result: p-value = {result.pvalue:.4f}")

# create bar plot of average scores by gender
labels = emotions
men_means = [np.mean(scores) for scores in male_scores]
women_means = [np.mean(scores) for scores in female_scores]

x = np.arange(len(labels))
width = 0.4

fig, ax = plt.subplots(figsize=(9, 6))

rects1 = ax.bar(x - width/2, men_means, width, color="#6495ED", label="Men")
rects2 = ax.bar(x + width/2, women_means, width, color="#8FBC8F", label="Women")

# set axis labels and title
ax.set_ylabel("Average Scores")
ax.set_title("Emotion Scores by Gender")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# add labels to bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f"{height:.1f}", xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha="center", va="bottom")

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.savefig("./emotion_bar_plot.png")
