import re
import csv
import time
import psutil
start = time.time()
#reading textfile to be converted
file1 = open("t8.shakespeare.txt","r")
data =file1.read()
#reading csv file
words = {}
with open("french_dictionary.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for i in reader_variable:
        words[i[0]] = [i[1],0]
temp=[]
for j in re.split(r'(\W)',data):
    if j.lower() in words:
        words[j.lower()][1] = words[j.lower()][1]+1
        if(j.islower()):
            temp.append(words[j][0])
        elif(j.isupper()):
            temp.append(words[j.lower()][0].upper())
        elif(j[0].isupper()):
            temp.append(words[j.lower()][0][0].upper() + words[j.lower()][0][1:])
    else:
        temp.append(j)
temp = "".join(temp)
f = open(" t8.shakespeare.translated.txt", "w")
f.write(temp)
f.close()
temp = ""
header = ["English","French","Frequency"]
with open('frequency.csv', 'w',newline='') as f2:
    freq = csv.writer(f2)
    freq.writerow(header)
    for i in words:
        freq.writerow([i,words[i][0],words[i][1]])
words.clear()
endtime = time.time()
print(endtime-start)
print(f"Memory used: {psutil.Process().memory_info().rss / (1024 * 1024)} MB")
