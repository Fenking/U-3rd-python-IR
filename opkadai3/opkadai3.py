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
# n_docs = 5    # 训练用

with open("inv.txt", encoding="utf-8") as f:
# with open("inv2.txt", encoding="utf-8") as f:  # 训练用
    for line in f:
        index=line.split()
        inv[index[0]]={}
        word=index[1].split(",")
        for i in word:
            i_dict=i.split(":")
            inv[index[0]][int(i_dict[0])]=int(i_dict[1])

with open("doc_id_name.txt", encoding="utf-8") as f2:
# with open("doc_id_name2.txt", encoding="utf-8") as f2:  # 训练用
    for line in f2:
        line_cut=line.split()
        doc.append(Document(line_cut[0],line_cut[1],0.0))


query_str = input("検索語を入力して下さい: ")

query_terms = query_str.split()
for term in query_terms:
    for i in inv[term]:
        doc[i].score+=1/len(query_terms)

doc_down=[]
for i in range(n_docs):
    if not doc[i].score==0.0:
        doc_down.append(doc[i])

message="{}: {}"
doc_down.sort(key=lambda s: s.get_score(),reverse=True)
for i in range(len(doc_down)):
    check={}
    print(message.format(doc_down[i].get_name(),doc_down[i].get_score()))
    with open("wiki/"+doc_down[i].get_name()+".txt", encoding="utf-8") as f:
    # with open("wiki2/"+doc_down[i].get_name()+".txt", encoding="utf-8") as f:  # 训练用
        for i,line in enumerate(f):
            for word in query_terms:
                if word in line and i not in check:
                    check[i]=line.strip()
    for i in check:
        print("第{}行:{}".format(i+1,str(check[i])))
    print("\n")

