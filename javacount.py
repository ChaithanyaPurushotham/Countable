str = "javaandjavaandjavajava"
word=0
for i in range(len(str)):
    if(str[i]=="j"):
        if(str[i+1]+str[i+2],str[i+3]=="ava"):
            word=word+1
print("Number of java word in given string is ",word)
