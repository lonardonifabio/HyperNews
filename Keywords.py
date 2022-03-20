#!C:\Users\lonar\AppData\Local\Programs\Python\Python39\python.exe
import sys
#from transformers import pipeline
#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#print(summarizer(sys.argv[1], max_length=30, min_length=10, do_sample=False))
from newspaper import Article
import nltk
#nltk.download("punkt")
url = sys.argv[1]
article = Article(url)
article.download()
article.parse()
article.nlp()
print(article.keywords)