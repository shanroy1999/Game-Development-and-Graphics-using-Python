import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image
currdir = os.path.dirname(__file__)

df = pd.read_csv("7817_1.csv")
print(df.shape)
print(df.head())

stopwords = set(STOPWORDS) #creating a set of stopwords and storing it in variable 'stopwords'
def mywc(data, title=None):
    mask = np.array(Image.open(os.path.join(currdir, "cloud.png")))
    wc = WordCloud(background_color='White', mask=mask,stopwords=stopwords,max_words=200,max_font_size=40,scale=3,random_state=1)
    wc.generate(str(data))

    fig = plt.figure(1, figsize=(20,20))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wc)
    plt.show()
    wc.to_file(os.path.join(currdir, "Amazon WC.png"))

mywc(df["reviews.text"])
