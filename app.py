import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)   # 做出progressbar型別的一個物件 bar

# 物件的第一個字是大寫，所以 ProgressBar 是物件，只要寫 Class（類別）就能自己創造一個型別

with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count) # 使用 bar 這個物件的 update function
print("檔案讀取完了，總共有", len(data), "筆資料")    # function 的第一個字會是小寫，寫在class裡的function，會被稱呼為method，就不再叫它function

print(data[0])

sum_len = 0
for d in data:
    sum_len += len(d)

print("留言長度平均是", sum_len / len(data))

sum_len100 = 0
for h in data:
    if len(h) > 100:
        sum_len100 += 1

print("留言長度大於100的有", sum_len100 ) 


# 文字計數
start_time = time.time()
wc = {} #word_count
for d in data:
    words = d.split() # 如果留空的時候代表空字串的意思
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增 word 到 wc 裡面

for word in wc: 
    if wc[word] > 1000000:
        print(word, wc[word])
end_time = time.time()

print("花了", end_time - start_time, "seconds")
print(len(wc)) 

while True:
    word = input("請問你要查詢什麼字？")
    if word == "q":
        break
    if word in wc:
        print(word, "出現的次數為", wc[word], "次")
    else:
        print("這個字沒有在留言裡面喔")

print("感謝您本查詢功能")



