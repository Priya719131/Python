with open('test2.txt','w') as f:
    f.write('test')
    f.seek(0)
    f.write('hello')