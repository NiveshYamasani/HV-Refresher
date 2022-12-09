#car,bike = map(int,input().split())
#print((40*car)+(bike*20))

#carcount = 0
#bikecount = 0
#carcount = int(input("No of cars :"))
#bikecount = int(input("No of bikes :"))
#total = bikecount*20+carcount*40
#print("Total :",total)
##using Input function
product_1 = int(input('quantity of first product :'))
product_2 = int(input('quantity of second product :'))
product_3 = int(input('quantity of third product :'))
# product_4 = int(input('quantity of fourth product :'))
# product_5 = int(input('quantity of fifth product :'))
# price1=int(input("price of product 1 :"))
# price2=int(input("price of product 2 :"))
# price3=int(input("price of product 3 :"))
# if(product_1 <0 or product_2 < 0 or product_3 < 0):
#     print("Zero or Negative value")
# else:
#     total = product_1 * price1 + product_2 * price2 + product_3 * price3
#     print('The total amount is  : %.2f'%total)
 
 
#l = [product_1 ,product_2,product_3]   ##Using the List

#for i in l:   ##using the for loop
#    print(i)
if((product_1<=0) or (product_2<=0) or (product_3<=0)):  #using If_else statements
    print('please enter a positive value')
else:
    print('product quantity with price')
    total = product_1*300 + product_2*400 + product_3*500
    entries = { product_1: 300,product_2 : 400 , product_3 : 500} #using dictionary
    x = open('supermarket.txt','a')    #using files
    print('the amount of all products ')
    print('the amount of all products ',file=x)
    print(entries)
    for i,p in entries.items():
        print(i,p)
        print(i,p,file=x)
    print('the amount that you need to pay is :')
    print('the amount that you need to pay is :',file=x)
    print(total)
    print(total,file=x)
    x.close()





