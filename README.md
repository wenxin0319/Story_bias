# Story_bias

# dataset
### https://github.com/janelleshane/novel-first-lines-dataset
download it and store in the "dataset" folder

# step 1 split the stories into male and female group
## so in each folder we will have male.txt and female.txt
```
CUDA_VISIBLE_DEVICES=1 python Transfer.py dataset/ancient.txt dataset/ancient
CUDA_VISIBLE_DEVICES=1 python Transfer.py dataset/potter.txt dataset/potter
CUDA_VISIBLE_DEVICES=1 python Transfer.py dataset/ponies.txt dataset/ponies
CUDA_VISIBLE_DEVICES=1 python Transfer.py dataset/victorian.txt dataset/victorian
```

# step 2 Anonymization replace every character with the ProtagonistA,B,C...
## so in each folder we will have male_mask.txt and female_mask.txt
```
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/ancient
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/potter
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/ponies
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/victorian
```

# step3 replace protogonist with our signed character
### we replace each story for male and female version, male's name are "Bob", "Dave", "Frank", female's name are "Alice", "Carol", "Elva"
### so in each folder we will have f_to_m.txt, f_to_f.txt, m_to_m.txt, m_to_f.txt
```
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/ancient
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/potter
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/ponies
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/victorian
```

# step4 use gpt3 tools, and for each story, we only select the first sentence as prompt to generate story
### for the origin dataset, our generated stories, and standford-ner tools we use, we are store in the https://drive.google.com/file/d/1ULq2fAbgKjtRseRwDYzjDWNWsTwxYC_5/view?usp=sharing
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

# step5 combine the generated_stories, for male and female, we both for 1601 stories
```
python read_story.py
```

# step6 emotion_analysis
```
python emotion analysis.py
python stat_test.py
```