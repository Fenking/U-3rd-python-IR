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

query_str = input("検索語を入力して下さい: ")

query_terms = query_str.split()
for term in query_terms:
    TF=0
    IDF=0
    for i in inv[term]:
        TF=inv[term][i]/len(query_terms)#TFを(文書内出現数/文書の全索引語出現数)　TF是(文章内出现次数/此文章内所有索引词的出现次数)
        IDF=math.log(n_docs/len(inv[term]))#IDFをlog(全文書数/出現文書数)　IDF是log(文章总数/此单词出现的文章数目)
        # print(tf,idf)
        doc[i].score+=TF*IDF

doc_down=[]
for i in range(n_docs):
    message="{}: {}"
    if not doc[i].score==0.0:
        doc_down.append(doc[i])
        # print(message.format("doc_"+str(doc[i].get_id()),doc[i].get_score()))

doc_down.sort(key=lambda s: s.get_score(),reverse=True)
for i in range(len(doc_down)):
    print(message.format(doc_down[i].get_name(),doc_down[i].get_score()))
