import os
import glob
import json
import numpy as np
from transformers import pipeline

def read_stories(filename):
    stories = []
    with open(filename, 'r') as f:
        for line in f:
            stories.append(line.strip())
    return stories

female_stories = read_stories("result/female_stories.txt")
male_stories = read_stories("result/male_stories.txt")

female_scores = {"sadness":[], "joy":[], "love":[], "anger":[], "fear":[], "surprise":[]}
male_scores = {"sadness":[], "joy":[], "love":[], "anger":[], "fear":[], "surprise":[]}

classifier = pipeline(
    "text-classification", 
    model='bhadresh-savani/distilbert-base-uncased-emotion', 
    return_all_scores=True, 
    truncation=True, 
    max_length=512
)

for i in range(len(female_stories)):
    female_prediction = classifier(female_stories[i])
    male_prediction = classifier(male_stories[i])
    for pred in female_prediction[0]:
        category = pred["label"]
        score = round(pred["score"], 4)
        female_scores[category].append(score)
    for pred in male_prediction[0]:
        category = pred["label"]
        score = round(pred["score"], 4)
        male_scores[category].append(score)

with open("female_result.json", "w") as tf_f:
    json.dump(female_scores, tf_f)

with open("male_result.json", "w") as tf_m:
    json.dump(male_scores, tf_m)

print("Female sadness mean score: ", np.mean(female_scores["sadness"]))
print("Female joy mean score: ", np.mean(female_scores["joy"]))
print("Female love mean score: ", np.mean(female_scores["love"]))
print("Female anger mean score: ", np.mean(female_scores["anger"]))
print("Female fear mean score: ", np.mean(female_scores["fear"]))
print("Female surprise mean score: ", np.mean(female_scores["surprise"]))
print("Male sadness mean score: ", np.mean(male_scores["sadness"]))
print("Male joy mean score: ", np.mean(male_scores["joy"]))
print("Male love mean score: ", np.mean(male_scores["love"]))
print("Male anger mean score: ", np.mean(male_scores["anger"]))
print("Male fear mean score: ", np.mean(male_scores["fear"]))
print("Male surprise mean score: ", np.mean(male_scores["surprise"]))
