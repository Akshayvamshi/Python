with open('test') as t: #opening a file named test which has data
    data = t.read()
t.closed
print(data)
data_string= data.replace('(','').replace(')','').replace('.','').replace('"','').replace(',','').replace("'",'')
#from above step all the mentioned special characters will be replaced with space
f=data_string.lower().split()
#here data(string) will be converted to lowercase and splitted into words
print(f)
wordcount={}
for w in f:
    if w not in wordcount:
        wordcount[w] = 1
    else:
        wordcount[w] += 1
#words which occur for first time will be counted as 1 and if they repeat their count is increased by 1.
print(wordcount)


