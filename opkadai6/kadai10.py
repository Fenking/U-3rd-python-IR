import networkx as nx
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

G = nx.Graph()

matrix = []
with open("doc_simc.txt", encoding="utf-8") as f:
    names = f.readline().strip().split(",")
    for line in f:
        data = []
        values = line.strip().split(",")
        for value in values:
            data.append(float(value))
        matrix.append(data)

for row, values in enumerate(matrix):
    for col, value in enumerate(values):
        if(value>=0.35):#各線が見える値
            G.add_edge(names[row],names[col])
            G.edges[names[row],names[col]]["weight"]=value


city={}
with open("citys.txt", encoding="utf-8") as f2:
    for line in f2:
        words=line.split()
        city[words[0]]=words[1]

n_color=[]
for node in nx.nodes(G):
    if(city[node]=="h"):#東北・北海道
        n_color.append("yellow")
    elif(city[node]=="t"):#関東
        n_color.append("green")
    elif(city[node]=="c"):#中部
        n_color.append("orange")
    elif(city[node]=="k"):#関西
        n_color.append("blue")
    elif(city[node]=="s"):#西日本(中国・九州)
        n_color.append("red")

n_size=[]#节点大小
for name,neighbors in G.adjacency():
    n_size.append(len(neighbors)*80)


plt.figure(figsize=(9.5, 9.5))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
pos = nx.spring_layout(G, k=1.5)
nx.draw_networkx_nodes(G, pos, node_size=n_size, node_color=n_color, alpha=0.5)
e_width = [G[u][v]["weight"] for u, v in G.edges]
nx.draw_networkx_edges(G, pos, edge_color="grey", alpha=1)
nx.draw_networkx_labels(G, pos, font_family="sans-serif", font_size=10)
plt.axis("off")
plt.show()


