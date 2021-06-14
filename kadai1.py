index={}
with open("morph.txt", encoding="utf-8") as f:
    for line in f:
    	line_first=line.split()
    	if line_first[0] not in index:
    		index[line_first[0]]=1
    	else:
    		index[line_first[0]]+=1
with open("tf1.txt", "w", encoding="utf-8") as f2:
	for i in index:
		f2.write(i + ": " + str(index[i])+'\n')

