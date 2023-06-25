import imp
import pandas as pd
import numpy as np
import csv

from main import liked_article
all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_article = []
not_liked_article = []