# index={"a":{0:1,1:2,2:3},"b":{0:2,1:3,2:4},"c":{0:3,1:4,2:5}}
# index["a"][0]=10
# # print(index["a"][0])
# for j,file in enumerate(index):
# 	print(j)
# index["a"][3]=2
# print(index)

# a2="123"
# a3=a2.split(",")
# print(a3)


import math

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
docx = []        # 文書オブジェクトのリスト
n_docs = 100    # 文書数
doc2=[]
doc=[]

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

with open("doc_id_name.txt", encoding="utf-8") as f:
	# count=len(f2.readlines())
	# print(count)
	for i in range(100):
		docx.append(doc2)
		for j,line in enumerate(f):
			line_cut=line.split()
			# doc[i].append(Document(line_cut[0],line_cut[1],0.0))
			docx[i].append(j)
			# print(doc[i][j].get_id())
			
for i in range(10):
	print(docx[i][1])
	print("\n")
		


doc_cos= [[0 for i in range(10)] for i in range(10)]
print(doc_cos)

with open("11223344.txt", "w", encoding="utf-8") as f4:
	f4.write(",".join(str(j.get_name()) for j in doc))
	f4.write("111")