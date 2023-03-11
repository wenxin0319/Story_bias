import nltk
import spacy
from allennlp.predictors.predictor import Predictor
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


predictor = Predictor.from_path(
    "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz",
    cuda_device=0
)

nlp = spacy.load('en_core_web_lg')

male = []
female = []
unresolved = []


def write_file(file_name, content):
    with open(file_name, 'a') as f:
        f.write(content)


def get_pronouns(para):
    output = predictor.predict(
        document=para
    )

    for i in output['clusters']:
        for j in i:
            print(output['document'][j[0]:j[1] + 1])
        print('\n')

    return output['clusters']


def find_subject(li):
    root = ""
    for i in li:
        if i[1] == "ROOT":
            root = i[0]

    for i in li:
        if i[1] == "nsubj" and i[2] == root and (i[0] == "protagonistA" or i[0] == "ProtagonistA"):
            return True

    return False


def process(inputf, outputf):
    with open(inputf, "r") as f:
        for p in f.readlines():
            p = p.replace("!", ".")
            p = p.strip("\n").split(".")
            p = [i + "\n" for i in p if i != '']

            for para in p:
                if para == "\n" or para == ".\n":
                    continue

                tokens = nltk.word_tokenize(para)
                tagged_sent = nltk.pos_tag(tokens)
                doc = nlp(para)

                token_dependencies = [(token.text, token.dep_, token.head.text) for token in doc]

                flag = find_subject(token_dependencies)

                if flag:
                    write_file(outputf + '_subj.txt', para)
                else:
                    if len(para) > 5:
                        write_file(outputf + '_obj.txt', para)


process("result/male_masked.txt", "male_masked")
process("result/female_masked.txt", "female_masked")
