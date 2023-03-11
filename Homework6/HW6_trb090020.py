# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# ASSIGNMENT: 6 - Web Scraping

from bs4 import BeautifulSoup as BS
from urllib import request
import pprint
import re
import certifi
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import pickle
from nltk.stem import WordNetLemmatizer


# only keep urls - throw out wiki internal links
def is_match(match):
    if match is None:
        return None
    return True


def create_tf_dict(doc):
    tf_dict = {}
    tokens = word_tokenize(doc)
    tokens = [w.lower() for w in tokens if w.isalpha() and w.lower() not in stopwords]
    wnl = WordNetLemmatizer()
    for i, token in enumerate(tokens):
        tokens[i] = wnl.lemmatize(token)

    # get term frequencies
    for t in tokens:
        if t in tf_dict:
            tf_dict[t] += 1
        else:
            tf_dict[t] = 1

    # normalize tf by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)

    return tf_dict


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Texas_Rangers_(baseball)'
    html = request.urlopen(url, cafile=certifi.where()).read().decode('utf8')
    soup = BS(html, features='html.parser')
    refs = soup.find_all('span', class_='reference-text')
    ref_soup = BS(str(refs), features='html.parser')

    links = []
    for a in ref_soup.find_all('a'):
        links.append(a['href'])
    valid = re.compile(r'https://web.archive.org/*')

    good_links = []
    for link in links:
        if is_match(valid.match(link)):
            good_links.append(link)

    # use the top 20 links
    good_links = good_links[:20]

    # get the text from the 15 links
    for i, link in enumerate(good_links):
        text = ''
        # request
        url = link
        html = request.urlopen(url, cafile=certifi.where()).read().decode()
        # make the soup
        soup = BS(html, features='html.parser')
        # get the web page text
        text += soup.get_text()
        # clean up the text
        text = text.strip()
        text = text.replace('\n', ' ')
        # sent_tokenize the text
        sentences = sent_tokenize(text)
        # write the sentences to a file
        with open(f'page{i+1}.txt', 'w', encoding='utf-8') as f:
            for sentence in sentences:
                f.write(sentence)

    # get the 25 most important terms
    stopwords = stopwords.words('english')
    text = ''
    for i, link in enumerate(good_links):
        with open(f'page{i+1}.txt', 'r', encoding='utf-8') as f:
            sentences = f.read()

        for sentence in sentences:
            text += sentence

    # make a dictionary from the text
    tf_rangers = create_tf_dict(text)
    # print the top terms
    pprint.pprint(sorted(tf_rangers.items(), key=lambda x:x[1], reverse=True)[:40])

    # pickle the dict
    with open('rangers_history.pickle', 'wb') as f:
        pickle.dump(tf_rangers, f, pickle.HIGHEST_PROTOCOL)



