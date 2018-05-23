from nltk import word_tokenize
import re

def preprocess_train_set(in_stream):
	s = in_stream.read().decode('utf8')
	tokens = word_tokenize(s)
	print tokens





def _main_():
	file = open('./test_file_cmps142_hw3', 'r')
	preprocess_train_set(file)


_main_()