f=open("stoi.txt","r+")
str1=f.read()
f.seek(0)
f.write(int(str1))
