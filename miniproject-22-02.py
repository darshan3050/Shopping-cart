pas=('viva123')
import os
clear = lambda: os.system("cls")
clear()
def list_print(content):
      print("                                                       "," +","="*55,"+")
      print("                                                       "," |    ID no     |       Name            |     Cost         |")
      print("                                                       "," +","="*55,"+") 
      for item in content:
            print("                                                       "," |     ",item[0]," "*(6-len(str(item[0]))),"|    "
                      ,item[1]," "*(15-len(str(item[1])))," |    " ,
                      item[2]," "*(10-len(str(item[2])))," |    "  )
      print("                                                       "," +","="*55,"+")

      return
def recipt_print(content):
    clear()
    list_print(cust_cart)
    calculate=0
    for item in cust_cart:
        calculate=calculate+item[2]
    tax=calculate*2.5/100
    disp_tax=str(tax)
    prtax=disp_tax[0:5]
    pr=float(prtax)
    print("                                                       "," |             Sub Total                |     ",calculate," "*(10-len(str(calculate))) ,"|")
    print("                                                       "," +","="*55,"+")
    print("                                                       "," |             CGST                2.5% |    ",disp_tax[0:5]," "*(10-len(str(disp_tax))) ,"|")
    print("                                                       "," |             SGST                2.5% |    ",disp_tax[0:5]," "*(10-len(str(disp_tax))) ,"|")
    print("                                                       "," +","="*55,"+")
    cal_tax=calculate+pr+pr
    cal_str=str(cal_tax)
    pos=cal_str.find('.')+3
    print("                                                       "," |                 Total                |   ",cal_str[0:pos]," "*(10-len(str(cla_str))) ,"|")
    print("                                                       "," +","="*55,"+")
    print('''




                                                                                            THANK YOU FOR SHOPPING WITH OUR STORE

    
                                                ''')  
    
def space_print():
    print('''












        
        ''')

item_list=[[1,"Lays chips",10],[2,"Thums Up",40],[3,"Detol Soap",25],[4,"cheese 200g",100],[5,"T Shirt",250],[6,"Watch",600],[7,"Chicken Nuggets",300],[8,"Ice Creame",240],[9,"PenDrive",400]]                    
cust_cart=[]
while True:
    clear()
    print ('                                                                                            WELCOME TO VIVA SUPER MARKET')
    space_print()
    print('''                  1.Admin login
                  2.customer login
                  3.exit''')
    print('''






    ''')

    a=int(input("                 enter your choice: "))

    clear()

    if (a==1):#admin loop
    
        p=input('''                
        
        



        
                             Enter password   :  ''')

        if(p==pas):
            clear()
            while True: 
                clear()
                print ('                                                                                            WELCOME  ADMIN ')
                space_print()
            
                print('''                      1.view item
                      2.add item
                      3.remove item
                      4.exit ''')
                admin_choice=int(input('''
                      Enter ypor choice:   '''))
                if admin_choice==1:
                    clear()
                    space_print()
                    list_print(item_list)
                    a=(input('''
                    
                    
                      Press Y to continue     :'''))
                    
                        

                      
                elif admin_choice==2:
                     clear()
                     space_print()
                     list_print(item_list)                    
                     prdct_id=len(item_list)+1
                     item_list.append([prdct_id])
                     prdct_name=input("enter product name: ")
                     prdct_cost=input("enter cost of product: ")
                     item_list[-1].insert(1,prdct_name)
                     item_list[-1].insert(2,prdct_cost)
                     print("           product added sucessfully   ")
                elif admin_choice==3:

                
                        list_print(item_list)                   
                        remove_choice=int(input("enter product id:"))-1
                        item_list.remove(item_list[remove_choice])

                        print("           product removed sucessfully   ")
                        tryal=0
                        for item in item_list:
                            tryal=tryal+1
                            item[0]=tryal
                        
                     
                    
                elif(admin_choice==4 ):  
                    break  

        else :
            print("             enter a valid password")
    
    elif(a==2):#customer loop
        clear()
        print ('                                                                                            WELCOME  TO VIVA STORE ')
        space_print()
        while True:  
            print('''              1.view product
              2.view cart
              3.exit ''')
            cust_choice=int(input(''))

            clear()
            if cust_choice==1:#view product
                space_print()
                list_print(item_list)
                while True:
                    print('''                   1.add to cart
                   2.back
                   ''')

                    cust_option=int(input('''    
                    
                    
                                
                                  Enter your choice:    ''')) 
                    if cust_option==1:
                        ask_id=int(input("                                  Enter id: "))
                        ask_id=ask_id-1
                        cust_cart.append(item_list[ask_id])
                        clear()
                        list_print(item_list)
                    if cust_option!=1:
                        clear()
                        print ('                                                                                            WELCOME  TO VIVA STORE ')
                        space_print()
                        break
            elif cust_choice==2:#view cart

                tryal=0
                for item in cust_cart:
                    tryal=tryal+1
                    item[0]=tryal
                clear()
                space_print()
                list_print(cust_cart)
                cartout_choice=0
                while cartout_choice!=1:
                    
                    
                    space_print()
                    print('''              1.checkout
              2.delete item
              3.exit ''') 
                    cartout_choice=int(input('''
                    


                                                enter your choice:  '''))   
                    clear()
                    if cartout_choice==1:#checkout
                    
                        space_print()
                        recipt_print(cust_cart)

                        ex=int(input("    Enter any Key to exit "))
                        cust_cart=[]
                        clear()
                        space_print()
                        break
                
                    elif cartout_choice==2:#remove item

                        space_print()
                        list_print(cust_cart)                   
                        remove_choice=int(input("enter product id:"))-1
                        cust_cart.remove(cust_cart[remove_choice])
                        tryal=0
                        for item in cust_cart:
                            tryal=tryal+1
                            item[0]=tryal
                        
                        break
                    elif cartout_choice>=3:
                        break
            elif cust_choice>=3:
                break


    elif(a==3):#exit
        print('exit')
        break
   
    else:
        print('enter valid choice')
