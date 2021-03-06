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

remove = stopwords.words('english')
stemmer = PorterStemmer()

#generates a list of the labels for each line
def generate_labels_list(in_stream):
	in_stream.seek(0)
	labels = []
	for line in in_stream:
		labels.append(line[:line.find('\t')])
	return labels

#removes words with count less than 5
def remove_irrelevant_words(vocabulary):
	for word,count in vocabulary.items():
		if count < 5:
			del vocabulary[word]
	return vocabulary

# creates a bag of words representation. 
# each word gets its corresponding cout
def associate_token_with_count(corpus, tokens):
	new_corpus = []
	for line in corpus:
		new_corpus.append(dict())
		for word in line:
			if word in tokens.keys():
				new_corpus[-1][word] = tokens[word]
	return new_corpus
# fill each line with 0 counts for words that don't exist
# map each line to its corresponding header label
def feature_list_to_csv(corpus, vocabulary, labels):
	csv_array = []
	line_num = 0

	for line in corpus:
		for word,count in vocabulary.items():
			if word not in line:
				line[word] = 0
		line.update({'label': labels[line_num]})
		csv_array.append(line)
		line_num += 1
	
	first_line = csv_array[0].keys()
	
	first_line.append('label')
	csv_array.insert(0, first_line)
	return csv_array
# tokenize, remove 	
def filter_tokens(line, stopwords, stemmer):
	line_without_label = line[line.find('\t')+1:]
	tokens = word_tokenize(line_without_label.lower())

	filtered_tokens = [word for word in tokens if (word not in stopwords) and (word not in string.punctuation)]
	stemmed_tokens = [stemmer.stem(unicode(words)) for words in filtered_tokens]
	return stemmed_tokens

def write_to_csv(outfile, bag_of_words):
	count = 1
	for key in bag_of_words[0]:
		outfile.write("\"%s\"," % key)
	outfile.write('\n')
	keys = bag_of_words.pop(0)

	for line in bag_of_words:
		sys.stdout.write("\rWriting line %d to csv" % count)
		sys.stdout.flush()
		count+=1
		for key in keys:
			outfile.write("%s," % line[key])
		outfile.write("\n")
	sys.stdout.write("\nFinished writing csv")

def preprocess_test_set(in_stream, feature_space):
	count = 1
	corpus = []
	remove = stopwords.words()
	stemmer = PorterStemmer()
	distinct_tokens = dict()
	in_stream.seek(0)
	
	for line in in_stream:
		sys.stdout.write("\rProcessing line %d" % count)
		sys.stdout.flush()
		count+=1
		stemmed_tokens = filter_tokens(line,remove,stemmer)
		corpus.append(stemmed_tokens)
		
	corpus = associate_token_with_count(corpus,feature_space)
	labels = generate_labels_list(in_stream)
	csv_ready = feature_list_to_csv(corpus,feature_space,labels)
	output = open("HW3_Shehan_test.csv", "w");

	write_to_csv(output,csv_ready)

	output.close()

def preprocess_train_set(in_stream):
	count = 1
	corpus = []
	remove = stopwords.words()
	stemmer = PorterStemmer()
	distinct_tokens = dict()
	in_stream.seek(0)
	
	for line in in_stream:
		sys.stdout.write("\rProcessing line %d" % count)
		sys.stdout.flush()
		count+=1
		stemmed_tokens = filter_tokens(line, remove, stemmer)
		corpus.append(stemmed_tokens)
		for word in stemmed_tokens:
			if word in distinct_tokens:
				distinct_tokens[word] += 1
			else:
				distinct_tokens[word] = 1
	sys.stdout.write("\nProcessing complete\n")
	vocabulary = remove_irrelevant_words(distinct_tokens)
	corpus = associate_token_with_count(corpus,vocabulary)
	labels = generate_labels_list(in_stream)
	csv_ready = feature_list_to_csv(corpus,vocabulary,labels)

	output = open("HW3_Shehan_train.csv", "w");

	write_to_csv(output,csv_ready)

	output.close()

	# will use vocabulary on test set
	return vocabulary

def _main_():
	
	#print "starting preprocessing..."
	start = time.clock()
	
	train_file = open('./train_file_cmps142_hw3', 'r')
	vocabulary = preprocess_train_set(train_file)
	train_file.close()
	
	test_file = open('./test_file_cmps142_hw3', 'r')
	preprocess_test_set(test_file, vocabulary)
	test_file.close()
	
	end = time.clock()
	#print "ended preprocessing in " + str(end-start) + " seconds"



_main_()