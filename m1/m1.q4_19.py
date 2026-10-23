a = [1, 2, 3, 4]
id_a = id(a) #id()関数はオプジェクトaのidを取得し、id_aに代入
b = a.copy() #aのcopyを作成し、bに代入する（aとは別のオプジェクトとなる）
id_b = id(b) #bのidを取得し、id_dに代入
if id_a == id_b:
    result = 'A'
elif id(a) == id_b: #False: aとbは別のオプジェクトなので、idも異なる
    result = 'B'
elif id_a == id(a): #Ture: id_aにはid(a)の戻り値が代入されている
    result = 'C'
else: #上記の条件のいずれかがTrueなるため実行されない
    result = 'D'
print(result)

"""note
pythonのid()関数は、オプジェクトを識別するための整数値(int)を返す
"""