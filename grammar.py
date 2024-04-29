# Valeria Zúñiga Mendoza
# Context-fre grammar


# Test the grammar without left recursion
import nltk
nltk.download('punkt')
from nltk import CFG


# Catalan context-free grammar
grammar = CFG.fromstring("""
  E -> E2 | E3
  E2 -> S | S2 | VP 
  E3 -> NP VP Conj NP VP 
  S -> NP VP
  S2 -> NP VP NP  
  NP -> Det N | PropN | Pron | Det N Adj | Det N PP | PropN PP | Pron PP
  PP -> P NP
  VP -> V | V Adv | V PP

  Adj -> 'gran' | 'blau' | 'bonic' | 'veloc' | 'vermell'
  Adv -> 'ràpidament' | 'ben'
  V -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van' | 'menjen'
  Conj -> 'i' | 'o' | 'però' | 'sinó' | ','
  Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'
  N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' | 'nenes' | 'nens'
  P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'
  PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'
  Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' | 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'

""")

# Test the grammar with the provided sentences

# Sentences to test
sentences = [
    # Valid
    "Maria corre ràpidament",
    "ells ballant a Barcelona",
    "ell va a Catalunya",
    "ells ballant a Barcelona i ell va a Catalunya",
    # Invalid
    "ràpidament",
    "ella vive en Barcelona",
    "ells bailaaant na Barclona"
]

# Iterate over each sentence
for sentence in sentences:
    print("\nSentence:", sentence)
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    # Try parsing the sentence
    try:
        for tree in parser.parse(tokens):
            print("Valid grammar")
            tree.pretty_print()
    except ValueError:
        print("Not valid grammar")


