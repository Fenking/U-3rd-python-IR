import os
import glob
import unicodedata

files = glob.glob("seireishi/*.txt")

if not files:
    print("ファイルのリストが見つかりません")
    exit()

files.sort()

with open("doc_id_city.txt", "w", encoding="utf-8") as f:
	for i,file in enumerate(files):
		filename = os.path.basename(file)
		filename = unicodedata.normalize("NFC", filename)
		filename = os.path.splitext(filename)
		f.write(str(i)+"\t"+str(filename[0])+"\n")
    