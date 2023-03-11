import os, glob
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
            with open(filename, 'r') as f:
                text = f.read()
                new_text = re.sub('\n', '', text)
                # ipdb.set_trace()
                stories.append(new_text)
    return stories

female_stories = read_stories(female_folder)
male_stories = read_stories(male_folder)

print("Num of male stories: ", len(male_stories))
print("Num of female stories: ", len(female_stories))
# Num of male stories:  1601
# Num of female stories:  1601

with open('result/male_stories.txt', 'w', encoding='utf-8') as f:
    for line in male_stories:
        f.write(line)
        f.write("\n")

with open('result/female_stories.txt', 'w', encoding='utf-8') as f:
    for line in female_stories:
        f.write(line)
        f.write("\n")

print("Example male story: ", male_stories[0])
print("Example female story: ", female_stories[0])