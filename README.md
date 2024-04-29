# Restricted_Context-Free_Grammar
E2 Generating and Cleaning a Restricted Context Free Grammar

## Catalan 

### Description:
Catalan, despite being mostly spoken in Spain, shares a lot of similarities with French. Its vocabulary  “has more in common with Occitan of southern France than with Spanish. It shares about 70 % of its lexicon with the first and about  20% with the second” (Gutman & Avanzati, 2013).


After the loss of Catalonia's independence to the Crown of Castile, Catalan culture was affected by new laws that promoted the use of Spanish. However, in the early 19th century, several artists, authors and playwrights helped revive the language. Although until 1975 its use was prohibited and it was prohibited to give Catalan names to newborns, as well as street names, in music, television and cinema, it was even prohibited to speak Catalan in public. Currently, Catalan is the official language in Andorra and co-official in Valencia, Catalonia and the Balearic Islands (Translinguo Global, 2022).


#### Language basics:

1. Gender and nouns: they are divided into masculine or feminine, which influences their use with articles and adjectives, '-a' for feminine, while those ending in '-o' are masculine.
2. Articles: there are definite articles (el, la, els, les) and indefinite articles (un, una, uns, unes), which agree in gender and number with the noun.
3. Adjectives: Adjectives differentiate between masculine and feminine. And to form the plural, "-os" (masculine) and "-es" (feminine) are added.
4. Verbs and Conjugation: Verbs in Catalan are classified into three groups based on their endings: “-ar,” “-er,” and “-ir.” Each group has its own conjugation pattern. Catalan also has auxiliary verbs (like ‘to have’ and ‘to be’) that combine with other verbs to create compound tenses and passive voice.
*We won´t consider compund sentences in the analysis. 
5. Pronouns and Prepositions: Catalan has subject pronouns (jo, tu, ell, ella, etc.) and object pronouns  (com "a", "de", "en", "amb") , which can undergo different changes depending on their function within a sentence. Additionally, Catalan prepositions (such as “a,” “de,” “en,” “amb”) help you connect words and phrases and show relationships between them.
(TalkPal, 2024)


#### Syntax

The basic word order in Catalan is Subject-Verb-Object, but it is quite flexible. Subject pronouns may be dropped. Some sentences have no subject at all (impersonal). For  syntactical relations Catalan uses prepositions. Attributive adjectives most often follow their noun (Gutman & Avanzati, 2013).

#### Common Simple Sentence Patterns in Catalan
In addition to the basic SVO structure, a few common sentence patterns are the following:
1. Subject + Verb + Adjective: La casa és verda. (The house is green)
2. Subject + Verb + Adverb: Ell camina ràpid. (He walks fast)
3. Subject + Verb + Prepositional Phrase: Ella viu a Girona. (She lives in Girona)
4. Verb + Object + Adjective: Joan troba interessant el llibre. (Joan finds the book interesting)
5. Reflexive Verb Sentences: Em rento les mans. (I wash my hands)
6. Negative sentences: No vull cafè. (I don’t want coffee)
(TalkPal, 2024)

*The analysis will include sentences patters 2, 3 plus the use of conjunctions.




##### References:

Gutman, A. & Avanzati, B. (2013). Catalan. The Language Gulper. Retrieved from:
https://www.languagesgulper.com/eng/Catalan.html#:~:text=The%20basic%20word%20order%20in,subject%20at%20all%20(impersonal).

TalkPal. (2024). Understanding Simple Sentences in Catalan Grammar. TalkPal AI. Retrieved from: https://talkpal.ai/grammar/simple-sentences-in-catalan-grammar/ 

TalkPal. (2024). Catalan Grammar: A Quick Guide for Language Enthusiasts.TalkPal AI. Retrieved from: https://talkpal.ai/catalan-grammar/ 

Translinguo Global. (2022). “Todo lo que necesitas saber sobre el idioma catalán”. Transilguo. Retrieved from: https://translinguoglobal.com/idioma-catalan/ 


### Models:
### Generate a grammar that recognizes the language.
E -> NP VP | NP VP NP | VP | E Conj E  
NP -> Det N | PropN | Pron | Det N Adj | Det N PP | PropN PP | Pron PP  
PP -> P NP  
VP -> V | V Adv | V PP  

Adj -> 'gran' | 'blau' | 'bonic' | 'veloc' | 'vermell'  
Adv -> 'ràpidament' | 'ben'  
V -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van'  
Conj -> 'i' | 'o' | 'però' | 'sinó' | ','  
Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' | 'nenes' | 'nens'  
P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'  
PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'  
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' | 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'  

### Eliminate Ambiguity in the grammar.
E -> E Conj E2 | E2  
E2 -> S | S2 | VP  
S -> NP VP  
S2 -> NP VP NP    
NP -> Det N | PropN | Pron | Det N Adj | Det N PP | PropN PP | Pron PP  
PP -> P NP  
VP -> V | V Adv | V PP  
  
Adj -> 'gran' | 'blau' | 'bonic' | 'veloc' | 'vermell'  
Adv -> 'ràpidament' | 'ben'  
V -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van'  
Conj -> 'i' | 'o' | 'però' | 'sinó' | ','  
Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' |  
 'nenes' | 'nens'    
P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'    
PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'    
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' |
 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'  
  

### Eliminate left recursion in the grammar.
 S -> NP VP  
S2 -> NP VP NP  
NP -> Det N | PropN | Pron | Det N Adj  | Det N PP | PropN PP  | Pron PP  
PP -> P NP  
VP -> V  | V Adv | V PP  
E' -> Conj E2 E' | ϵ  

Adj -> 'gran' | 'blau' | 'bonic' | 'veloc' | 'vermell'  
Adv -> 'ràpidament' | 'ben'  
V -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van'  
Conj -> 'i' | 'o' | 'però' | 'sinó' | ','  
Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' | 'nenes' | 'nens'  
P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'  
PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'  
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' | 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'  



#### Adapted for the code
The code didn´t accept the use of ‘ so it was changed to the following:

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
V -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van'  
Conj -> 'i' | 'o' | 'però' | 'sinó' | ','  
Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' | 'nenes' | 'nens'  
P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'  
PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'  
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' | 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'  




#### Strings to accept
Sentence patterns that are accepted are
- Subject + Verb + Adverb
- Subject + Verb + Prepositional Phrase
- Plus the use of conjunctions.


Only valid sentences are accepted, and adjective on its own is not valid.

###### Valid
- "Maria corre ràpidament",
- "ells ballant a Barcelona",
- "ell va a Catalunya",
###### Invalid
- "ràpidament",
- "ella vive en Barcelona",
- "ells bailaaant na Barclona"


### Implementation:
The implementation uses the library nltk in python.
To test every grammar modification (ambiguous, non ambiguous and no left recursion):
https://colab.research.google.com/drive/1nnfthD9neyCilSnmddMhJuA5_lhBcYDd?usp=sharing 

### Test: 
Run the program to accept the grammar. 

### Analysis:
(Thoroughly explain what type of grammar it is (Chomsky Hierarchy Extended Level), what traits does it have, and why is not on any other level.)


