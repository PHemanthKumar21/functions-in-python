#default arguments
'''def Grocery(item,price):
    print("item is %s" %item)                   #OUTPUT:item is rice
    print("price is %.2f" %price)                   #   price is 15000.00
Grocery("rice",15000)'''


'''def Grocery(item="sugar",price=100):            #OUTPUT:item is sugar
    print("item is %s" %item)                        #     price is 100.00
    print("price is %.2f" %price)
Grocery()'''



'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''


'''def Grocery(item="sugar",price):
    print("item is %s" %item)
    print("price is %.2f" %price)   #ERROR
Grocery(500)'''




#cake,price,quantity
def Bakery(cake,price=1000,quantity="1kg"):  
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Bakery("black forest")

'''OUTPUT:cake is black forest
       price is 1000.00
       quantity is 1kg'''



'''def Bakery(cake="black forest",price=1000,quantity="1kg"):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Bakery()'''


'''def Bakery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("quantity is %s" %quantity)
Bakery("chocolate cake",800,"2kg")'''


'''def Bakery(cake="black forest",price,quantity="1kg"):
    print("cake is %s" %cake)                          
    print("price is %.2f" %price)            #ERROR
    print("quantity is %s" %quantity)
Bakery(1000)'''
