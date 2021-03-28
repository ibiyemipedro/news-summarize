import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://edition.cnn.com/travel/article/seychelles-reopens-to-travelers/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publish Date: {article.publish_date}')
print(f'Summary: {article.summary}')

sentimentAnalysis = TextBlob(article.text);
print(f'News Polarity: {sentimentAnalysis.polarity }')

print(f'Analysis : { "positive" if sentimentAnalysis.polarity > 0 else "negative"  if sentimentAnalysis.polarity < 0 else "neutral"}')


# root = tk.Tk()
# root.title("News Summarizer")
# root.geometry('1200x600')

# root.mainloop()