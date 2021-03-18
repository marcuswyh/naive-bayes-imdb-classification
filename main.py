import os
import math

pos_path = 'data\\trainSmall\\pos\\'
neg_path = 'data\\trainSmall\\neg\\'

test_neg = 'data\\test\\neg\\'
test_pos = 'data\\test\\pos\\'

pos_listing = os.listdir(pos_path)
neg_listing = os.listdir(neg_path)

test_listing_n = os.listdir(test_neg)
test_listing_p = os.listdir(test_pos)

vocab = set()

pos_totalWords = []
neg_totalWords = []

#positive files
for file in pos_listing:
    
    f = open(pos_path+file, "r", encoding="utf8")
    
    allWords = f.read().split()
    
    for word in allWords:
        vocab.add(word)
        pos_totalWords.append(word)

    f.close()

#negative files
for file in neg_listing:
    
    f = open(neg_path+file, "r", encoding="utf8")
    
    allWords = f.read().split()
    
    for word in allWords:
        vocab.add(word)
        neg_totalWords.append(word)
    
    f.close()

pos_dict = dict.fromkeys(vocab, 0)
neg_dict = dict.fromkeys(vocab, 0)

for p in pos_totalWords:
    key = p
    if key in vocab:
        pos_dict[p]+=1

for p in neg_totalWords:
    key = p
    if key in vocab:
        neg_dict[p]+=1

print ("done frequency counting")


#===========================================

pos_prob = dict.fromkeys(vocab, 0)
neg_prob = dict.fromkeys(vocab, 0)

for word in pos_dict:
    pos_prob[word] = (pos_dict[word]+1) / (len(pos_totalWords) + len(vocab))
    
print ("done positive probability dictionary")

for word in neg_dict:
    neg_prob[word] = (neg_dict[word]+1) / (len(neg_totalWords) + len(vocab))
    
print ("done negative probability dictionary")


#===========================================

pos_probability= 0
neg_probability= 0
pos_review= 0
neg_review = 0
is_pos = False

if is_pos ==True:
    for file in test_listing_p:
        f = open(test_pos+file, "r", encoding="utf8")
        
        allWords = f.read().split()
        
        for word in allWords:
            try:
                pos_probability += math.log(pos_prob[word])
                neg_probability += math.log(neg_prob[word])
            except KeyError:
                pos_probability += 0
                neg_probability += 0
        
        if pos_probability > neg_probability:
            pos_review += 1
        else:
            neg_review +=1
    
        pos_probability = 0
        neg_probability = 0
else: 
    for file in test_listing_n:
        f = open(test_neg+file, "r", encoding="utf8")
        
        allWords = f.read().split()
        
        for word in allWords:
            try:
                pos_probability += math.log(pos_prob[word])
                neg_probability += math.log(neg_prob[word])
            except KeyError:
                pos_probability += 0
                neg_probability += 0
        
        if pos_probability > neg_probability:
            pos_review += 1
        else:
            neg_review +=1
    
        pos_probability = 0
        neg_probability = 0
    
print ("")
print ("Results")
print ("=======")
print ("positive : {}, negative : {}".format(pos_review, neg_review))
if is_pos:
    print("accuracy percentage: ", (pos_review/(pos_review + neg_review))*100, "%")
else:
    print("accuracy percentage: ", (neg_review/(pos_review + neg_review))*100, "%")

