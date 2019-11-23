def getdate():
    import datetime
    time=datetime.datetime.now()
    return time

print("Whom do you want to log or retrieve")
name=int(input("Press 1 for harry "
               "2 for rohan "
               "3 for hamad"+"\n"))

print("Press 1 for log & 2 for retrieve")
take = int(input())

if name==1 and take==1:
    j=str(input("enter what you eat"+"\n"))
    with open("harry.txt","a") as h:
        h.write(str([str(getdate())])+"="+j+"\n")
        print("done")
elif name==1 and take==2:
    with open("harry.txt") as h:
        a = h.read()
        print(a)
elif name==2 and take==1:
    j = str(input("enter what you eat"+"\n"))
    with open("rohan.txt","a") as r:
        r.write(str([str(getdate())])+"="+j)
        print("done")
elif name==2 and take==2:
    with open("rohan.txt") as r:
        a=r.read()
        print(a)
elif name==3 and take==1:
    j = str(input("enter what you eat","\n"))
    with open("hamad.txt","a") as d:
        d.write(str([str(getdate())]) + "=" + j)
        print("done")
else:
    with open("hamad.txt") as d:
        a=d.read()
        print(a)





