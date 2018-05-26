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
sys.stdout.write("Beginning the preprocessing\n")
count = 0;
for line in train:
	label = line[:line.find('\t')]
	trim = line[line.find('\t')+1:]
# 	print trim
	tokens = word_tokenize(trim.lower())
	tokens2 = [unicode(tok) for tok in tokens if (tok not in remove) and (tok not in string.punctuation)]
	singles = [stemmer.stem(tok) for tok in tokens2]
	
	instances.append((label, singles))
	for token in singles:
# 		print token,
		if token in v_dict.keys():
			v_dict[token] = v_dict[token] + 1;
		else:
			v_dict[token] = 1;
	count +=1
	sys.stdout.write("\rPreprocessing instance %i" % count)
	sys.stdout.flush()
sys.stdout.write("\n")

sys.stdout.write("Building vocabulary\n")
for token,count in v_dict.iteritems():
	if (token in v_dict) and (v_dict[token] > 4):
# 		print token
		vocab.append(token)

output = open("output_file.csv", "w");
print "Writing headers"
output.write('label,')
for feat in vocab:
	output.write("\"%s\"," % (feat))
output.write('\n')
print "Writing instances"
count = 0
for label,features in instances:
	count += 1
	sys.stdout.write("\rWriting instance %i to file" % count)
	sys.stdout.flush()
	output.write("%s," % label)
	for feat in vocab:
		value = v_dict[feat] if (feat in features) else 0
		output.write("%i," % value)
	output.write('\n')
sys.stdout.write("\n")
print "Finished."
