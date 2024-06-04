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


### Models:

**Grammar** includes a set of rules which we can derive strings. These rules are effectively statements of logical equivalence of tht form  ψ → ω, where ψ and ω are strings (Caltech, s.f.). Each branch corresponds to one rule. The mother of each branch corresponds to ψ and the daughters to ω. 

The language that is being modelled can be described in a **context-Free grammar**, in which all rules of R are of the form A → ψ  
- **A:** is a single non-terminal element of V<sub>N</sub>
- **ψ:** is a string of terminals from V<sub>T</sub> and non-terminals from of V<sub>N</sub>.
  
Example...  
- **V<sub>T</sub>** = {a, b}
- **V<sub>N</sub>** = {S, A}
- **S**=S
- **R** = {S → Ab, A → ε , A → Aa] 

### Generating the grammar that recognizes the language.
In the model analyzed of Catalan the non terminals are elements such as Subject, Verb, Adverb, Prepositional Phrase; and terminal are words such as 
'gran', 'blau', 'ràpidament',  'ben','menja', 'corre'.

[... Explain LL(1) and way it is going to be used...]

**Grammar:**
``` ruby
E -> S V | V | E Conj E  
S -> Det S | Pron | N | PropN | S AdjQual | S Conj S  
Det -> Art | Art AdjPos | AdjC  
V -> V | V AdjQual | V Adv | V PP | V Conj V  
PP -> Prep S | PP PP  

V -> 'corre' | 'van' |'viatja' | 'visita' | 'visitem' | 'menja' | 'juga' | 'balla' | 'sóc' | 'és' | 'són' | 'som' | 'bota' | 'camina' | 'ploren'  
Art -> 'el' | 'els' | 'la' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
AdjPos -> 'mi' | 'meves' | 'teu' | 'teus' | 'teva' | 'teves' | 'seva' | 'seves' | 'seu' | 'seus' | 'nostra' | 'nostre' | 'nostres'  
AdjQual -> 'gran' | 'petit' | 'blanc' | 'vermell' | 'groc' | 'blau' | 'nou' | 'vell' | 'veloc'  
AdjC -> 'aquest' | 'aquesta' | 'això' | 'aquell' | 'aquella' | 'aquests' | 'aquestes' | 'aquells' | 'aquelles' | 'dos' | 'tres' | 'quatre' | 'cinc' | 'sis' | 'deu' | 'quinze' | 'vint' | 'cent' | 'mil' | 'alguns' | 'pocs' | 'molts' | 'tots'  
Adv -> 'ràpidament' | 'ben'  
Prep -> 'a' | 'davant' | 'baix' | 'cap' | 'amb' | 'contra' | 'de' | 'des' | 'fins' | 'per' | 'si' | 'sobre' | 'després'  
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles'  
N -> 'nens' | 'nadons' | 'nena' | 'nenes' | 'nen' | 'nens' | 'dona' | 'dones' | 'home' | 'homes' | 'girafa' | 'cavall' | 'cotxe' | 'casa' | 'parc' | 'avió' | 'pares' | 'ballet' | 'futbol' | 'escola' | 'poma' | 'carn' | 'pesat'  
PropN -> 'Xavi' | 'Albert' | 'Montse' | 'Eva' | 'Venècia' | 'Andorra' | 'València' | 'Catalonia' | 'Mèxic'  
Conj -> 'i' | 'o' | 'ni' | 'perquè' | 'encara que' | 'doncs' | 'però' | 'encara' | ',' | 'sinó'  
```

Let's break down the analysis. To generate the grammar, the following sentences patters were considered plus the use of conjunctions.

1. Subject + Verb + Adjective: La casa és verda. (The house is green)
2. Subject + Verb + Adverb: Ell camina ràpid. (He walks fast)
3. Subject + Verb + Prepositional Phrase: Ella viu a Girona. (She lives in Girona)
4. Subject + Verb: Ella viu a Girona. (She lives in Girona)
5. Impersonal sentences->Conjugated Verb: corre. (run)

In the first rule (E) we have the option to form sentences with only a Verb (Sentence pattern number 5) or form sentences with Subject and Verb, having the possibility to later include additions, like adjetive, adverb or prepositional phrase.  

```
E -> S V | V | E Conj E
```
The nexts 2 rules indicate the forms that a Subject can take:
1. Subjects can go after a determinant which are predominal modifiers that can be an article (Art), an article (Art) with a possessive adjective (AdjPos) or an adjective complement (AdjC).

Articles in Catalan are “el”, “la”, “els” and “les”. Indefinite articles are “un” and “una” for singular nouns and there are no specific indefinite articles in the plural form. Grouping an article with a possessive adjective indicate possesion overall. For example: "**My** dad" traslates to "**el meu** pare", having "el (Art) meu (AdjPos) pare". Lastly adjective complement (AdjC) include demonstrative ("aquest", "aquesta"), quantitative ("quatre", "cinc") and numeral ("alguns", "pocs", "molts") adjectives (TalkPal, 2024).

2. Subjects can also take the form of Pronouns ('jo', 'tu', 'ell'), Nouns ('girafa', 'avió', 'pares' ) or Proper Nouns ('Xavi', 'Albert', 'Montse').

3. And they can be added qualitative adjectives (AdjQual) to the describe the nouns, "and in Catalan, they agree in gender and number with the nouns they modify." (TalkPal, 2024).
   
5. Additionaly there is also the case where we have more than one Subject joined by a conjunction.

```
S -> Det S | Pron | N | PropN | S AdjQual | S Conj S  
Det -> Art | Art AdjPos | AdjC
```

Verbs in Catalan are classified into three groups with its distinct conjugation pattern based on their infinitive endings: “-ar,” “-er,” and “-ir.” Catalan also has auxiliary verbs (like ‘to have’ and ‘to be’) that combine with other verbs to create compound tenses and passive voice (TalkPal, 2024). But auxiliary verbs will not be considered for this grammar.  

As can be seen in the sentence's patterns, verbs can be alone or they can be followed by a qualitative adjetive, an adverb or a Prepositional Phrase. And we can include one or many verbs.

```
V -> V | V AdjQual | V Adv | V PP | V Conj V
```

"Additionally, Catalan prepositions (such as “a,” “de,” “en,” “amb”) help you connect words and phrases and show relationships between them" (TalkPal, 2024). A prepositional phrase consists of a preposition and a subject and we will consider the possibility of having more than une combination of these. So we can form sentences like "Xavi , Montse i Albert van **a Venècia**...**amb avió**...**amb els seus pares**"

```
PP -> Prep S | PP PP
```

The non terminals include words of the language separated by category: 
```
V -> 'corre' | 'van' |'viatja' | 'visita' | 'visitem' | 'menja' | 'juga' | 'balla' | 'sóc' | 'és' | 'són' | 'som' | 'bota' | 'camina' | 'ploren'  
Art -> 'el' | 'els' | 'la' | 'les' | 'un' | 'una' 
AdjPos -> 'mi' | 'meves' | 'teu' | 'teus' | 'teva' | 'teves' | 'seva' | 'seves' | 'seu' | 'seus' | 'nostra' | 'nostre' | 'nostres'  
AdjQual -> 'gran' | 'petit' | 'blanc' | 'vermell' | 'groc' | 'blau' | 'nou' | 'vell' | 'veloc'  
AdjC -> 'aquest' | 'aquesta' | 'això' | 'aquell' | 'aquella' | 'aquests' | 'aquestes' | 'aquells' | 'aquelles' | 'dos' | 'tres' | 'quatre' | 'cinc' | 'sis' | 'deu' | 'quinze' | 'vint' | 'cent' | 'mil' | 'alguns' | 'pocs' | 'molts' | 'tots'  
Adv -> 'ràpidament' | 'ben'  
Prep -> 'a' | 'davant' | 'baix' | 'cap' | 'amb' | 'contra' | 'de' | 'des' | 'fins' | 'per' | 'si' | 'sobre' | 'després'  
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles'  
N -> 'nens' | 'nadons' | 'nena' | 'nenes' | 'nen' | 'nens' | 'dona' | 'dones' | 'home' | 'homes' | 'girafa' | 'cavall' | 'cotxe' | 'casa' | 'parc' | 'avió' | 'pares' | 'ballet' | 'futbol' | 'escola' | 'poma' | 'carn' | 'pesat'  
PropN -> 'Xavi' | 'Albert' | 'Montse' | 'Eva' | 'Venècia' | 'Andorra' | 'València' | 'Catalonia' | 'Mèxic'  
Conj -> 'i' | 'o' | 'ni' | 'perquè' | 'encara que' | 'doncs' | 'però' | 'encara' | ',' | 'sinó'  
```

### Eliminate Ambiguity in the grammar.
The previous grammar recognizes the language, however, it is ambiguous. This means a string can formed in more than own way with this rules, For example for: "Xavi , Montse i Albert van a Venècia amb avió amb els seus pares" these are a few ways that a Parse tree can be produced. 

[ add images of the parse trees ]

To eliminate embiguity this steps need to be followed:
1. Read from left to right, if ambiguous (Same leves of priority) then:
1.1. Add an intermediate non-terminal
1.2. And an "or" to get to the terminal

Evaluating the previous grammar, reading from left to right, we can found ambiguity in the first rule (E):

  - E -> S V | V | **E Conj E**


Which can be solved adding an intermediate non-terminal and an "or" to get to the terminal
```
E ->  E Conj E2 | E2  
E2 -> S V | V  
```
The next rule we can found ambiguity is S, where we have:
  - S -> Det S | Pron | N | PropN | S AdjQual | **S Conj S**

For this rule, many non-terminals where added: [... more explanation...]
```
S -> S Conj S2 | S2
S2 -> S3 AdjQual | S3
S3 -> Det S4 | PropN | S4
S4 -> Pron | N
```

We also can identify ambiguity in the following rule:
  - V -> V | V AdjQual | V Adv | V PP | V Conj V  

That can be changed to:
```
V -> V Conj V2 | V2
V2 -> V3 AdjQual | V3 Adv | V3 PP | V3 AdjQual | V3
```


Finally there is also ambiguity in this rule
  - PP -> Prep S | PP PP  

Which after removing ambiguity we have:
```
PP -> PP Prep S | Prep S
```
-------------------------------------------

Leaving us with the next grammar, where inputs can only generate one Parse tree:

``` ruby
E ->  E Conj E2 | E2
E2 -> S V | V
S -> S Conj S2 | S2
S2 -> S3 AdjQual | S3
S3 -> Det S4 | PropN | S4
S4 -> Pron | N 
Det -> Art | Art AdjPos | AdjC
V -> V Conj V2 | V2
V2 -> V3 AdjQual | V3 Adv | V3 PP | V3 AdjQual | V3
PP -> PP Prep S | Prep S
 
  
Adj -> 'gran' | 'blau' | 'bonic' | 'veloc' | 'vermell'  
Adv -> 'ràpidament' | 'ben'  
V3 -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van'  
Conj -> 'i' | 'o' | 'però' | 'sinó' | ','  
Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' |  
 'nenes' | 'nens'    
P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'    
PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'    
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' |
 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'
```

### Eliminate left recursion in the grammar.
[ Add why is it important to eliminate left recursion ]

To eliminate left recursion the next rule as followed.
> [!IMPORTANT]
> A -> Aα | β by { A -> βA' , A' -> αA' | ϵ  
> [Add reference]

To eliminate left recursion from this:   
    - E ->  E Conj E2 | E2    
We consider:  
    - A = E  
    - α = Conj E2  
    - β = E2  
    - A'= E'  
Replacing the values on the rule we have:
```
{ A -> β A' , A' -> αA' | ϵ  
{ E -> E2 E' , E' -> Conj E2 E' | ϵ  
```

The next line that has the form A -> Aα | β, where we can find left recursion in the previous grammar is:  
    - S -> S Conj S2 | S2   
Replacing the rule we get:
        - A = S  
        - α = Conj S2  
        - β = S2  
        - A'= S'  

```
{ A -> β A' , A' -> αA' | ϵ
{ S -> S2 S' , S' -> Conj S2 S' | ϵ
```  
For the next line also presents left recursion  
    - V -> V Conj V2 | V2  
And can be transformed in:
```
{ A -> β A' , A' -> αA' | ϵ
{ V -> V2 V' , V' -> Conj V2 V' | ϵ
```  
Finally, for the next line:   
    - PP -> PP Prep S | Prep S  
We can eliminate left recursion:
```
{ A -> β A' , A' -> αA' | ϵ
{ PP -> Prep S PP' , PP' -> Prep S PP' | ϵ
```

Leaving us with the following grammar without left recursion:
```ruby
E ->  E2 E’
E’ -> Conj E2 E’ | ϵ
E2 -> S V | V
S -> S2 S’
S’ -> Conj S2 S’ | ϵ
S2 -> S3 AdjQual | S3
S3 -> Det S4 | PropN | S4
S4 -> Pron | N 
Det -> Art | Art AdjPos | AdjC
V -> V2 V’
V’ ->Conj V2 V’ | ϵ
V2 -> V3 AdjQual | V3 Adv | V3 PP | V3 AdjQual | V3
PP -> Prep S PP’
PP’ -> Prep S PP’ |  ϵ


Adj -> 'gran' | 'blau' | 'bonic' | 'veloc' | 'vermell'  
Adv -> 'ràpidament' | 'ben'  
V3 -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van'  
Conj -> 'i' | 'o' | 'però' | 'sinó' | ','  
Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' | 'nenes' | 'nens'  
P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'  
PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'  
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' | 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'  
```


#### Adapted for the code
The nltk library doesn´t accept the use of ' and ϵ. The next steps were followed to get an acceptable grammar for the library:  

For the following:
```
E ->  E2 E’
E’ -> Conj E2 E’ | ϵ
```
Step 1: Whenever encountering ' change it to 'apos', meaning E' converts to Eapos, for S' changes to Sapos, V' to Vapos and PP' to PPapos.
```
E ->  E2 Eapos
Eapos -> Conj E2 Epos | ϵ

```
2. As for ϵ it had to be explicitely indicated.
As for this case, Eapos can take the value of ϵ / empty, meaning in the first line, E could or could not include Eapos, and in the second line E the same thing. 
```
E ->  E2 Eapos | E2
Eapos -> Conj E2 Eapos | Conj E2

```

These steps were followed through all the grammar. Leaving us with a grammar representing the previous grammar that can be (...) with nltk library:  

``` ruby
E ->  E2 Eapos | E2
Eapos -> Conj E2 Eapos | Conj E2
E2 -> S V | V
S -> S2 Sapos | S2
Sapos -> Conj S2 Sapos | Conj S2
S2 -> S3 AdjQual | S3
S3 -> Det S4 | PropN | S4
S4 -> Pron | N 
Det -> Art | Art AdjPos | AdjC
V -> V2 Vapos | V2
Vapos -> Conj V2 Vapos | Conj V2
V2 -> V3 AdjQual | V3 Adv | V3 PP | V3 AdjQual | V3
PP -> Prep S PPapos |  Prep S
PPapos -> Prep S PPapos | Prep S 


Adj -> 'gran' | 'blau' | 'bonic' | 'veloc' | 'vermell'  
Adv -> 'ràpidament' | 'ben'  
V -> 'menja' | 'corre' | 'va' | 'és' | 'manegen' | 'ballant' | 'van'  
Conj -> 'i' | 'o' | 'però' | 'sinó' | ','  
Det -> 'el' | 'la' | 'els' | 'les' | 'un' | 'una' | 'uns' | 'unes'  
N -> 'gat' | 'gats' | 'gata' | 'gates' | 'cotxe' | 'cotxes' | 'casa' | 'cases' | 'nenes' | 'nens'  
P -> 'a' | 'amb' | 'en' | 'per' | 'sobre'  
PropN -> 'Maria' | 'Pere' | 'Barcelona' | 'Catalunya' | 'Praga' | 'Madris'  
Pron -> 'jo' | 'tu' | 'ell' | 'ella' | 'nosaltres' | 'vós' | 'ells' | 'elles' | 'això' | 'aixòs' | 'aquell' | 'aquella' | 'aquests' | 'aquestes'  
```



#### Strings to accept
Sentence patterns that are accepted plus the use of conjunctions.

1. Subject + Verb + Adjective
    - La casa és verda. (The house is green)
2. Subject + Verb + Adverb
    - Ell camina ràpid. (He walks fast)
3. Subject + Verb + Prepositional Phrase
    - Ella viu a Girona. (She lives in Girona)
4. Subject + Verb
    - Ella viu a Girona. (She lives in Girona)
5. Conjugated Verb
    - corre. (run)
6. Conjunctions with this sentences paterns
    - example 1...
    - example 2...



###### Valid
- "Maria corre ràpidament",
- "ells ballant a Barcelona",
- "ell va a Catalunya",
- "ells ballant a Barcelona i ell va a Catalunya",
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



##### References:

Gutman, A. & Avanzati, B. (2013). Catalan. The Language Gulper. Retrieved from:
https://www.languagesgulper.com/eng/Catalan.html#:~:text=The%20basic%20word%20order%20in,subject%20at%20all%20(impersonal).

TalkPal. (2024). Understanding Simple Sentences in Catalan Grammar. TalkPal AI. Retrieved from: https://talkpal.ai/grammar/simple-sentences-in-catalan-grammar/ 

TalkPal. (2024). Catalan Grammar: A Quick Guide for Language Enthusiasts.TalkPal AI. Retrieved from: https://talkpal.ai/catalan-grammar/ 

Translinguo Global. (2022). “Todo lo que necesitas saber sobre el idioma catalán”. Transilguo. Retrieved from: https://translinguoglobal.com/idioma-catalan/ 

Caltech. (s.f.). Chapter 6 Formal Language Theory. Math.dvi. Retrieved from: https://www.its.caltech.edu/~matilde/FormalLanguageTheory.pdf 
