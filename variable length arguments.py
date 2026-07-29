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
check(*d)

OUPUT:
()
<class 'tuple'>
(2, 3, 4, 5, 6, 7)
<class 'tuple'>
(4, 6, 8, 9, 0)
<class 'tuple'>
(6, 7, 8, 9, 10)
<class 'tuple'>
('name', 'city')
<class 'tuple'>'''
