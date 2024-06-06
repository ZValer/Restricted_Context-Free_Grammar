# -*- coding: utf-8 -*-
"""CatalanNOLeftRecursion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n-aFM1E9AETQpezNtEoQ5MkyGFUd27ZV
"""

import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser

nltk.download('punkt')

# Catalan context-free grammar
grammar = CFG.fromstring("""
  E ->  E2 Eapos | E2
  Eapos -> Conj E2 Eapos | Conj E2
  E2 -> S V
  S -> S2 Sapos | S2
  Sapos -> Conj S2 Sapos | Conj S2
  S2 -> S3 AdjQual | S3
  S3 -> Det S4 | S4
  S4 -> Pron | N | PropN
  Det -> Art | Art Det2 | AdjC
  Det2 -> AdjPos | AdjC
  V -> V2 Vapos | V2
  Vapos -> Conj V2 Vapos | Conj V2
  V2 -> V3 AdjQual | V3 Adv | V3 PP | V3 AdjQual | V3
  PP -> Prep S PPapos |  Prep S
  PPapos -> Prep S PPapos | Prep S

  V3 -> 'és' | 'cuina' | 'són' | 'corre' | 'visitan' | 'va' | 'van' | 'viu' | 'treballa' | 'criden' | 'ploren' | 'estan'
  Art -> 'la' | 'les' | 'el' | 'els' | 'un' | 'una' | 'uns' | 'unes'
  AdjPos -> 'seva' | 'seus' | 'mi' | 'teu' | 'teves' | 'seves' | 'seu' | 'nostres'
  AdjQual -> 'verda' |  'vermella' | 'vermelles' | 'tristos' | 'nova' | 'alts' | 'baixos' | 'blaves' | 'petites'
  AdjC -> 'aquelles' | 'aquest' | 'dues' | 'cinc' | 'mil' | 'alguns' | 'molts' | 'tots'
  Adv -> 'ràpid' | 'bé' |'ràpidament' | 'ben'
  Prep -> 'a' | 'amb' | 'contra' | 'de' | 'des' | 'en'
  Pron -> 'ella' | 'jo' | 'tu' | 'ell' | 'nosaltres' | 'vós' | 'ells' | 'elles'
  N ->  'casa' | 'bicicleta' | 'pilotes' | 'noies' | 'escola' | 'taxi' | 'ciutat' | 'germana' | 'nens' | 'avió' | 'pares'
  PropN -> 'Xavi' | 'Albert' | 'Montse' | 'Eva' | 'Venècia' | 'València' | 'Mèxic'
  Conj -> 'i' | 'o' | 'ni' | 'perquè' | 'però' | ',' | 'sinó'

""")


# Create a parser
parser = ChartParser(grammar)

# Test the grammar with the provided sentences

# Sentences to test
sentences = [
    # Valid
    "la casa és verda",
    "les cinc pilotes vermelles i les dues pilotes blaves són petites",
    "ella corre ràpid",
    "Albert cuina bé i cuina ràpid",
    "aquelles noies visitan a la escola",
    "el taxi va a la ciutat",
    "ella viu a València amb la seva germana",
    "la Montse treballa",
    "Eva i Albert són alts però la Montse i Albert són baixos",
    "alguns nens criden i ploren perquè estan tristos",
    "Xavi , Montse i Albert van a Venècia amb avió amb els seus pares",

    # Invalid
    "ràpidament",
    "ella vive en Barcelona",
    "this sentence is in English",
    "corre verda ella les"
    "scjv ddkd ddd cf"
]

# Iterate over each sentence
for sentence in sentences:
    print("\nSentence:", sentence)
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    # Try parsing the sentence
    try:
        parse_trees = list(parser.parse(tokens))
        if parse_trees:
            print("Valid grammar")
            for tree in parse_trees:
                tree.pretty_print()
        else:
            print("Not valid grammar")
    except ValueError:
        print("Not valid grammar")