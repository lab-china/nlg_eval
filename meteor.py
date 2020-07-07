# https://www.nltk.org/api/nltk.translate.html
# http://compling.hss.ntu.edu.sg/wnja/
import nltk
# import nltk.translate.meteor_score.single_meteor_score as single_meteor_score
import nltk.translate.meteor_score as meteor_score
try:
  nltk.data.find('corpora/wordnet/lexnames')
except LookupError:
  nltk.download('wordnet')

hypothesis1 = 'It is a guide to action which ensures that the military always obeys the commands of the party'
hypothesis2 = 'It is to insure the troops forever hearing the activity guidebook that party direct'
reference1 = 'It is a guide to action that ensures that the military will forever heed Party commands'
reference2 = 'It is the guiding principle which guarantees the military forces always being under the command of the Party'
reference3 = 'It is the practical guide for the army always to heed the directions of the party'


hypothesis1 = 'それは軍が常に党の命令に従うことを保証する行動へのガイドです'
hypothesis2 = 'それはパーティーが直接活動ガイドブックを聞いて軍隊に永遠に保険をかけることです'
reference1 = 'それは軍が永遠に党の命令に耳を傾けることを保証する行動へのガイドです'
reference2 = '軍隊が常に党の指揮下にあることを保証するのは指導原則です'
reference3 = 'それは軍が常に党の指示に注意を払うための実用的なガイドです'
def splitString(str):
    outStr=""
    for i in list(str):
        outStr=outStr+i+" "
    return outStr
hypothesis1=splitString(hypothesis1)
hypothesis2=splitString(hypothesis2)
reference1=splitString(reference1)
reference2=splitString(reference2)
reference3=splitString(reference3)
# print( round(meteor_score.meteor_score([reference1, reference2, reference3], hypothesis2),4))
# print( round(meteor_score.single_meteor_score(reference1, hypothesis2),4))
print( meteor_score.exact_match(reference1, hypothesis2))