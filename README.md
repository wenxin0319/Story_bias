# Story_bias

# step 1
```
CUDA_VISIBLE_DEVICES=1 python Transfer1.py dataset/reddit_short_stories.txt dataset/reddit
```
# step 2
```
CUDA_VISIBLE_DEVICES=1 python replacegender.py dataset/ancient
```
# step3 replace protogonist
```
CUDA_VISIBLE_DEVICES=1 python replacepron.py dataset/ancient
