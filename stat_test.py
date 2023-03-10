import json
import scipy.stats as stats
import numpy as np

tf_f = open("female_result.json", "r")
female_dict = json.load(tf_f)
tf_m = open("male_result.json", "r")
male_dict = json.load(tf_m)

sadness_female = female_dict["sadness"]
sadness_male = male_dict["sadness"]
joy_female = female_dict["joy"]
joy_male = male_dict["joy"]
love_female = female_dict["love"]
love_male = male_dict["love"]
anger_female = female_dict["anger"]
anger_male = male_dict["anger"]
fear_female = female_dict["fear"]
fear_male = male_dict["fear"]
surprise_female = female_dict["surprise"]
surprise_male = male_dict["surprise"]

sadness_result = stats.ttest_rel(a=np.array(sadness_female), b=np.array(sadness_male))
print(sadness_result)
joy_result = stats.ttest_rel(a=np.array(joy_female), b=np.array(joy_male))
print(joy_result)
love_result = stats.ttest_rel(a=np.array(love_female), b=np.array(love_male))
print(love_result)
anger_result = stats.ttest_rel(a=np.array(anger_female), b=np.array(anger_male))
print(anger_result)
fear_result = stats.ttest_rel(a=np.array(fear_female), b=np.array(fear_male))
print(fear_result)
surprise_result = stats.ttest_rel(a=np.array(surprise_female), b=np.array(surprise_male))
print(surprise_result)

import matplotlib
import matplotlib.pyplot as plt

labels = ['Sadness', 'Joy', 'Love', 'Anger', 'Fear','Surprise'] # 级别
men_means = [np.mean(sadness_male), np.mean(joy_male), np.mean(love_male), np.mean(anger_male), np.mean(fear_male), np.mean(surprise_male)]
women_means = [np.mean(sadness_female), np.mean(joy_female), np.mean(love_female), np.mean(anger_female), np.mean(fear_female), np.mean(surprise_female)]

x = np.arange(len(men_means))

plt.figure(figsize=(9,6))
width = 0.4

rects1 = plt.bar(x - width/2, men_means, width, color = "#6495ED") # 返回绘图区域对象
rects2 = plt.bar(x + width/2, women_means, width, color = "#8FBC8F")

# 设置标签标题，图例
plt.ylabel('Average Scores')
plt.title('Emotion Scores by Gender')
plt.xticks(x,labels)
plt.legend(['Men','Women'])

# 添加注释
def set_label(rects):
    for rect in rects:
        height = rect.get_height() # 获取⾼度
        plt.text(x = rect.get_x() + rect.get_width()/2, # ⽔平坐标
                 y = height + 0.5, # 竖直坐标
                 s = height, # ⽂本
                 ha = 'center') # ⽔平居中

#set_label(rects1)
#set_label(rects2)

plt.tight_layout() # 设置紧凑布局
plt.savefig('./emotion_bar_plot.png')
