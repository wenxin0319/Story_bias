import os
import glob
import re

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
            with open(filename, 'r', encoding='utf-8') as f:
                text = f.read().replace('\n', '')
                stories.append(text)
    return stories

female_stories = read_stories(female_folder)
male_stories = read_stories(male_folder)

print("Number of male stories:", len(male_stories))
print("Number of female stories:", len(female_stories))

with open('result/male_stories.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(male_stories))

with open('result/female_stories.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(female_stories))

print("Example male story:", male_stories[0])
print("Example female story:", female_stories[0])
