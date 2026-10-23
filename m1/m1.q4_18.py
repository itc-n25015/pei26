phrase = "PythonProgramming"
list_p = []
for p in phrase: #phraseの一文字ずつを繰り返しでチャック
    if p not in list_p: #チャック文字がlist_pにない場合
        list_p.append(p) #pをlis_pに追加(append)する
print(len(phrase) - len(list_p)) 




