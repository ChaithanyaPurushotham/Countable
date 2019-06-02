import sys
str1=sys.argv[1]
str="javaandjavanadjavajava"
lst=str.split("java")
sub=len(str)-len(lst)
count=int(sub/len(str1))
print(count)