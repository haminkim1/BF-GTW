import random as rand
from nltk.corpus import wordnet

def random_username():
        adj_synsets = wordnet.all_synsets(pos='a')
        adj_lemmas = [lemma.name() for synset in adj_synsets for lemma in synset.lemmas()]
        noun_synsets = wordnet.all_synsets(pos='n')
        noun_lemmas = [lemma.name() for synset in noun_synsets for lemma in synset.lemmas()]
        return rand.choice(adj_lemmas) + rand.choice(noun_lemmas)