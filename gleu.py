import nltk
import nltk.translate.gleu_score as gleu

import numpy
import os

try:
  nltk.data.find('tokenizers/punkt/japanese.pickle')
except LookupError:
  nltk.download('punkt/japanese.pickle')
hyp =   str('彼女は 世界史に 興味が あった ので 本を 読んだ').split()
ref_a = str('彼女は 世界史に 興味が あった ので 本を 読んだ').split()
ref_b = str('彼女は 世界史に 興味が　ある 　ので 本を 読んだ').split()


hyp =   list('彼女は世界史に興味があったので本を読んだ')
ref_a = list('彼女は世界史に興味があったので本を読んだ')
ref_b = list('彼女は世界史に興味があるので本を読んだ')
score_ref_a = gleu.sentence_gleu([ref_a], hyp)
print("Hyp and ref_a are the same: {}".format(score_ref_a))
score_ref_b = gleu.sentence_gleu([ref_b], hyp)
print("Hyp and ref_b are different: {}".format(score_ref_b))
score_ref_ab = gleu.sentence_gleu([ref_a, ref_b], hyp)
print("Hyp vs multiple refs: {}".format(score_ref_ab))