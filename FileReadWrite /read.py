f=open('FileReadWrite /test1.txt','r')
print(f.name)
print(f.mode)
f.close()
print(f.closed)

with open('FileReadWrite /test1.txt','r') as f:
    fcontents=f.read()
    print(fcontents)
print("---------------------------------------------------------------------")

with open('FileReadWrite /test1.txt','r') as f:
    fcontents=f.readlines()
    print(fcontents)
    print("---------------------------------------------------------------------")

with open('FileReadWrite /test1.txt','r') as f:
    fcontents=f.readline()
    print(fcontents)
print("---------------------------------------------------------------------")

with open('FileReadWrite /test1.txt','r') as f:
    for line in f:
        print(line,end=' ')
print("---------------------------------------------------------------------")


with open('FileReadWrite /test1.txt','r') as f:
    sizetoread=100
    fcontents=f.read(sizetoread)
    while len(fcontents)>0:
        print(fcontents,end=' ')
        print(f.tell())
        fcontents=f.read(sizetoread)

#f.seek(0)----> bring the position to start