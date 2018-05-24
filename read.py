#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python2
import sys
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

reload(sys)
sys.setdefaultencoding('utf-8')

remove = stopwords.words()
print remove

print string.punctuation

train = open("train_file_cmps142_hw3", "r")
for line in train:
	tokens = word_tokenize(line.lower())
	tokens2 = [x for x in tokens if x not in remove and x not in string.punctuation]
	print tokens2;
