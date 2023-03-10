################################
# Here is the code to read files from folders conatining female or male stories
################################
import os, glob
female_folder = ["ancient_f_to_f/", "ancient_m_to_f/", 
                 "ponies_f_to_f/", "ponies_m_to_f/", 
                 "potter_f_to_f/", "potter_m_to_f/",
                 "victorian_f_to_f/", "victorian_m_to_f/"]
male_folder = ["ancient_f_to_m/", "ancient_m_to_m/", 
               "ponies_f_to_m/", "ponies_m_to_m/", 
               "potter_f_to_m/", "potter_m_to_m/",
               "victorian_f_to_m/", "victorian_m_to_m/"]

def read_stories(folder_list):
    stories = []
    for folder_path in folder_list:
        for filename in glob.glob(os.path.join(folder_path, '*.txt')):
            with open(filename, 'r') as f:
                text = f.read()
                # print(filename)
                stories.append(text)
    return stories

female_stories = read_stories(female_folder)
male_stories = read_stories(male_folder)

# print("Sanity Check: \n")
# print("Num of male stories: ", len(male_stories))
# print("Num of female stories: ", len(female_stories))
# print("Example male story: ", male_stories[0])
# print("Example female story: ", female_stories[0])


#############################
# Here is the code for emotion analysis
#############################
female_scores = {"sadness":[], "joy":[], "love":[], "anger":[], "fear":[], "surprise":[]}
male_scores = {"sadness":[], "joy":[], "love":[], "anger":[], "fear":[], "surprise":[]}

from transformers import pipeline
classifier = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True, truncation=True, max_length = 512)
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

# print("Sanity Check: \n")
# print("Num of male scores: ", len(male_scores["joy"]))
# print("Num of female scores: ", len(female_scores["anger"]))

import json
import numpy as np
tf_f = open("female_result.json", "w")
json.dump(female_scores, tf_f)
tf_f.close()
tf_m = open("male_result.json", "w")
json.dump(male_scores, tf_m)
tf_m.close()

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




