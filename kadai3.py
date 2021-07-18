import os
import glob
import unicodedata
import MeCab
index={}

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
				else:#名詞を確認
					line_cut=line_first[1].split(',')
					if line_cut[0]=="名詞":
						if line_first[0] not in index:
							index[line_first[0]]={}
							index[line_first[0]][j]=1
						else:
							if j not in index[line_first[0]]:
								index[line_first[0]][j]=1
							else:
								index[line_first[0]][j]+=1



with open("inv_seireishi.txt", "w", encoding="utf-8") as f2:
	for i in index:
		f2.write(format(i,"<20"))
		f2.write(",".join(str(j)+":"+str(index[i][j]) for j in index[i]))
		f2.write("\n")


