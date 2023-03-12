# Story_bias

# dataset
The dataset used in this project can be found at: https://github.com/janelleshane/novel-first-lines-dataset

To use this dataset, download it and store it in the "dataset" folde

# standford-ner
The Stanford NER software used in this project can be found at: https://nlp.stanford.edu/software/stanford-ner-4.2.0.zip

To use this software, download it, unzip it and change its name to the "stanford-ner" folder.

# GoogleNews-vectors-negative300.bin.gz 
The GoogleNews-vectors-negative300.bin.gz  used in this project can be found at: https://drive.google.com/open?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&authuser=0

To use this software, download it, move it outside this folder.

# step 1 split the stories into male and female group
To split the stories into male and female groups, run the following commands:

```
CUDA_VISIBLE_DEVICES=1 python transfer.py dataset/ancient.txt dataset/ancient
CUDA_VISIBLE_DEVICES=1 python transfer.py dataset/potter.txt dataset/potter
CUDA_VISIBLE_DEVICES=1 python transfer.py dataset/ponies.txt dataset/ponies
CUDA_VISIBLE_DEVICES=1 python transfer.py dataset/victorian.txt dataset/victorian
```
This will create a "male.txt" and "female.txt" file in each of the four subfolders.

# step 2 Anonymization
To anonymize the stories, replace every character with the ProtagonistA, ProtagonistB, ProtagonistC, etc.

To do this, run the following commands:

```
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/ancient
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/potter
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/ponies
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/victorian
```
This will create a "male_mask.txt" and "female_mask.txt" file in each of the four subfolders.

# step3 Replace protagonists with signed characters
To replace each story for male and female versions, use "Bob", "Dave", and "Frank" for male names and "Alice", "Carol", and "Elva" for female names.

To do this, run the following commands:

```
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/ancient
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/potter
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/ponies
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/victorian
```
This will create "f_to_m.txt", "f_to_f.txt", "m_to_m.txt", and "m_to_f.txt" files in each of the four subfolders.

# step4 Use GPT-3 tools to generate stories

To generate stories, use GPT-3 tools to select only the first sentence of each story as the prompt.

To do this, run the following commands:

```
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ancient/result/f_to_m.txt generated_stories/ancient_f_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ancient/result/f_to_f.txt generated_stories/ancient_f_to_f
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ancient/result/m_to_m.txt generated_stories/ancient_m_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ancient/result/m_to_f.txt generated_stories/ancient_m_to_f
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/potter/result/f_to_m.txt generated_stories/potter_f_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/potter/result/f_to_f.txt generated_stories/potter_f_to_f
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/potter/result/m_to_m.txt generated_stories/potter_m_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/potter/result/m_to_f.txt generated_stories/potter_m_to_f
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ponies/result/f_to_m.txt generated_stories/ponies_f_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ponies/result/f_to_f.txt generated_stories/ponies_f_to_f
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ponies/result/m_to_m.txt generated_stories/ponies_m_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/ponies/result/m_to_f.txt generated_stories/ponies_m_to_f
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/victorian/result/f_to_m.txt generated_stories/victorian_f_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/victorian/result/f_to_f.txt generated_stories/victorian_f_to_f
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/victorian/result/m_to_m.txt generated_stories/victorian_m_to_m
CUDA_VISIBLE_DEVICES=1 python generation.py dataset/victorian/result/m_to_f.txt generated_stories/victorian_m_to_f
```
For the original dataset, our generated stories, and the Stanford NER tools we used, please check https://drive.google.com/file/d/1ULq2fAbgKjtRseRwDYzjDWNWsTwxYC_5/view?usp=sharing. 

# step5 Combine the Generated Stories
Combine the generated stories for male and female into one file containing 1601 stories.

To run the script, execute the following command in the terminal:

```
python read_story.py
```

# step6 Emotion Analysis
Perform emotion analysis on the combined stories.

To run the emotion analysis script, execute the following command in the terminal:

```
python emotion analysis.py
```

After running the emotion analysis, run the statistical test script by executing the following command in the terminal:

```
python stat_test.py
```
# step7 to step11 are analysis implicit gender bias
# step7 Extract Stories with More Than Two Characters
In this step, we extracted stories that have more than two characters. This was done to check the effect of the subject and object in the story. To run the script for this step, use the following command:

```
python extract_two.py 
```

# step8 Classify sentences according to protagonist
In this step, sentences were classified according to the protagonist. To run the script for this step, use the following command:
```
python find_subject.py 
```

# step9 Get COMeT outputs
In this step, we obtained COMeT outputs. To run the script for this step, use the following command
```
python generate_inference.py
```

# step10 Calculate Valence, arousal scores 
In this step, valence and arousal scores were calculated. To run the script for this step, use the following command:
```
python comet-nrc.py
```
After calculating Valence, arousal scores, run the statistical test script by executing the following command in the terminal:

```
python plot_results.py
```
# step11 Calculate Intellect, Appearance, Power scores
In this step, intellect, appearance, and power scores were calculated. To run the script for this step, use the following command, store in pics folder
```
python calculate_score.py
```
<<<<<<< HEAD
After calculating Intellect, Appearance, Power scores, run the statistical test script by executing the following command, store in pics2 folder
=======
After calculating Intellect, Appearance, Power scores, run the statistical test script by executing the following command in the terminal:
>>>>>>> 885cf4d40d1af5edc455aa3ad6aac444ec8338f9

```
python plot_result_intel.py
```
Acknowledgement:
      
We borrowed some code from this repository: https://github.com/tenghaohuang/Uncover_implicit_bias
