import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import FreqDist
from nltk.tokenize import sent_tokenize

lem_data = []
lemmatizer = WordNetLemmatizer()
data=(open('test.txt').read())
print(data)  #Original data from 'test.txt' file
sent_data = sent_tokenize(data)  #Sentence tokenization applied here
print(sent_data)
word_data = []
for words in sent_data:
    word_data.append(word_tokenize(words))   #Word tokenization applied here on sentences which were tokenized above.
print("Tokenized data...... ")
print(word_data)
for sent in word_data:
    for word in sent:
        lem_data.append(lemmatizer.lemmatize(word))  #lemmatization applied here
print(lem_data)
print("Lemmatized data.....")
print(lem_data)
pos_words=pos_tag(lem_data) #POS applied here
print ("POS tagged data.....")
print(pos_words)
temp1 = []
for word in pos_words:
    if(word[-1] not in ['VBN','VBZ','VB','VBD','VBG','VBP']):    #Removing all verbs from the pos tagging words
        temp1.append(word[0])
pos_words = temp1
print("Data after removing all verbs....")
print(pos_words)
wordfreq= FreqDist(pos_words)  #Frequency distribution applied here
print(wordfreq.most_common(5))  #Printing the top 5 most repeated strings with frequencies.
temp =[]
bucket = []
temp = wordfreq.most_common(5)
for word in temp:
    bucket.append(word[0])   #Picking the top 5 repeated strings.
print(bucket)
print("List with no verbs:")
print(pos_words)
pos_words = ' '.join(map(str, pos_words))
print("Converting the 'lists(pos_words) with no verbs' to string: ")
print(pos_words)
new_sent_data = sent_tokenize(pos_words)  #Sentence tokenizing the new data without verbs
print("Sentences tokenized on new data with no verbs:")
print(new_sent_data)
final_sent = []
for sentence in new_sent_data:
    if (any(map(lambda word: word in sentence, bucket))):   #Picking the senetnces which has one of the most repeated words.
        final_sent.append(sentence)
final_sent = ''.join(map(str, final_sent))
print("Sentences which has any one of the repeated strings are:")
print(final_sent)


