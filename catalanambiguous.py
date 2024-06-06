# -*- coding: utf-8 -*-
"""CatalanAmbiguous.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZFGeFtPMJD-o7N5yyRCJoIGnKDu_psA6
"""

import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Catalan context-free grammar
grammar = CFG.fromstring("""
  E -> S V |  E Conj E
  S -> Det S | Pron | N | PropN | S AdjQual | S Conj S
  Det -> Art | Art AdjPos | AdjC
  V -> V | V AdjQual | V Adv | V PP | V Conj V
  PP -> Prep S | PP PP

  V -> 'és' | 'cuina' | 'són' | 'corre' | 'visitan' | 'va' | 'van' | 'viu' | 'treballa' | 'criden' | 'ploren' | 'estan'
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

# Sentences to test
sentences = [
    # Valid
    "la casa és verda",
    "ella corre ràpid",
    "Albert cuina bé i cuina ràpid",
    "aquelles noies visitan a la escola",
    "la Montse treballa",

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
    tokens = word_tokenize(sentence)
    # Try parsing the sentence
    try:
        parse_trees = list(parser.parse(tokens))
        if parse_trees:
            print("Valid grammar")
            for tree in parse_trees:
                tree.pretty_print()
        else:
            print("Not valid grammar")
    except ValueError as error:
        print("Not valid grammar")
        print(error)