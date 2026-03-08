# Class 1: Sports & Athletics (Context: Winning/Medals)
doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"

# Class 2: Finance & Economy (Context: Market/Investment)
doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"

import numpy as np
from sklearn.cluster import KMeans
import re
import string
# Your Task: Fill these functions

def preprocess_text(text):
    """
    Make sure to lowercase and remove punctuation.
    """
    text=text.lower()
    text=re.sub(f"[{string.punctuation}]","",text)
    # Implement cleaning and tokenization
    tokens=text.split()
    return tokens
    pass

def vectorize(docs, n_gram_size=1):
    # Implement n-gram extraction and vectorization
    procesed_docs=[preprocess_text(doc)for doc in docs]
    ngrams=[]
    for tokens in procesed_docs :
        for i in range(len(tokens)-n_gram_size+1):
            gram=" ".join(tokens[i:i+n_gram_size])
            ngrams.append(gram)
    vocabulair=sorted(set(ngrams))
    vocabulair_ind={words:i for i,words in enumerate(vocabulair)}
    x=np.zeros((len(docs), len(vocabulair)))

    for doc ,tokens in enumerate(procesed_docs) :
        for i in range(len(tokens)-n_gram_size+1):
            gram= " ".join(tokens[i:i+n_gram_size])
            index=vocabulair_ind[gram]
            x[doc,index]=x[doc,index]+1
    return x

    pass

# Training / Clustering

all_docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]

# 1-gram Experiment
X1 = vectorize(all_docs, n_gram_size=1)
km1 = KMeans(n_clusters=2, random_state=42).fit(X1)

# 2-gram Experiment
X2 = vectorize(all_docs, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42).fit(X2)

print(f"1-gram clusters: {km1.labels_}")
print(f"2-gram clusters: {km2.labels_}")

# compare accuracy and precision