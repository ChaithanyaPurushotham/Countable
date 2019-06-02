str1=input()
str="javaandjavanadjavajava"
lst=str.split("java")
sub=len(str)-len(lst)
count=int(sub/len(str1))
print(count)