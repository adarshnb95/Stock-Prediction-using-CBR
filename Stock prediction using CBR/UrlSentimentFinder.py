# -*- coding: utf-8 -*-
from senti_classifier import senti_classifier
#import UrlReader as u

def getSentiment(url,date,company,num,sentences):
	#print(url)
	#sentences = u.dataFromURL(url)
	#print(type(sentences))
	#print(sentences.split(". "))
	#sentences = sentences.split(". ")
    pos_score, neg_score = senti_classifier.polarity_scores(sentences);
    f = open("Articles/"+company+date+"_"+str(num)+'.txt', 'w');
    f.write(". ".join(sentences).encode('utf-8'));
    f.close();
    return(str(pos_score) + " " + str(neg_score))
    """
	if pos_score < neg_score:
		return ("Negative")
	elif pos_score > neg_score:
		return ("Positive")
	else:
		return ("Neutral")"""


	#getSentiment("xyx",'20170401','amazon',0,"This is Sahil. I am good")
