import math
import os
import glob
import datetime

start = datetime.datetime.now()

inv = dict()
numlist = list()
with open("inv.txt", encoding="utf-8") as f:
    for line in f:
        tango = line.split('\t')
        for value in tango[1].split(","):
            if value == '\n':
                continue
            id = value.split(':')[0]
            time = value.split(':')[1]
            if id in inv:
                inv[id][tango[0]] = time
            else:
                inv[id] = {tango[0]: time}

f = open('doc_sim_op1.txt', mode='w', encoding='utf-8')
veclist = dict()
for i in range(100):
    for key, value in inv[str(i)].items():
        if i in veclist:
            veclist[i] += int(value) * int(value)
        else:
            veclist[i] = int(value) * int(value)
    veclist[i] = math.sqrt(veclist[i])

files = glob.glob("fp2_win/data/wiki/*.txt")
if not files:
    print("ファイルのリストが⾒つかりません")
    exit()
files.sort()
filenames = list()
for file in files:
    filename = os.path.basename(file)
    filenames.append(filename.split('.')[0])
line = ''
for i in range(100):
    if i == 0:
        line = str(filenames[i])
    line += ',' + str(filenames[i])
f.write(line + '\n')
line = ''
for id in range(100):
    for cpr in range(100):
        num_1 = 0
        num_2 = 0
        num_2 = veclist[id] * veclist[cpr]
        for key, value in inv[str(id)].items():
            if key in inv[str(cpr)]:
                num_1 += int(value) * int(inv[str(cpr)][key])
        temp = num_1 / num_2
        if cpr == 0:
            line = str(temp)
            continue
        line += ',' + str(temp)
    f.write(line + '\n')
f.close()
end = datetime.datetime.now()
print('run time :', end - start)
# run time : 0:00:02.942897
