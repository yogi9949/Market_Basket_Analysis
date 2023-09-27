import pandas as pd
import numpy as np

#for viz
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

#to avoid warning
import warnings
warnings.filterwarnings('ignore')

#to display all feature if the number increase
pd.set_option('display.max_columns', None)
#importing Dataset

data=pd.read_excel('/kaggle/input/market-basket-analysis/Assignment-1_Data.xlsx')
data.head()
data.tail()
data.info()
data.shape
data.describe()
data[data['Quantity']<0]
from wordcloud import WordCloud, STOPWORDS
stopwords = STOPWORDS
worldcloud= WordCloud(background_color='Black',stopwords=stopwords, height=1000, width =2000)

temp=data[data['Quantity']<0]
body =temp['Itemname'].to_string(index=False)
### Generate word cloud
worldcloud.generate(body)
## Visualize
plt.figure(figsize=(22,10))
plt.imshow(worldcloud)
plt.axis("off")
#next we can see for price small or equal to 0
temp=data[data['Price']<=0]
body =temp['Itemname'].dropna().to_string(index=False)
### Generate word cloud
worldcloud.generate(body)
## Visualize
plt.figure(figsize=(22,10))
plt.imshow(worldcloud)
plt.axis("off")
# check for duplicate entries 
data.duplicated().sum()
# there are 5286 duplicates transcations are present in the dataset Lets remove them
data.drop_duplicates(inplace=True)
#Let remove the space in that word
data['Itemname'] = data['Itemname'].str.strip()
#Lets Check for null Values
data.isnull().sum()
data.isnull().mean()*100
sns.heatmap(data.isnull())
data['Date']


