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


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        #进栈
        self.stack.append(data)

    def pop(self):
        #出栈
        return self.stack.pop()

    def gettop(self):
        #栈顶
        return self.stack[-1]


inv = {}        # 転置索引を格納する辞書型変数
doc = []        # 文書オブジェクトのリスト
n_docs = 100    # 文書数
stack = Stack()


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

with open("doc_data.txt", encoding="utf-8") as f3:
    for line in f3:
        line_data=line.split()
        doc[int(line_data[0])].vec_length=line_data[2]
        

query_str = input("検索語を入力して下さい(スペース空け): ")


def logical(q_terms):
    if "(" in q_terms and ")" in q_terms:
        q_terms.remove("(")
        q_terms.remove(")")
    # print("q_terms",q_terms)
    if "NOT" in q_terms:
        words=[]
        for word in q_terms:
            if word!="NOT" and isinstance(word,list):
                words.append(word)
            elif word!="NOT":
                word_keys=list(inv[word].keys())
                words.append(word_keys)
        word_not=list(set(words[0]).difference(*words[1:]))
        return word_not


    if "OR" in q_terms:
        words=[]
        for word in q_terms:
            if word!="OR" and isinstance(word,list):
                words.append(word)
            elif word!="OR":
                word_keys=list(inv[word].keys())
                words.append(word_keys)
        word_or=list(set(words[0]).union(*words[1:]))
        return word_or


    if "AND" in q_terms:
        words=[]
        for word in q_terms:
            if word!="AND" and isinstance(word,list):
                words.append(word)
            elif word!="AND":
                word_keys=list(inv[word].keys())
                words.append(word_keys)
        word_and=list(set(words[0]).intersection(*words[1:]))
        return word_and

    elif "NOT" not in q_terms and "OR" not in q_terms and "AND" not in q_terms:
        for word in q_terms:
            if isinstance(word,list):
                word_keys=word
            elif isinstance(word,str):
                word_keys=list(inv[word].keys())
        return word_keys


query_terms = query_str.split()
for word in query_terms:
    stack.push(word)
    if word==")":
        l=[]
        while True:
            l.append(stack.pop())
            if l[-1]=="(":
                l.reverse()
                # print("l2",l)
                l3=logical(l)
                stack.push(l3)
                # print("l3",l3)
                break
lend=[]
while True:
    lend.append(stack.pop())
    if len(stack.stack)==0:
        lend.reverse()
        # print("lend2",lend)
        lend3=logical(lend)
        # print("lend3",lend3)
        break


query_t=[]
query_terms = query_str.split()
if "(" in query_terms and ")" in query_terms:
    query_terms.remove("(")
    query_terms.remove(")")
for word in query_terms:
    if word in inv:
        query_t.append(word)


for i in lend3:
    dot_product=0
    for term in query_terms:
        if term in inv:
            tf=0
            for j in inv[term]:
                if j==i:
                    tf+=inv[term][j]
            dot_product+=tf
    score=dot_product/(float(doc[i].get_length())*math.sqrt(len(query_t)))
    doc[i].set_score(score)


doc_down=[]
for i in range(n_docs):
    message="{}: {}"
    if not doc[i].score==0.0:
        doc_down.append(doc[i])


doc_down.sort(key=lambda s: s.get_score(),reverse=True)
for i in range(len(doc_down)):
    print(message.format(doc_down[i].get_name(),doc_down[i].get_score()))
