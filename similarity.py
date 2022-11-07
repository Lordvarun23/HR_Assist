import textdistance as td
from sent2vec.vectorizer import Vectorizer

def calc_similarity(jd,resume):
    '''
    To Calculate the similarity measures of resume and job description
    :param jd:
    :param resume:
    :return float:
    '''

    vectorizer = Vectorizer()
    rs = vectorizer.run(resume)
    j = vectorizer.run(jd)

    j = td.jaccard.similarity(rs,j)
    s = td.sorensen_dice.similarity(rs, j)
    c = td.cosine.similarity(rs, j)
    o = td.overlap.normalized_similarity(rs, j)
    total = (j + s + c + o) / 4

    return round(total*100,2)
