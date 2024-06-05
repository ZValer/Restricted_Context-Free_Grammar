# Restricted_Context-Free_Grammar
E2 Generating and Cleaning a Restricted Context Free Grammar

## Catalan 

### Description:
#### History
Catalan, despite being mostly spoken in Spain, shares a lot of similarities with French. Its vocabulary  “has more in common with Occitan of southern France than with Spanish. It shares about 70 % of its lexicon with the first and about  20% with the second” (Gutman & Avanzati, 2013).


After the loss of Catalonia's independence to the Crown of Castile, Catalan culture was affected by new laws that promoted the use of Spanish. However, in the early 19th century, several artists, authors and playwrights helped revive the language. Although until 1975 its use was prohibited and it was prohibited to give Catalan names to newborns, as well as street names, in music, television and cinema, it was even prohibited to speak Catalan in public. Currently, Catalan is the official language in Andorra and co-official in Valencia, Catalonia and the Balearic Islands (Translinguo Global, 2022).

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

#### Generating the grammar that recognizes the language

Let's break down the analysis to generate a grammar that recognizes de language.  
The following sentences patters were considered plus the use of conjunctions.

1. Subject + Verb + Adjective: La casa és verda. (The house is green)
2. Subject + Verb + Adverb: Ell camina ràpid. (He walks fast)
3. Subject + Verb + Prepositional Phrase: Ella viu a Venècia. (She lives in Venice)
4. Subject + Verb: Ella corre. (She runs)

In the first rule (E) we have the option to form sentences with Subject (S) and Verb (V), having the possibility to later include additions, like adjetive, adverb or prepositional phrase. And also to form sentences with conjunctions.  

```
E -> S V | E Conj E
```
The nexts 2 rules indicate the forms that a Subject can take:
1. Subjects can go after a determinant which are predominal modifiers that can be an article (Art), an article (Art) with a possessive adjective (AdjPos) or an adjective complement (AdjC).

Articles in Catalan are definite: “el”, “la”, “els” and “les” or indefinite: “un” and “una”. Grouping an article with a possessive adjective indicate possesion overall. For example: "**My** dad" traslates to "**el meu** pare", having "el (Art) meu (AdjPos) pare". Lastly adjective complement (AdjC) include demonstrative ("aquest", "aquesta"), quantitative ("quatre", "cinc") and numeral ("alguns", "pocs", "molts") adjectives (TalkPal, 2024).

2. Subjects can also take the form of Pronouns ('jo', 'tu', 'ell'), Nouns ('girafa', 'avió', 'pares' ) or Proper Nouns ('Xavi', 'Albert', 'Montse').

3. And they can be added a qualitative adjective (AdjQual) to the describe the nouns, "and in Catalan, they agree in gender and number with the nouns they modify." (TalkPal, 2024).
   
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

"Additionally, Catalan prepositions (such as “a,” “de,” “en,” “amb”) help you connect words and phrases and show relationships between them" (TalkPal, 2024). A prepositional phrase consists of a preposition and a subject and we will consider the possibility of having more than une combination of these. So we can form sentences like "Xavi , Montse i Albert van ***a** Venècia...**amb** avió...**amb** els seus pares"*

```
PP -> Prep S | PP PP
```

The non terminals include a vocabulary of words of the language separated by category: 
```
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
```

Joining all the rules we get the following **grammar**:
``` ruby
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
```

#### Eliminate Ambiguity in the grammar.
The previous grammar recognizes the language, however, it is ambiguous. This means a string can formed in more than own way with this rules, For example for: "la casa és verda" these are a few ways that a Parse tree can be produced. 

![image](https://github.com/ZValer/Restricted_Context-Free_Grammar/assets/111622587/0f8dd85e-8fcf-4faf-b2da-9c0c37085afa)


To eliminate ambiguity this steps need to be followed:  
1. Read from left to right, if ambiguous (Same level of priority) then:  
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
  - S -> Det **S** | Pron | N | PropN | **S** AdjQual | **S Conj S**

For this rule, a few non-terminals where added, this way the tree can only follow one path:
```
S -> S Conj S2 | S2
S2 -> S3 AdjQual | S3
S3 -> Det S4 | S4
S4 -> Pron | N | PropN 
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

Leaving us with the next grammar, where inputs can only generate one Parse tree:  

**Unambiguous Grammar:**
``` ruby
  E ->  E Conj E2 | E2
  E2 -> S V
  S -> S Conj S2 | S2
  S2 -> S3 AdjQual | S3
  S3 -> Det S4 | S4
  S4 -> Pron | N | PropN 
  Det -> Art | Art Det2 | AdjC
  Det2 -> AdjPos | AdjC
  V -> V Conj V2 | V2
  V2 -> V3 AdjQual | V3 Adv | V3 PP | V3 AdjQual | V3
  PP -> PP Prep S | Prep S


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
```

#### Eliminate left recursion in the grammar.
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

Leaving us with the following **grammar without left recursion**:
```ruby
E ->  E2 E’
E’ -> Conj E2 E’ | ϵ
E2 -> S V 
S -> S2 S’
S’ -> Conj S2 S’ | ϵ
S2 -> S3 AdjQual | S3
S3 -> Det S4 | S4
S4 -> Pron | N | PropN 
Det -> Art | Art Det2 | AdjC
Det2 -> AdjPos | AdjC
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



### Implementation:
The implementation of the grammar uses the library nltk in python.
To test every grammar modification consult the following:  
**Ambiguous**:   
https://colab.research.google.com/drive/1ZFGeFtPMJD-o7N5yyRCJoIGnKDu_psA6?usp=sharing    
**Non ambiguous**:   
https://colab.research.google.com/drive/1wI5OKmj2THOuXVgumSIPAoSad24vbEor?usp=sharing     
**No left recursion**:   
https://colab.research.google.com/drive/1n-aFM1E9AETQpezNtEoQ5MkyGFUd27ZV?usp=sharing    

#### Grammar adapted for the code for 'No left recursion"
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

These steps were followed through all the grammar. Leaving us with a grammar representing the previous grammar that can be parsed with nltk library:  

``` ruby
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
    - Ella corre. (She runs)
5. Conjugated Verb
    - corre. (run)
6. Conjunctions with this sentences paterns

### Tests: 
After running each program you can see the tests with the previous this defined sentences: 

###### Valid sentences
- "la casa és verda",
- "les cinc pilotes vermelles i les dues pilotes blaves són petites",
- "ella corre ràpid",
- "Albert cuina bé i cuina ràpid",
- "aquelles noies visitan a la escola",
- "el taxi va a la ciutat",
- "ella viu a València amb la seva germana",
- "la Montse treballa",
- "Eva i Albert són alts però la Montse i Albert són baixos",
- "alguns nens criden i ploren perquè estan tristos",
- "Xavi , Montse i Albert van a Venècia amb avió amb els seus pares",

###### Invalid sentences
- "ràpidament",
- "ella vive en Barcelona",
- "this sentence is in English",
- "corre verda ella les"
- "scjv ddkd ddd cf"

The expected output for the valid sentences is "Valid grammar" and a Parse Tree and for the invalid sentences it should print "Invalid grammar" and the error if it´s the case. 
Here is an example of the output of the test with the same sentence in every modification (To see the rest go to:
**Ambiguous**:   
https://colab.research.google.com/drive/1ZFGeFtPMJD-o7N5yyRCJoIGnKDu_psA6?usp=sharing    
**Non ambiguous**:   
https://colab.research.google.com/drive/1wI5OKmj2THOuXVgumSIPAoSad24vbEor?usp=sharing     
**No left recursion**:   
https://colab.research.google.com/drive/1n-aFM1E9AETQpezNtEoQ5MkyGFUd27ZV?usp=sharing    


**Ambiguous**:    
![image](https://github.com/ZValer/Restricted_Context-Free_Grammar/assets/111622587/70196a46-f5cd-4f64-b703-57e98e18a6c4)
![image](https://github.com/ZValer/Restricted_Context-Free_Grammar/assets/111622587/ff0eb5e0-87f2-42f2-a8d5-7b1b0e0da36b)  


**Non ambiguous**:    
![image](https://github.com/ZValer/Restricted_Context-Free_Grammar/assets/111622587/72c11d51-37d6-4648-b7b3-4d70bb28c95d)  

**No left recursion**:    
![image](https://github.com/ZValer/Restricted_Context-Free_Grammar/assets/111622587/4272a155-3bf8-4d45-a1fe-4c0589ba8bb2)  
  

### Analysis:
**Grammar** includes a set of rules which we can derive strings. These rules are effectively statements of logical equivalence of tht form  ψ → ω, where ψ and ω are strings (Caltech, s.f.). Each branch corresponds to one rule. The mother of each branch corresponds to ψ and the daughters to ω. 

The language that is being modelled can be described in a **context-Free grammar**, in which all rules of R are of the form A → ψ  
- **A:** is a single non-terminal element of V<sub>N</sub>
- **ψ:** is a string of terminals from V<sub>T</sub> and non-terminals from of V<sub>N</sub>.
  
Example...  
- **V<sub>T</sub>** = {a, b}
- **V<sub>N</sub>** = {S, A}
- **S**=S
- **R** = {S → Ab, A → ε , A → Aa] 

In the model analyzed of Catalan the non terminals are elements such as Subject, Verb, Adverb, Prepositional Phrase; and terminal are words such as 
'gran', 'blau', 'ràpidament', 'ben','visitan', 'corre'.


This context-free grammar that can be accepted with a push-down automaton. In the Chomsky Hierarchy it is the second less restricted grammar, more complex than a regular grammar that can be accepted with a finite automaton (Tecumseh, 2014).
![image](https://github.com/ZValer/Restricted_Context-Free_Grammar/assets/111622587/a39091c7-42f5-427f-aec4-f73d363d10ff)

Context free grammars are defined as “rewrite rules” which allow one string to be rewritten as another string, given certain restrictions. For example, a context-free grammar can include rules such as  
A -> A B C  
which says to rewrite the string ‘A’ as the string ‘A B C’. However, a rule such as  
z A -> A B C  
which indicates that A can be so rewritten only when preceded by a z would be a “context sensitive” grammar (Tecumseh, 2014). Which is not the case for the grammar previously generated. Where rules are written in the first way. 

### Time complexity
**Ambiguous**:    
General Context-Free Grammars have a time complexity of O($n^3$).

**Non ambiguous**:  
Unambiguous Context-Free Grammars have a time complexity of O($n^2$).

**No left recursion**:   
LL(1) Grammars have a time complexity of O(n).

After analizing each code we can declare that the most efficient for the problem is the grammar with no left recursion. 

### References:

Gutman, A. & Avanzati, B. (2013). Catalan. The Language Gulper. Retrieved from:
https://www.languagesgulper.com/eng/Catalan.html#:~:text=The%20basic%20word%20order%20in,subject%20at%20all%20(impersonal).

TalkPal. (2024). Understanding Simple Sentences in Catalan Grammar. TalkPal AI. Retrieved from: https://talkpal.ai/grammar/simple-sentences-in-catalan-grammar/ 

TalkPal. (2024). Catalan Grammar: A Quick Guide for Language Enthusiasts.TalkPal AI. Retrieved from: https://talkpal.ai/catalan-grammar/ 

Translinguo Global. (2022). “Todo lo que necesitas saber sobre el idioma catalán”. Transilguo. Retrieved from: https://translinguoglobal.com/idioma-catalan/ 

Caltech. (s.f.). Chapter 6 Formal Language Theory. Math.dvi. Retrieved from: https://www.its.caltech.edu/~matilde/FormalLanguageTheory.pdf 

Tecumseh, W. (2014). Toward a computational framework for cognitive biology: Unifying approaches from cognitive neuroscience and comparative cognition. Elsevier. Retrieved from: https://www.sciencedirect.com/science/article/pii/S157106451400058X#fg0040
