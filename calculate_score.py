import pandas as pd
import numpy as np
import gensim
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from empath import Empath
from scipy import stats
import pickle
from scipy import spatial
from collections import Counter
import os
from pathlib import Path
import ipdb

df = pd.read_csv('Lexicons of bias - Gender stereotypes.csv')
model = KeyedVectors.load_word2vec_format('../GoogleNews-vectors-negative300.bin.gz', binary=True)
lexicon = Empath()

intellect = [
    "intellectual", "intuitive", "imaginative", "knowledgeable", "ambitious", 
    "intelligent", "opinionated", "admirable", "eccentric", "crude", "likable", 
    "empathetic", "superficial", "tolerant", "resourceful", "uneducated", "academically", 
    "studious", "temperamental", "exceptional", "cynical", "outspoken", "destructive", 
    "dependable", "amiable", "impulsive", "frivolous", "insightful", "overconfident", 
    "charismatic", "prideful", "influential", "likeable", "unconventional", "educated", 
    "flawed", "articulate", "pretentious", "perceptive", "vulgar", "easygoing", "listener", 
    "skillful", "assertive", "philosophical", "rebellious", "selfless", "cunning", "deceptive", 
    "artistic", "appalling", "overbearing", "temperament", "diligent", "charitable", "disposition", 
    "quirky", "strategic", "compulsive", "benevolent", "pessimistic", "scientific", "flamboyant", 
    "obsessive", "selective", "oriented", "humorous", "narcissistic", "reliable", "headstrong", 
    "manipulative", "practical", "rewarding", "refined", "resilient", "desirable", "spiritual", 
    "tendencies", "pompous", "judgmental", "respected", "inexperienced", "compassionate", "promiscuous", 
    "argumentative", "conventional", "intellectually", "expressive", "impractical", "observant", "fickle", 
    "hyperactive", "immoral", "straightforward", "vindictive"
]

def get_words(cates):
    tmp = df.loc[:,cates].values
    words = set()
    for i in tmp:
        for j in i:
            if(type(j) is not float):
                words.add(j)
    return words

appearance = ["beautiful", "sexual"]
appear = get_words(appearance)
power = ["dominant", "strong"]
power = get_words(power)
weak = ['submissive', 'weak', 'dependent', 'afraid']
weak = get_words(weak)

print("loaded")

file_list = [
    "male_masked_subj.txt_at_dict", 
    "female_masked_subj.txt_at_dict", 
    "male_masked_subj.txt_xr_dict", 
    "female_masked_subj.txt_xr_dict", 
    "male_two_and_above_obj.txt_or_dict", 
    "female_two_and_above_obj.txt_or_dict", 
    "male_two_and_above_subj.txt_or_dict", 
    "female_two_and_above_subj.txt_or_dict"
]

def load_file(file_path):
    with open(file_path, 'rb') as f:
        words = pickle.load(f)
    return words

def calculateSubspace(A, B, model):
    A_vecs = [model.wv[i] for i in A if i in model]
    B_vecs = [model.wv[i] for i in B if i in model]

    suma = A_vecs[0].copy()
    for i in range(1, len(A_vecs)):
        suma += A_vecs[i]

    sumb = B_vecs[0].copy()
    for i in range(1, len(B_vecs)):
        sumb += B_vecs[i]

    return suma / len(A) - sumb / len(B)

def compute(words_clusters, title, model):
    intel_sum = []
    appear_sum = []
    power_sum = []

    power_subspace = calculateSubspace(power, weak, model)

    for x in words_clusters:
        if x not in model:
            continue

        # calculate similarity
        intel_sims = 0
        appear_sims = 0
        for j in intellect:
            if j in model:
                intel_sims += model.similarity(x, j)
        for k in appear:
            if k in model:
                appear_sims += model.similarity(x, k)

        power_sum.append(1 - spatial.distance.cosine(model.wv[x], power_subspace))
        intel_sum.append(intel_sims / len(intellect))
        appear_sum.append(appear_sims / len(appear))

    print("Dumping results")


    # Create directory if it does not exist
    if not os.path.exists(title):
        os.makedirs(title)

    # Save variables to files
    file_names = [
        (title + "_intellect.pkl", intel_sum),
        (title + "_appear.pkl", appear_sum),
        (title + "_power.pkl", power_sum)
    ]

    for file_name, variable in file_names:
        if not os.path.isfile(file_name):
            Path(file_name).touch()

        with open(file_name, "wb") as f:
            pickle.dump(variable, f)

        return [np.median(stats.zscore(intel_sum)), 
                np.median(stats.zscore(appear_sum)), 
                np.median(stats.zscore(power_sum))]


def get_stats(lst):
    return np.max(lst), np.min(lst), np.percentile(lst, 25), np.percentile(lst, 75), np.median(lst)

def get_lexicon_score(file1, file2):
    male_words = load_file(file1)
    female_words = load_file(file2)

    if type(female_words[0]) is list:
        male_words = [i[0] for i in male_words]
        female_words = [i[0] for i in female_words]

    if type(female_words[0]) is tuple:
        male_words = [i[1] for i in male_words]
        female_words = [i[1] for i in female_words]

    male_removed = [i[0] for i in Counter(male_words).most_common(5)]
    female_removed = [i[0] for i in Counter(female_words).most_common(5)]

    m = [word for word in male_words if word not in male_removed]
    f = [word for word in female_words if word not in female_removed]

    if "curious" in m:
        print("Incorrect word found in male words.")
    else:
        print("All good!")

    m = list(filter(lambda a: a != "none", m))
    f = list(filter(lambda a: a != "none", f))
    ipdb.set_trace()

    return get_stats(m), get_stats(f)

# def get_lexicon_score_b5(f1, f2):
#     male = load_file(f1)
#     female = load_file(f2)

#     mm = set([word for line in male for word in line if word != 'none'])
#     ff = set([word for line in female for word in line if word != 'none'])

#     m = list(mm)
#     f = list(ff)

#     m_score = compute(m, f"../0515replotting/{f1.split('/')[-2]}/{f1.split('/')[-1].split('.')[0]}")
#     f_score = compute(f, f"../0515replotting/{f2.split('/')[-2]}/{f2.split('/')[-1].split('.')[0]}")

#     return m_score, f_score


directs = ["./result/"]
result = []

for direct in directs:
    result.append(get_lexicon_score(f"{direct}male_masked_subj.txt_at_dict", f"{direct}female_masked_subj.txt_at_dict"))

print(result)
