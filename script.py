fp=open("Chat.txt","r")
a=fp.read()
#names=[]
name1=""
lines=a.split("\n")
line1=lines[0]
name1=line1.split("-")[1:]
name1="-".join(name1)
name1=name1.split(":")[0].strip()
for line in lines:
	#print line
	
	name=line.split("-")[1:]
	name="-".join(name)
	name=name.split(":")[0].strip()

	word=line.split(":")[2:]
	word=":".join(word).strip()
	clas=""
	if (name==name1):
		clas="b"
	else:
		clas="c"
	print "<li class=\"" + clas + "\"><span class=\"" + clas + "\">" + word + "</span></li>"