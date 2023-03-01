
import re
from collections import defaultdict
import ipdb
import sys
import os

f_name = sys.argv[1]

def replace_by_male_names(para):
    male_names = ["Bob", "Dave", "Frank"]
    init = 65
    for i in range(0, 3):
        word_ = "Protagonist" + chr(init + i)
        words_ = "Protagonist" + chr(init + i) + "'s"
        # ipdb.set_trace()
        new_para = para.replace(word_, male_names[i], 1)
        new_para = new_para.replace(words_, "her")
        new_para = new_para.replace(word_, "she")
        para = new_para
    return new_para    

def replace_by_female_names(para):
    female_names = ["Alice", "Carol", "Elva"]
    init = 65
    for i in range(0, 3):
        word_ = "Protagonist" + chr(init + i)
        words_ = "Protagonist" + chr(init + i) + "'s"
        # ipdb.set_trace()
        new_para = para.replace(word_, female_names[i], 1)
        new_para = new_para.replace(words_, "her")
        new_para = new_para.replace(word_, "she")
        para = new_para
    return new_para    

def process_male(inputf, outputf):
    f = open(inputf, "r")
    for para in f.readlines():
        new_para = replace_by_male_names(para)
        a = open(outputf, 'a')
        a.write(new_para)
    a.close()

def process_female(inputf, outputf):
    f = open(inputf, "r")
    for para in f.readlines():
        new_para = replace_by_female_names(para)
        a = open(outputf, 'a')
        a.write(new_para)
    a.close()


print("Male to female")
input_ = f_name + str("/male_masked.txt")
output_ = f_name + str("/result/m_to_f.txt")
process_female(input_, output_)

print("Female to female")
input_ = f_name + str("/female_masked.txt")
output_ = f_name + str("/result/f_to_f.txt")
process_female(input_, output_)

print("Male to male")
input_ = f_name + str("/male_masked.txt")
output_ = f_name + str("/result/m_to_m.txt")
process_male(input_, output_)

print("Female to male")
input_ = f_name + str("/male_masked.txt")
output_ = f_name + str("/result/f_to_m.txt")
process_male(input_, output_)


# para = "ProtagonistA was one of the most popular women of ProtagonistA's day ."
# new_para = replace_by_male_names(para)
# print(new_para)

# para = "This is a story about a man who must be kept from knowing , because it would kill ProtagonistA , that the man who killed ProtagonistB long before ProtagonistB , could be alive and always be looking for ProtagonistB . "
# new_para = replace_by_male_names(para)
# print(new_para)
