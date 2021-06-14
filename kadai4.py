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

# (1)転置索引のファイルinv.txtを読み込み，辞書型変数invに格納
with open("inv.txt", encoding="utf-8") as f:
    for line in f:
        index=line.split()
        inv[index[0]]={}
        word=index[1].split(",")
        for i in word:
            i_dict=i.split(":")
            inv[index[0]][int(i_dict[0])]=int(i_dict[1])

# (2)文書オブジェクトのリストを作成し，初期化
for i in range(n_docs):
    # 仮の文書名（doc_文書ID）で文書オブジェクトを生成し，リストに追加
    doc.append(Document(i, "doc_" + str(i), 0.0))

# (3)ユーザによる検索語の入力
query_str = input("検索語を入力して下さい: ")

# (4)検索語ごとに転置索引を参照し，文書スコアを計算
query_terms = query_str.split()
for term in query_terms:
    for i in inv[term]:
        doc[i].score+=1/len(query_terms)


# (5)検索結果の出力
for i in range(n_docs):
    message="{}: {}"
    if not doc[i].score==0.0:
        print(message.format("doc_"+str(doc[i].get_id()),doc[i].get_score()))
