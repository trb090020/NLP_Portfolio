# AUTHOR: Thomas Bennett - trb090020
# COURSE: CS 4395.001 - UTD Spring 2023
# Chatbot Project

import pickle


if __name__ == '__main__':
    corpus_sentences = pickle.load(open('flying_circus_sentences.pickle', 'rb'))
    prev_next = {}

    for episode in corpus_sentences:
        for i, line in enumerate(episode):
            ep_length = len(episode)
            if i == 0:
                prev_next[str(line)] = {'this': line,
                                        'prev': None,
                                        'next': episode[i+1]}
            elif i >= ep_length - 1:
                prev_next[str(line)] = {'this': line,
                                        'prev': episode[i-1],
                                        'next': None}
            else:
                prev_next[str(line)] = {'this': line,
                                        'prev': episode[i-1],
                                        'next': episode[i+1]}

    with open('flying_circus_prev_next.pickle', 'wb') as f:
        pickle.dump(prev_next, f, pickle.HIGHEST_PROTOCOL)
