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

#query_str = input("検索語を入力して下さい: ")

#query_terms = query_str.split()
for a in range(n_docs):
    for b in range(n_docs):
        dot_product=0
        for term in inv:
            tf_a=0
            tf_b=0
            for j in inv[term]:
                #a==bの場合、先にifを実行するので、elifはなし、判断は0になる
                #a==b的时候因为会先执行第一个if 导致elif不会被执行 使得a!=0但b==0 所有要先判断来防止
                #我tm个傻逼直接用俩if不写elif不就得了 前面写一堆废话
                # if j==a and j==b:
                #     tf_a+=inv[term][j]
                #     tf_b+=inv[term][j]
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

# for i in range(n_docs):
#     print(doc_cos[i])
with open("doc_sim.txt", "w", encoding="utf-8") as f4:
    f4.write(",".join(str(j.get_name()) for j in doc))
    f4.write("\n")
    for i in range(n_docs):
        f4.write(",".join(str(j) for j in doc_cos[i]))
        if i!=99:
            f4.write("\n")

time_end=time.time()
print('time cost of kadai9',time_end-time_start,'s')