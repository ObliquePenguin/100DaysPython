f=open("Other Basic/txttt.txt",'w')
f.write("hello i am ansh    m")
f.close()
g=open("Other Basic/txttt.txt",'r')
text=g.read()
print (text)
g.close()
