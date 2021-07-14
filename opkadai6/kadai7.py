import os
import glob
import unicodedata
import MeCab
import math
index={}
doc_math=[]
value_math=0

files = glob.glob("seireishi/*.txt")

if not files:
    print("ファイルのリストが見つかりません")
    exit()

files.sort()

for j,file in enumerate(files):
	m = MeCab.Tagger()
	with open(file, encoding="utf-8") as f:
		for line in f:
			terms = m.parse(line)
			for i in terms.splitlines():
				line_first=i.split()
				if line_first[0]=="EOS":
					pass
				else:
					line_cut=line_first[1].split(',')
					if line_cut[0]=="名詞":
						if line_first[0] not in index:
							index[line_first[0]]=1
						else:
							index[line_first[0]]+=1
	for value in index.values():
		value_math+=value**2
	doc_math.append(math.sqrt(value_math))
	value_math=0
	index={}





with open("doc_datac.txt", "w", encoding="utf-8") as f:
	for i,file in enumerate(files):
		filename = os.path.basename(file)
		filename = unicodedata.normalize("NFC", filename)
		filename = os.path.splitext(filename)
		f.write(str(i)+"\t"+str(filename[0])+"\t"+str(doc_math[i])+"\n")
    
