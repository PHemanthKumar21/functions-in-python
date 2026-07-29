#kwargs(**)

def check(**a):
    print(a)
    print(type(a))

check()
details={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
check(**details)

def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
check(**details)


#both * and ** usage
'''def final(*a,**b):
     d=3
     print(a)
     print(b)
     print(type(a))
     print(type(b))
     for i in a:
         d=d+1
         print(d)
     for i,j in b.items():
         print("key is",i)
         print("value is",j)
final()
data=(4,6,7,9,9)
final(*data)
details={"idnos":[10,20,30],"names":["sai","siva","ravi"],"status":["p","a","p"]}
final(**details)
final(*data,**details)'''

#max, min, sum()
'''print(max(3,6,8,9,2,23))
print(min(7,3,21,5,8,4))'''
'''a=3,4,5,6,9
print(sum(a))'''

#marks analysis report
'''students=int(input("no.of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student {i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print(".........marks report........")
print("total students",students)
print("height marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average",sum(marks)/students)'''
         


