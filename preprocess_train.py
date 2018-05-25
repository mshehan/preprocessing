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

def getLabels(in_stream):
	in_stream.seek(0)
	labels = []
	for line in in_stream:
		labels.append(line[line.find('\t')])
	return labels

def remove_irrelevant_words(vocabulary):
	for word,count in vocabulary.items():
		if count < 5:
			del vocabulary[word]
	return vocabulary

def prepare_corpus(corpus, tokens):
	new_corpus = []
	for line in corpus:
		new_corpus.append(dict())
		for word in line:
			if word in tokens.keys():
				new_corpus[-1][word] = tokens[word]
	return new_corpus

def featurify(corpus, vocabulary, labels):
	csv_array = []
	csv_array.append(vocabulary.keys())
	csv_array[0].append('label')
	line_num = 0
	for line in corpus:
		for word,count in vocabulary.items():
			if word not in line:
				line[word] = 0
			csv_array.append(line.keys())
			csv_array[-1].append(labels[line_num])
			line_num += 1
	
	return csv_array
	

def preprocess_train_set(in_stream):
	corpus = []
	remove = stopwords.words()
	stemmer = PorterStemmer()
	distinct_tokens = dict()
	in_stream.seek(0)
	
	for line in in_stream:
		line_without_label = line[line.find('\t')+1:]
		tokens = word_tokenize(line_without_label.lower())

		filtered_tokens = [word for word in tokens if (word not in remove) and (word not in string.punctuation)]
		stemmed_tokens = [stemmer.stem(unicode(words)) for words in filtered_tokens]
		corpus.append(stemmed_tokens)
		for word in stemmed_tokens:
			if word in distinct_tokens:
				distinct_tokens[word] += 1
			else:
				distinct_tokens[word] = 1

	
	vocabulary = remove_irrelevant_words(distinct_tokens)
	corpus = prepare_corpus(corpus,vocabulary)
	labels = getLabels(in_stream)
	#csv_ready = featurify(corpus,vocabulary,labels)
	#print vocabulary
	

	





def _main_():
	file = open('./train_file_cmps142_hw3', 'r')
	#print "starting preprocessing..."
	start = time.clock()
	
	#preprocess_train_set(file)

	test = {'a': 1, 'b':2, 'c': 3}
	test2 = []
	test2.append(test.keys())

	print test2[-1]
	
	end = time.clock()
	#print "ended preprocessing in " + str(end-start) + " seconds"



_main_()