import openai
import sys

openai.api_key = "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"

model_engine = "text-davinci-002"

file_name = sys.argv[1]
folder_name = sys.argv[2]


def generate_from_prompt_list(prompts, foldername):
    count = 85
    for prompt in prompts:
        converted_prompt = f"Write a story using '{prompt}' as the prompt."
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=converted_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        message = completions.choices[0].text
        filename = f"{foldername}/{count}.txt"
        with open(filename, 'w') as f:
            f.write(message)
        count += 1


def read_prompts_from_file(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    return lines


prompts = read_prompts_from_file(file_name)
generate_from_prompt_list(prompts[85:], folder_name)
