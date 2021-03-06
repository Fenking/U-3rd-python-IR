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
doc = []        # 文書オブジェクトのリスト
n_docs = 100    # 文書数


with open("inv_location.txt", encoding="utf-8") as f:
	for line in f:
		index=line.split(' ',1)
		inv[index[0]]={}
		word=index[1].strip().split(";")
		for i in word:
			i_dict=i.split(":")
			i_dict_lc=i_dict[1].strip("[").strip("]").split(",")
			inv[index[0]][int(i_dict[0])]=[]
			inv[index[0]][int(i_dict[0])].append(int(i_dict_lc[0].strip()))
			for dicts in i_dict_lc[1:]:
				inv[index[0]][int(i_dict[0])].append(int(dicts))
# print(",\n".join(str(i)+":"+str(inv[i]) for i in inv))

with open("doc_id_name.txt", encoding="utf-8") as f2:
    for line in f2:
        line_cut=line.split()
        doc.append(Document(line_cut[0],line_cut[1],0.0))


query_str = input("検索語を入力して下さい: ")

query_terms = query_str.split()
for term in query_terms:
	TF=0
	IDF=0
	if term in inv:
		for i in inv[term]:
			TF=inv[term][i][0]/len(query_terms)
			IDF=math.log(n_docs/len(inv[term]))
			doc[i].score+=TF*IDF
	else:
		for s in range(len(term)):
			if term[:s+1] in inv and term[s+1:] in inv:
				for i in inv[term[:s+1]]:
					for j in inv[term[:s+1]][i][1:]:
						if i in inv[term[s+1:]]:
							for k in inv[term[s+1:]][i][1:]:
								if j+1==k:
									TF=inv[term[:s+1]][i][0]/len(query_terms)
									IDF=math.log(n_docs/len(inv[term[:s+1]]))
									doc[i].score+=TF*IDF
									break




doc_down=[]
for i in range(n_docs):
    if not doc[i].score==0.0:
        doc_down.append(doc[i])

message="{}: {:.2f}"
doc_down.sort(key=lambda s: s.get_score(),reverse=True)

if doc_down==[]:
	print("該当なし")
else:
	for i in range(len(doc_down)):
		check={}
		print(message.format(doc_down[i].get_name(),doc_down[i].get_score()))
		with open("wiki/"+doc_down[i].get_name()+".txt", encoding="utf-8") as f:
			for i,line in enumerate(f):
				for word in query_terms:
					if word in line and i not in check:
						check[i]=line.strip()
		for i in check:
			print("第{}行:{}".format(i+1,str(check[i])))
			print("\n")
