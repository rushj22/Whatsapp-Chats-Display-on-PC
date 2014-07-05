import sys,webbrowser,os

d=sys.argv[1]

#storing chat file location in a variable
for file in os.listdir(sys.argv[1]):
	if file.endswith(".txt"):
		d=os.path.join(d,file)

#file reading
fp=open(d,"r+")
a=fp.read()

template='''<html>
<head>
<title>Whatsapp Chats Display on PC</title>
</head>
<style>
li.a	{
		list-style-type:none;
		text-align:right;
		margin-bottom:15px;
	}
li 		{marhin-bottom:15px;}

li.b 	{
		list-style-type:none;
		text-align:left;
		margin-bottom:15px;
		
		
	}
span.a	{
		box-shadow: 0px 0px 2px black;
    	border-radius: 5px;
		background-color:rgb(214,248,183);
		padding:6px;
	}
span.b  {
		padding-left:10px;
		box-shadow: 0px 0px 2px;
    	border-radius: 5px;		
		padding:6px;	
}

li.date	{
		list-style-type:none;
    	border:1px solid; 
		text-align:center;
		padding:2px;
		margin-bottom:15px;
		

}

span.time	{
		font-size:10;
		margin-left:6px;
}

</style>
<body>
<ul>
%s
</ul>
</body>
</html>'''

line1=a.split("\n")[0]
lines=a.split("\n")

#extract name of first person
name1=line1.split("-")[1:]
name1="-".join(name1)
name1=name1.split(":")[0].strip()

date1=""
msg=""
lis=""

#traversing chat line-wise
for line in lines:

	#extracting message
	word=line.split(":")[2:]
	word=":".join(word).strip()

	#extracting name of person
	name=line.split("-")[1:]
	name="-".join(name)
	name=name.split(":")[0].strip()
	
	#class allotment for css
	if (name==name1):
		clas="a"
	else:
		clas="b"

	#extracting time
	time=line.split(",")[1:]
	time=",".join(time)
	time=time.split("-")[0].strip()

	#checking if continued message in new line
	try:
		if(time[-2:]!="AM" and time[-2:]!="PM"):
			msg=msg+"<br/>"+line
			continue
	except:
		msg=msg+"<br/>"+line
		continue
	
	#extracting date of message and checking if date is new
	date=line.split(",")[0]
	if (date!=date1):
 		date1=date
 		lis+='<li class=%s>%s</li>'%("date",date)
	
	#checking for image or video as message

	img=line.split(":")[2:]
	img=":".join(img).strip()
	img=img.split(" ")[0].strip()
	#print img
	imgtag=""
	
	if (img[:3]=="IMG" and img [-4:]==".jpg"): #terminal numbers not included
		imgtag='<img src='+os.path.join(sys.argv[1],img)+' width="250" border="1">'
		imgtag='<a href='+os.path.join(sys.argv[1],img)+'>'+imgtag+'</a>'
		#print word

	if (img[:3]=="VID" and img [-4:]==".mp4"):
		imgtag='<video width="320" height="240" controls> \
  				<source src='+os.path.join(sys.argv[1],img)+' type="video/mp4">\
  				</video>'

	#adding message to list depending on what type of message is it

	#for multiline message
	if (msg!=""):
		lis+='<li class=%s><span class=%s>%s<span class="time">%s</span></span></li>'%(clas,clas,msg,time)
		
	msg=""

	#for image or video message
	if (imgtag!=""):
		lis+='<li class=%s>%s<span class="time">%s</span></li>'%(clas,imgtag,time)
		
	#for one-line message
	if (msg=="" and imgtag==""):
		lis+='<li class=%s><span class=%s>%s<span class="time">%s</span></span></li>'%(clas,clas,word,time)

#creating html file with require display properties of message
output=template % lis
fp=open("output.html","w")
fp.write(output)
webbrowser.open_new_tab("file://"+os.getcwd()+"/output.html")
fp.close()
