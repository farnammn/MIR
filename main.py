from __future__ import unicode_literals
from xml.dom import minidom
from hazm import *


negareshiMoreOne = ['==']
def read_xml(path):
    mydoc = minidom.parse(path)

    items = mydoc.getElementsByTagName('text')

    documents = []
    for i in range(len(items)):
        documents.append(items[i].firstChild.data)

    return documents

def preprocess(document):

    processed_doc = []
    normalizer = Normalizer()
    stemmer = Stemmer()
    for text in document:

        text_temp = normalizer.normalize(text)
        # print("NORMALIZED ", text_temp)
        text_temp = word_tokenize(text_temp)
        # print("TOKENIZED ", text_temp)

        text_noNegarshi = []
        for t in text_temp:
            if len(t) != 1 and not t in negareshiMoreOne:
                text_noNegarshi.append(t)

        # print("NO NEGARESHI ", text_noNegarshi)

        text_stemmed = []
        for t in text_noNegarshi:
            temp = stemmer.stem(t)
            text_stemmed.append(temp)

        # print("STEMMED ", text_stemmed)
        processed_doc.append(text_stemmed)
    return processed_doc



persian = read_xml('Persian.xml')
num_postings = len(persian)
persian = preprocess(persian)



print("sex")
gram = {}
# bigram = {}

for page_indx, page in enumerate(persian):
    for word_indx, word in enumerate(page):
        if not word in gram:
            gram[word] = [[] for _ in range(num_postings)]
        gram[word][page_indx].append(word_indx)

        if word_indx == len(page) - 1:
            continue
        next_word = page[word_indx + 1]
        biword = (word, next_word)

        # if not biword in bigram:
        #     bigram[biword] = []
        # bigram[biword].append(page_indx)

print(gram['فکر'])




