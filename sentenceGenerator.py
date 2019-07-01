# Lexical Categories
NOUN = []
VERB = []
AUX = []
ADJECTIVE = []
DETERMINER = []
PREPOSITION = []
ADVERB = []
CONJUNCTION = []



# Phrases
NP, VP, PP = [],[],[]

NP = [NOUN,
      [DETERMINER, NOUN],
      [DETERMINER, ADJECTIVE, NOUN],
      [DETERMINER, NOUN, PP],
      [DETERMINER, ADJECTIVE,NOUN,PP]
      [NP, CONJUNCTION, NP]]
VP = [VERB,
      [VERB, NP],
      [VERB, NP, ADVERB],
      [VERB, NP, PP],
      [VERB, PP, ADVERB]
      [VP, CONJUNCTION, VP]]
PP = [PREPOSITION,
      [PREPOSITION, NP]
      [PP, CONJUNCTION, PP]]


SENTENCE = []
SENTENCE = [[NP, VP],
            [NP, AUX, VP],
            [SENTENCE, CONJUNCTION, SENTENCE]]