# AUTHOR: Thomas Bennett - trb090020
# COURSE: 4395.001 - UTD Spring 2023
# Chatbot Project

from bs4 import BeautifulSoup as BS
from urllib import request
from nltk.tokenize import sent_tokenize
import pickle


if __name__ == '__main__':
    links = []

    for i in range(1, 46):
        ep_num = i
        if ep_num < 10:
            ep_str = '0' + str(ep_num)
        else:
            ep_str = str(ep_num)
        ep_link = 'https://www.ibras.dk/montypython/episode' + ep_str + '.htm'
        links.append(ep_link)

    # get the text
    corpus = []
    for link in links:
        # request
        url = link
        html = request.urlopen(url)
        # make the soup
        soup = BS(html, features='html.parser')
        # get all the elements labeled by actor names
        elements = soup.find_all('font')
        episodes_text = ''
        episode_lines = []
        for element in elements:
            episodes_text += ' '.join(element.get_text().splitlines()) + ' '

        corpus.append(episodes_text)

    corpus_sentences = []
    for episode in corpus:
        corpus_sentences.append(sent_tokenize(episode, language='english'))

    # pickle the corpus
    with open('flying_circus_corpus.pickle', 'wb') as f:
        pickle.dump(corpus, f, pickle.HIGHEST_PROTOCOL)
    with open('flying_circus_sentences.pickle', 'wb') as f:
        pickle.dump(corpus_sentences, f, pickle.HIGHEST_PROTOCOL)
