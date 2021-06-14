import MeCab
m = MeCab.Tagger()
index={}
with open("wikisamp.txt", encoding="utf-8") as f:
    for line in f:
    	terms = m.parse(line)
    	for i in terms.splitlines():	
    		line_first=i.split()
    		if line_first[0]=="EOS":
    			pass
    		elif line_first[0] not in index:
    			index[line_first[0]]=1
    		else:
    			index[line_first[0]]+=1
with open("tf2.txt", "w", encoding="utf-8") as f2:
	for i in index:
		f2.write(i + ": " + str(index[i])+'\n')

