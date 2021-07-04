import os
import glob
import unicodedata
import MeCab
index={}

files = glob.glob("wiki/*.txt")

if not files:
    print("ファイルのリストが見つかりません")
    exit()

files.sort()

for j,file in enumerate(files):
	m = MeCab.Tagger()
	with open(file, encoding="utf-8") as f:
		for rank,line in enumerate(f):
			terms = m.parse(line)
			for num,i in enumerate(terms.splitlines()):
				line_first=i.split()
				if line_first[0]=="EOS":
					pass
				elif line_first[0] not in index:
					index[line_first[0]]={}
					index[line_first[0]][j]=[]
					index[line_first[0]][j].append(1)
					index[line_first[0]][j].append({rank:num})
				else:
					if j not in index[line_first[0]]:
						index[line_first[0]][j]=[]
						index[line_first[0]][j].append(1)
						index[line_first[0]][j].append({rank:num})
					else:
						index[line_first[0]][j][0]+=1
						index[line_first[0]][j].append({rank:num})

#こちらのパソコンは外国語対応するため、txtファイル名前は日本語文字化けと示している。例岩坂 名奈=>娾嶁柤撧
#そのためこちら転置索引の順番、認識された単語について違いがあるかもしれません。
#結果の手順はTA／教授での出力結果を基本としてお願いします。
#また、TAさんチェックする際に、正しい順番のinv.txtファイルをメールで発送していいでしょうか、次の課題に使用するため


with open("inv_location.txt", "w", encoding="utf-8") as f2:
	for i in index:
		f2.write(format(i,"<25"))
		f2.write(";".join(str(j)+"="+str(index[i][j]).strip() for j in index[i]))#改变读取样式
		f2.write("\n")


