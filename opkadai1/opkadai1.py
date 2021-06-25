import math
import time

time_start=time.time()

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
# for i in range(n_docs):
#     doc.append(Document(i, "doc_" + str(i), 0.0))

with open("doc_data.txt", encoding="utf-8") as f3:
    for line in f3:
        line_data=line.split()
        doc[int(line_data[0])].vec_length=line_data[2]

doc_cos= [[0 for i in range(100)] for i in range(100)]#cos用


for a in range(n_docs):
    for b in range(a,n_docs):
        dot_product=0
        for term in inv:
            tf_a=0
            tf_b=0
            for j in inv[term]:
                if j==a:
                    tf_a+=inv[term][j]
                if j==b:
                    tf_b+=inv[term][j]
            if tf_a!=0 and tf_b!=0:
                dot_product+=tf_a*tf_b
        #dot_product+=tf_a
        # print(float(doc[a].get_length())*math.sqrt(len(query_terms)))
        length_a=float(doc[a].get_length())
        length_b=float(doc[b].get_length())
        doc_cos[a][b]=dot_product/(length_a*length_b)


with open("doc_sim2.txt", "w", encoding="utf-8") as f4:
    f4.write(",".join(str(j.get_name()) for j in doc))
    f4.write("\n")
    for i in range(n_docs):
        f4.write(",".join(str(j) for j in doc_cos[i]))
        if i!=99:
            f4.write("\n")

time_end=time.time()
print('time cost of opkadai1',time_end-time_start,'s')