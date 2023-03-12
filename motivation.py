import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import defaultdict

# Define a function to extract the protagonist's motivations based on their gender
def extract_motivations(text):
    sentences = nltk.sent_tokenize(text)
    sid = SentimentIntensityAnalyzer()
    male_motivations = []
    female_motivations = []
    
    for sentence in sentences:
        sentence_list = sentence.lower().split()
        if 'she' in sentence_list or 'her' in sentence_list:
            sentiment = sid.polarity_scores(sentence)['compound']
            if sentiment > 0:
                tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)))
                phrases = []
                for subtree in tree.subtrees():
                    for sub in subtree:
                        if len(sub) >= 2:
                            if sub[1] == 'NN':
                                phrases.append(sub[0])
                female_motivations.extend(phrases)

        elif 'he' in sentence_list or 'him' in sentence_list:
            sentiment = sid.polarity_scores(sentence)['compound']
            if sentiment > 0:
                tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)))
                phrases = []
                for subtree in tree.subtrees():
                    for sub in subtree:
                        if len(sub) >= 2:
                            if sub[1] == 'NN':
                                phrases.append(sub[0])
                male_motivations.extend(phrases)

    return male_motivations,female_motivations

def convert_to_dict(my_list):
    my_dict = defaultdict(int)
    for item in my_list:
        my_dict[item] += 1
    return my_dict

def analysis_motivation(filename):
    male_motivations = []
    female_motivations = []

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        male_,female_ = extract_motivations(text)
        male_motivations += male_
        female_motivations += female_

    print(filename)
    dict_male = convert_to_dict(male_motivations)
    male_list = sorted(dict_male.items(), key=lambda x: x[1], reverse=True)

    dict_female = convert_to_dict(female_motivations)
    female_list = sorted(dict_female.items(), key=lambda x: x[1], reverse=True)

    # print(male_list)
    # print(female_list)
    return male_list, female_list


males, females = analysis_motivation("./results/male_stories.txt")
maless, femaless = analysis_motivation("./results/female_stories.txt")
common_words = []
for word1, count1 in males:
    for word2, count2 in femaless:
        if word1 == word2:
            common_words.append((word1, count1, count2))
print(common_words)