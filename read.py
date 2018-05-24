#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python2
import sys
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

reload(sys)
sys.setdefaultencoding('utf-8')

remove = stopwords.words()
# print remove
print string.punctuation
stemmer = PorterStemmer();
v_dict = {}
vocab = []

train = open("train_file_cmps142_hw3", "r")
for line in train:
	trim = line[line.find('\t')+1:]
# 	print trim
	tokens = word_tokenize(trim.lower())
	tokens2 = [unicode(tok) for tok in tokens if (tok not in remove) and (tok not in string.punctuation)]
	singles = [stemmer.stem(tok) for tok in tokens2]
	for token in singles:
		if token in v_dict:
			v_dict[token] = v_dict[token] + 1;
		else:
			v_dict[token] = 1;
# 	print singles;
print v_dict;
for token,count in v_dict.iteritems():
	if (token in v_dict) and (v_dict[token] > 4):
# 		print token
		vocab.append(token)
print vocab
print len(vocab)
# 	print tokens2;
