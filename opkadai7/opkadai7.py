import os
import glob
import unicodedata
import MeCab
import re

class Document:
    def __init__(self, doc_id, doc_name, vec_length):
        self.doc_id = doc_id            # 文書ID
        self.doc_name = doc_name        # 文書名
        self.vec_length = vec_length    # 文書ベクトル長
        self.score = 0.0                # 文書のスコア（検索時に計算）

    def get_id(self):
        return self.doc_id

    def get_name(self):
        return self.doc_name

    def get_length(self):
        return self.vec_length

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score


inv = {}        # 転置索引を格納する辞書型変数
doc = []        # 文書オブジェクトのリスト
n_docs = 100    # 文書数

with open("inv.txt", encoding="utf-8") as f:
    for line in f:
        index=line.split()
        inv[index[0]]={}
        word=index[1].split(",")
        for i in word:
            i_dict=i.split(":")
            inv[index[0]][int(i_dict[0])]=int(i_dict[1])

with open("doc_id_name.txt", encoding="utf-8") as f2:
    for line in f2:
        line_cut=line.split()
        doc.append(Document(line_cut[0],line_cut[1],0.0))

inv_str=input("追加したい文書を入力してください(.txtは不要、スペースで空け)：")
inv_str=re.sub('\s',' ',inv_str)
inv_add=inv_str.split(" ")

for j,name in enumerate(inv_add):
    doc.append(Document(n_docs+j,name,0.0))
    m = MeCab.Tagger()
    with open(name+".txt", encoding="utf-8") as fa:
        for line in fa:
            terms = m.parse(line)
            for i in terms.splitlines():
                line_first=i.split()
                if line_first[0]=="EOS":
                    pass
                else:
                    line_cut=line_first[1].split(',')
                    if line_cut[0]=="名詞":
                        if line_first[0] not in inv:
                            inv[line_first[0]]={}
                            inv[line_first[0]][n_docs+j]=1
                            # print(0,line_first[0],n_docs+j)
                        else:
                            if n_docs+j not in inv[line_first[0]]:
                                inv[line_first[0]][n_docs+j]=1
                                # print(1,line_first[0],n_docs+j)
                            else:
                                inv[line_first[0]][n_docs+j]+=1
                                # print(2,line_first[0],n_docs+j)

query_str = input("検索語を入力して下さい: ")

query_terms = query_str.split()
for term in query_terms:
    for i in inv[term]:
        doc[i].score+=1/len(query_terms)

doc_down=[]
for i in range(n_docs+len(inv_add)):
    message="{}: {}"
    if not doc[i].score==0.0:
        doc_down.append(doc[i])

doc_down.sort(key=lambda s: s.get_score(),reverse=True)
for i in range(len(doc_down)):
    print(message.format(doc_down[i].get_name(),doc_down[i].get_score()))


with open("inv2.txt", "w", encoding="utf-8") as fi:
	for i in inv:
		fi.write(format(i,"<20"))
		fi.write(",".join(str(j)+":"+str(inv[i][j]) for j in inv[i]))
		fi.write("\n")

with open("doc_id_name2.txt", "w", encoding="utf-8") as fd:
    for i,d in enumerate(doc):
        fd.write(str(i)+"\t"+doc[i].get_name()+"\n")