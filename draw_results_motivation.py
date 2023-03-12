import matplotlib.pyplot as plt
import numpy as np
# define the array
arr = [ ('world', 132, 152), ('family', 130, 127), ('house', 81, 82),('friend', 64, 129), ('dream', 59, 70),  ('peace', 56, 51), ('work', 46, 46), ('love', 38, 58), ('help', 32, 36), ('money', 32, 32), ('book', 30, 36), ('king', 26, 20), ('child', 24, 33), ('power', 24, 25), ('business', 22, 15), ('beauty', 21, 27), ('garden', 20, 33), ('future', 17, 20), ('hero', 17, 15), ('hope', 16, 26), ('company', 16, 13), ('adventure', 16, 33),('proud', 13, 15),('experience', 12, 11), ('stone', 12, 5), ('window', 12, 13), ('creature', 12, 14), ('knowledge', 12, 12), ('trip', 11, 14), ('career', 11, 8), ('energy', 11, 6), ('kitchen', 11, 15), ('content', 11, 7),('captain', 10, 9), ('leader', 10, 7),('doctor', 9, 6), ('baby', 8, 15), ('war', 8, 5), ('study', 8, 6), ('opportunity', 8, 16), ('president', 8, 6), ('wealth', 7, 3), ('success', 7, 12),('challenge', 6, 9), ('satisfaction', 6, 14), ('wisdom', 6, 4), ('promotion', 6, 9)]

# separate the data into male and female lists
male_data = [x[1] for x in arr]
female_data = [x[2] for x in arr]

# define the x-axis labels
x_labels = [x[0] for x in arr]

bar_width = 0.35

# create the figure and the axes
fig, ax = plt.subplots()

# create the bars for male and female data
male_bars = ax.bar(np.arange(len(x_labels)), male_data, bar_width, label='Male')
female_bars = ax.bar(np.arange(len(x_labels)) + bar_width, female_data, bar_width, label='Female')

# add chart titles and labels
ax.set_title('Word Occurrences in Male and Female Stories')
ax.set_xlabel('Words')
ax.set_ylabel('Frequency')
ax.set_xticks(np.arange(len(x_labels)) + bar_width / 2)
ax.set_xticklabels(x_labels, rotation=90)
ax.legend()
# adjust the figure layout
fig.tight_layout()
plt.savefig(f"./pics2/motivation_gender.png")
