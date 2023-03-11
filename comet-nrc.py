import argparse
import csv
import math
import os
import pickle
import warnings
from collections import Counter, defaultdict
from pathlib import Path
import ipdb

import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
from pandas.core.common import SettingWithCopyWarning
from scipy.stats import zscore


def get_NRC_lexicon():
    """
    @output:
    - A dictionary of format {word : score}
    """
    lexicon = "NRC-VAD-Lexicon.txt"
    val_dict = {}
    aro_dict = {}
    dom_dict = {}

    with open(lexicon, "r") as infile:
        reader = csv.DictReader(infile, delimiter="\t")
        for row in reader:
            word = row["Word"]
            val_dict[word] = float(row["Valence"])
            aro_dict[word] = float(row["Arousal"])
            dom_dict[word] = float(row["Dominance"])
    return val_dict, aro_dict, dom_dict


def write_output(writer, df, label, title):
    df = df.copy()
    z = zscore(df["Value"])
    pt = "./comet/"

    if not os.path.exists(pt):
        Path(pt).mkdir()

    ptr = f"./comet/{title}_{label}.obj"
    if not os.path.isfile(ptr):
        Path(ptr).touch()

    filehandler = open(ptr, "wb")
    pickle.dump(z, filehandler)

    for i in range(df.shape[0]):
        df.loc[i, "value"] = z[i]

    df = df.drop(columns=["Value"])

    stats = df.groupby(["Category"]).agg(["mean", "median", "count", "std"])
    print(stats)
    cis = []
    for i in stats.index:
        mean, median, c, s = stats.loc[i]
        cis.append(1.96 * s / math.sqrt(c))

    stats["ci"] = cis
    for index, row in stats.iterrows():
        writer.writerow(
            {
                "category": row.name,
                "dimension": label,
                "median": row["value"]["median"],
                "mean": row["value"]["mean"],
                "ci": row["ci"].values[0],
            }
        )


def judge_category(file):
    if "at_dict" in file and "female" in file:
        return "female_at"
    if "at_dict" in file and "male" in file:
        return "male_at"

    if "xr_dict" in file  and "female" in file:
        return "female_xr"
    if "xr_dict" in file  and "male" in file:
        return "male_xr"

    if "obj.txt_or_dict" in file  and "female" in file:
        return "female_or_obj"
    if "obj.txt_or_dict" in file  and "male" in file:
        return "male_or_obj"
    
    if "subj.txt_or_dict" in file and "female" in file:
        return "female_or_subj"
    if "subj.txt_or_dict"  in file and "male" in file:
        return "male_or_subj"


def compute(inputt):
    adj = {"Category": [], "Measurement": [], "Value": [], "Word": []}
    val_dict, aro_dict, dom_dict = get_NRC_lexicon()
    print(inputt)

    with open(inputt, "rb") as file:
        tups = pickle.load(file)

    words = []
    for i in tups:
        words += set(i)

    words = list(filter(lambda a: a != "none", words))

    # category = "male" if input[0] == "m" else "female"
    category = judge_category(inputt)

    c = Counter(words)
    removed = c.most_common(5)
    removed = [i[0] for i in removed]
    print(removed)

    for word in words:
        if word in removed:
            continue
        if word in val_dict:
            val = val_dict[word]
            aro = aro_dict[word]
            dom = dom_dict[word]
            adj["Category"].append(category)
            adj["Measurement"].append("Valence")
            adj["Value"].append(val)
            adj["Word"].append(word)

            adj["Category"].append(category)
            adj["Measurement"].append("Arousal")
            adj["Value"].append(aro)
            adj["Word"].append(word)

            adj['Category'].append(category)
            adj['Measurement'].append('Dominance')
            adj['Value'].append(dom)
            adj['Word'].append(word)

    adj_df = pd.DataFrame.from_dict(adj)
    # ipdb.set_trace()
    val_df = adj_df[adj_df['Measurement'] == 'Valence']
    aro_df = adj_df[adj_df['Measurement'] == 'Arousal']
    dom_df = adj_df[adj_df['Measurement'] == 'Dominance']

    with open('comet_median.csv', 'a') as outfile:
        fieldnames = ['category', 'dimension', 'median','mean', 'ci']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        write_output(writer, val_df, 'valence',category)
        write_output(writer, aro_df, 'arousal',category)
        write_output(writer, dom_df, 'dominance',category)

if not os.path.exists('./comet_remove'):
    os.mkdir('./comet_remove')
if not os.path.isfile("./comet_remove/aba.obj"):
    Path("./comet_remove/aba.obj").touch()

with open("./comet_remove/aba.obj", "wb") as filehandler:
    pickle.dump("1", filehandler)

for filename in ["./result/male_masked_subj.txt_at_dict", "./result/female_masked_subj.txt_at_dict",
                 "./result/male_masked_subj.txt_xr_dict", "./result/female_masked_subj.txt_xr_dict",
                 "./result/male_two_and_above_obj.txt_or_dict", "./result/female_two_and_above_obj.txt_or_dict",
                 "./result/male_two_and_above_subj.txt_or_dict", "./result/female_two_and_above_subj.txt_or_dict"]:
    compute(filename)