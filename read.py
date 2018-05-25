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

instances = []
# (label, [features])

train = open("train_file_cmps142_hw3", "r")
for line in train:
	label = line[:line.find('\t')]
	trim = line[line.find('\t')+1:]
# 	print trim
	tokens = word_tokenize(trim.lower())
	tokens2 = [unicode(tok) for tok in tokens if (tok not in remove) and (tok not in string.punctuation)]
	singles = [stemmer.stem(tok) for tok in tokens2]
	
	instances.append((label, singles))
	for token in singles:
		if token in v_dict.keys():
			v_dict[token] = v_dict[token] + 1;
		else:
			v_dict[token] = 1;
# 	print singles;
# print v_dict;
print instances
for token,count in v_dict.iteritems():
	if (token in v_dict) and (v_dict[token] > 4):
# 		print token
		vocab.append(token)
for word in sorted(vocab):
	print word, ' ',
print len(vocab)

print
print 'label,',
for feature in v_dict.keys():
	print ("%s," % feature),;
print
for label,features in instances:
	print "%s," % label,
	for feat in v_dict.keys():
		str = feat if (feat in features) else ''
		print "%s," % str,;
	print '';
#for label,features in instances:
# 	print "%s," % label,;
# 	for feature in v_dict.keys():
# 		if feature in features:
# 			print ("%s," % feature),;
# 		else:
# 			print ',',;
# 	print tokens2;
