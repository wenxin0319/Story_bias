import re
from collections import defaultdict


def replace_names(para, names, pronoun):
    """
    Replaces the names and pronouns in the given paragraph
    with the given names and pronouns.

    Args:
    para (str): The paragraph to replace names and pronouns in.
    names (list): The list of names to replace with.
    pronoun (str): The pronoun to replace with.

    Returns:
    str: The paragraph with the names and pronouns replaced.
    """
    init = 65
    for i, name in enumerate(names):
        word_ = f"Protagonist{chr(init + i)}"
        words_ = f"Protagonist{chr(init + i)}'s"
        para = para.replace(word_, name)
        para = para.replace(words_, f"{pronoun}s")
        para = para.replace(word_, pronoun)
    return para

def process_names(inputf, outputf, names, pronoun):
    """
    Processes the given input file by replacing names and pronouns in the paragraphs
    with the given names and pronouns, and writes the result to the output file.

    Args:
    inputf (str): The path to the input file.
    outputf (str): The path to the output file.
    names (list): The list of names to replace with.
    pronoun (str): The pronoun to replace with.
    """
    with open(inputf, "r") as f, open(outputf, 'a') as a:
        for para in f:
            new_para = replace_names(para, names, pronoun)
            a.write(new_para)

input_dir = input("Enter the directory containing input files: ")

# Male to female
input_file = f"{input_dir}/male_masked.txt"
output_file = f"{input_dir}/result/m_to_f.txt"
names = ["Alice", "Carol", "Elva"]
pronoun = "she"
process_names(input_file, output_file, names, pronoun)

# Female to female
input_file = f"{input_dir}/female_masked.txt"
output_file = f"{input_dir}/result/f_to_f.txt"
names = ["Alice", "Carol", "Elva"]
pronoun = "she"
process_names(input_file, output_file, names, pronoun)

# Male to male
input_file = f"{input_dir}/male_masked.txt"
output_file = f"{input_dir}/result/m_to_m.txt"
names = ["Bob", "Dave", "Frank"]
pronoun = "he"
process_names(input_file, output_file, names, pronoun)

# Female to male
input_file = f"{input_dir}/female_masked.txt"
output_file = f"{input_dir}/result/f_to_m.txt"
names = ["Bob", "Dave", "Frank"]
pronoun = "he"
process_names(input_file, output_file, names, pronoun)

print("Done")
