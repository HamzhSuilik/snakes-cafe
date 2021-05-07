print (""" 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

menu = {'Wings':0 ,'Cookies':0,'Spring Rolls':0,'Salmon':0,'Steak':0,'Meat Tornado':0, 'A Literal Garden': 0, 'Ice Cream':0 ,'Cake':0,'Pie':0,'Coffee':0,'Tea':0,'Unicorn Tears':0}

def show_list():
    list = ''
    for i in menu :
        if menu[i] :
            list = list + str(menu[i]) + ' order of ' + i + ' have been added to your meal' + '\n'
    print(list)

order = input()

while (order != 'quit') :
    check = True
    for i in menu :
        if order == i :
            check = False
            menu[i] = menu[i] + 1
            show_list()
            break
    if check :
        print ('Invalid input , please try again')

    order = input()



quit()