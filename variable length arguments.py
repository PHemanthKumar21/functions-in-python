#variable length arguments:-variable length arguments are automatically stores in tuple and we use star aruguments.
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[4,6,8,9,0]
check(*b)
c={6,7,8,9,10}
check(*c)
d={"name":"hemanth","city":"vja"}
check(*d)'''





def check1(*a):
    d=2 #creating variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,4,5,6,7)
check1(1,2,3,4.5,2.5)
check1(3,4,2,5,3.6,2.4,"hemanth")





