
days = ['月','月','火','水','木','金','金']

days.remove('月')  # 重複している月を1つ削除
days.remove('金')  # 重複している金を1つ削除

j = 0
for cd in ['日', '土']:
    days.insert(j, cd)  # 指定した位置に曜日を追加
    j += 6

print(days)