#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python2
import sys
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
import time
from nltk.stem.porter import PorterStemmer

reload(sys)
sys.setdefaultencoding('utf-8')

remove = stopwords.words()
stemmer = PorterStemmer()

train = open("train_file_cmps142_hw3", "r")
#print "starting preprocessing..."
start = time.clock()

#need to get number of distinct tokens in the train set
# tokens = word_tokenize(train.read().lower())
# filtered_tokens = [word for word in tokens if word not in remove and word not in string.punctuation]
# stemmed_tokens = [stemmer.stem(words.decode('utf-8')) for words in filtered_tokens]

# distinct_tokens = dict.fromkeys(set(stemmed_tokens), 0)

# for word in stemmed_tokens:
# 	distinct_tokens[word] += 1

# vocabulary = stemmed_tokens

# for word in stemmed_tokens:
# 	if distinct_tokens[word] < 5:
# 		vocabulary.remove(word)

# vocabulary = set(vocabulary)
# print "the size of the vocabulary is " + str(len(vocabulary)) 

distinct_tokens = dict()
corpus = []
for line in train:
	new_line = line[line.find('\t')+1:]
	tokens = word_tokenize(new_line.lower())
	filtered_tokens = [word for word in tokens if (word not in remove) and (word not in string.punctuation)]
	
	stemmed_tokens = [stemmer.stem( unicode(words)) for words in filtered_tokens]
	
	for word in stemmed_tokens:
		if word in distinct_tokens.keys():
			distinct_tokens[word] += 1
		else:
			distinct_tokens[word] = 1
	
	corpus.append(stemmed_tokens)


# for line in corpus:
# 	for word in line:
# 		if distinct_tokens[word] < 5:
# 			line.remove(word)

vocabulary = []
for k,v in distinct_tokens.iteritems():
	if v >= 5:
		vocabulary.append(k)
for word in sorted(vocabulary):
	print word

#discrepency with unique values top code = 2989, this code says 1131
#requires step 7 and check on validity of lines 56 - 59 
			




end = time.clock()
#print "ended preprocessing in " + str(end-start) + " seconds"
