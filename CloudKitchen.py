import pymysql
import pymysql.cursors
import subprocess as sp
import datetime

from tabulate import tabulate

def insertCustomer():
    global cur
    tuple = {}
    print("Enter the Customer details:")

    

    try:
        tuple["Customer_ID"] = int(input("Customer_ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    tuple["Customer_Name"] = input("Name: ")
    tuple["Email"] = input("Email: ")

    tuple_phone = []
    
    try:
        n = int(input("Enter the number of Customer's phone number's you want to input: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n") 
    
    for i in range(n):
        tuple_phone.append(int(input("Phone Number : ")))
    
    try:
        query = "INSERT INTO Customer(Customer_ID, Customer_Name, Email_ID) VALUES('%d', '%s', '%s')" % (
            tuple["Customer_ID"], tuple["Customer_Name"], tuple["Email"] )
        cur.execute(query)
        connect.commit()
    except Exception as e:
        print(e)
        print("\n\nError: WRONG DATA!\n")
        return
    
    for i in range(n):
        try:
            query = "INSERT INTO Customer_PhoneNumber(Customer_ID, Phone_Number) VALUES('%d', '%d')" % (
                tuple["Customer_ID"], tuple_phone[i])
            cur.execute(query)
            connect.commit()
        except Exception as e:
            print(e)
            print("\n\nError: WRONG DATA!\n")
            return
    
    return

    

    
    

def insertCustomerAddress():
    global cur
    tuple = {}
    print("Enter the address of the customer:")
    
    try:
        tuple["Customer_ID"] = int(input("Customer_ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        tuple["House_Number"] = int(input("House Number:"))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    

    tuple["Street_Name"] = input("Street Name:")
    tuple["Landmark"] = input("Landmark:")
    tuple["City"] = input("City:")
    tuple["State"] = input("State:")
    
    try:
        tuple["Pin_Code"] = int(input("Pin Code:"))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    
    try:
        tuple["Address_ID"] = int(input("Address ID:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

       
    
    try:
        query = "INSERT INTO Customer_Address(Customer_ID, House_Number, Street_Name, Landmark, City, State, Pin_Code, Address_ID) VALUES('%d', '%d', '%s', '%s', '%s', '%s', '%d', '%d')" % (tuple["Customer_ID"], tuple["House_Number"], tuple["Street_Name"], tuple["Landmark"], tuple["City"], tuple["State"],  tuple["Pin_Code"], tuple["Address_ID"])
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

def insertChef():
    global cur
    tuple = {}
    print("Enter the Chef Details: ")
    
    try:
        tuple["Chef_ID"] = int(input("Chef_ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    tuple["Chef_Name"] = input("Chef_Name: ")
    
    try:
        tuple["Chef_Ph"] = int(input("Chef_Ph: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        tuple["Chef_Salary"] = int(input("Chef_Salary: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        query = "INSERT INTO Chef(Chef_ID, Name, Phone_number, Salary) VALUES('%d', '%s', '%d', '%d')" % (
            tuple["Chef_ID"], tuple["Chef_Name"], tuple["Chef_Ph"], tuple["Chef_Salary"] )
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    print("Enter the Chef Specialities: ")

    tuple["Specialties"] = input("Specialities: ")

    try:
        query = "INSERT INTO Chef_specialities(Chef_ID, Specialties) VALUES('%d', '%s')" % (
            tuple["Chef_ID"],tuple["Specialties"])
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return
    


def insertOrders():
    global cur
    tuple = {}
    print("Enter the details of the order")
    
    try:
        tuple["Customer_ID"] = int(input("Customer_ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    try:
        tuple["Address_ID"] = int(input("Address ID:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        
    try:
        tuple["Outlet_ID"] = int(input("Outlet ID:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    try:
        tuple["Order_Serial_Number"] = int(input("Order_Serial_Number:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        tuple["Total_Price"] = int(input("Total_Price:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    try:
        tuple["Final_Price"] = int(input("Final_Price:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    


    try:
        tuple["Payment_Mode"] = int(input("Payment_Mode:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    
    
    


    
    try:
        tuple["Promocode"] = int(input("Promocode:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    

    
    try:
        query = "INSERT INTO Orders(Customer_ID, Order_Serial_Number, Payment_Mode, Total_Price, Final_Price, Promocode) VALUES('%d','%d','%d','%d','%d',%d)" % (
            tuple["Customer_ID"], tuple["Order_Serial_Number"], tuple["Payment_Mode"],tuple["Total_Price"], tuple["Final_Price"], tuple["Promocode"]  
        )
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    n = int(input("Number of dishes in order: "))
    while(n):
        tuple["Dish_ID"] = int(input("Enter the Dish_ID: "))
        tuple["Quantity"] = int(input("Enter the Quantity: "))
        try:
            query = "INSERT INTO Dishes(Customer_ID,Order_Serial_Number,Dish_ID,Quantity) VALUES('%d' , '%d' , '%d' , '%d' )" % (
                tuple["Customer_ID"], tuple["Order_Serial_Number"], tuple["Dish_ID"], tuple["Quantity"]
            )
            cur.execute(query)
            connect.commit()
        except Exception as err:
            print(err)
            print("\n\nError: WRONG DATA!\n")
        n= n -1

    try:
        query = "INSERT INTO Order_Details (Customer_ID, Address_ID, Outlet_ID, Order_Serial_Number) VALUES('%d','%d','%d','%d')" % (
            tuple["Customer_ID"], tuple["Address_ID"], tuple["Outlet_ID"], tuple["Order_Serial_Number"] )
        
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    

    
def deleteOffer():
    global cur

    try:
        x = int(input("Enter Promocode of the offer: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")


 
    try:
        query = "UPDATE Orders SET Promocode = NULL, Final_Price = Total_Price WHERE Promocode = '%d'" % (x)
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return



    try:
        query = "DELETE FROM Offers WHERE Promocode=%d;" % (x)
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return
    
    




def deleteOrder():
    global cur

    try:
        x = int(input("Enter The Customer ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        y = int(input("Enter The Order Serial Number: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    try:
        query = "DELETE FROM Dishes WHERE Customer_ID=%d and Order_Serial_Number=%d;" % (x,y)
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    try:
        query = "DELETE FROM Order_Details WHERE Customer_ID=%d and Order_Serial_Number=%d;" % (x,y)
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    try:
        query = "DELETE FROM Orders WHERE Customer_ID=%d and Order_Serial_Number=%d;" % (x,y)
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    

    

    try:
        query = "UPDATE Order_Status SET Current_Status = 'cancelled' WHERE Customer_ID=%d and Order_Serial_Number=%d;" % (x,y)
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

def updateOrderStatus():
    global cur
    tuple = {}
    print("Update the status of the order")
    try:
        tuple["Customer_ID"] = int(input("Enter The Customer ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        tuple["Order_Serial_Number"] = int(input("Order_Serial_Number:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    
    tuple["Status"] = input("New status:")
    
    try: 
        query = "UPDATE OrderStatus SET Current_Status = '%s' WHERE Customer_ID = '%d' AND Order_Serial_Number = '%d'" % (
        tuple["Status"], tuple["Customer_ID"], tuple["Order_Serial_Number"])

    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n") 
        return 

    if tuple["Status"] == "delivered":
        tuple["Time_of_Delivery"] = input("Time_of_Delivery:")
        try:    
            query = "UPDATE OrderStatus SET Time_of_Delivery = '%s' WHERE Customer_ID = '%d' AND Order_Serial_Number = '%d'" % (
            tuple["Time_of_Delivery"], tuple["Customer_ID"], tuple["Order_Serial_Number"])
        except Exception as err:
            print(err)
            print("\n\nError: WRONG DATA!\n") 
            return 



def updateDishPrice():
    global cur
    
    try:
        x = int(input("Enter the Dish ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    try:
        y = int(input("Enter the New Price of the Dish: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n") 
        return 

    try:
        query = "UPDATE Dish SET Price=%d  WHERE Dish_ID=%d;" % (y,x)
        cur.execute(query)
        connect.commit()
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return
    

def updateOffer():
    global cur

    try:
        n = int(input("Enter The number of offers to be modified: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    while(n):

        try:
            x = int(input("Enter Promocode of the offer: "))
        except Exception as err:
            print(err)
            print("\n\nError: WRONG DATA!\n")
            n = n - 1
            continue

        y = input("Enter the Description of the new offer: ")

        try:
            query = "UPDATE Offers SET Description='%s' WHERE Promocode=%d;" % (y,x)
            cur.execute(query)
            connect.commit()
        except Exception as err:
            print(err)
            print("\n\nError: WRONG DATA!\n")
            n = n - 1
            continue

        n = n - 1    


def retrieveOrders():
    global cur
    
    try:
        n = int(input("Enter The Customer_ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    try:
        query = "SELECT O.Order_Serial_Number,D.Dish_ID,D.Quantity,O.Payment_Mode,O.Promocode,F.Rating,F.Review AS CustomerOrders FROM Orders O,Dishes D,Feedback F WHERE O.Customer_ID=%d AND O.Order_Serial_Number = D.Order_Serial_Number AND O.Order_Serial_Number = F.Order_ID;" % (n)
        no_of_rows = cur.execute(query)
    except Exception as err:
        print(err)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return        

    rows = cur.fetchall()
    viewTable(rows)
    connect.commit()

def retrieveRating():
    global cur    
    
    try:
        n = int(input("Enter The Rating Value above which you want to find the orders: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    try:
        query = "SELECT * FROM Feedback WHERE Rating > %d;" % (n)
        no_of_rows = cur.execute(query)
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return
    
    print(no_of_rows)

def retrieveFeedback():
    global cur 

    try:
        query1 = "SELECT * FROM Feedback;"
        no_of_rows1 = cur.execute(query1)
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    try:
        query2 = "SELECT * FROM Customer;"
        no_of_rows2 = cur.execute(query2)
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    percentage = (int(no_of_rows1)/float(no_of_rows2)) * 100
    print(percentage)




def search():
    global cur
    
    substring = input("Enter the partial text: ")
    length = len(substring)
    
    try:
        query = "SELECT Name FROM Dish Where SUBSTRING(Name,1, '%d') = '%s'" % (length, substring)
        no_of_rows = cur.execute(query)
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    connect.commit()

def projectDishes():
    global cur
    try:
        price = int(input("Enter the price for the projection: "))
    except Exception as err:
        print(err)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    
    try:
        flag = int(input("Enter 0 if above 1 if below: "))
    except Exception as err:
        print(err)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    
    if flag == 0:
        query = "SELECT Name FROM Dish WHERE Price > '%d'" % (
            price
        )
    elif flag ==1:
        query = "SELECT Name FROM Dish WHERE Price < '%d'" % (
            price
        )        
    
    total_rows = cur.execute(query)
    tuples =  cur.fetchall()
    
    viewTable(tuples)
    connect.commit

def retrieveTotalPrice():
    global cur
    tuple = {}
    try:
        tuple["Customer_ID"] = int(input("Enter The Customer ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        tuple["Order_Serial_Number"] = int(input("Order_Serial_Number:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")


    query = "SELECT SUM(b.Price*a.Quantity) as Total_Price from Dishes a, Dish b where a.Customer_ID = '%d' AND a.Order_Serial_Number = '%d' AND a.Dish_ID = b.Dish_ID" % (
        tuple["Customer_ID"], tuple["Order_Serial_Number"])

    cur.execute(query)
    tuples =  cur.fetchall()
    
    viewTable(tuples)
    connect.commit
    
def retrieveTimeTakenForDelivery():
    global cur
    tuple = {}
    try:
        tuple["Customer_ID"] = int(input("Enter The Customer ID: "))
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        tuple["Order_Serial_Number"] = int(input("Order_Serial_Number:")) 
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")
    
    try:
        query = "SELECT TIMESTAMPDIFF(minute, Time_of_Order, Time_of_Delivery) as Duration_Of_Delivery(mins) from Order_Status where Customer_ID = '%d' AND Order_Serial_Number = '%d'" % (
            tuple["Customer_ID"], tuple["Order_Serial_Number"]
        )
        cur.execute(query)
    except Exception as err:
        print(err)
        print("\n\nError: WRONG DATA!\n")

    
    tuples =  cur.fetchall()
    
    viewTable(tuples)
    connect.commit


def viewTable(tuples):
    global cur
    alpha = []
    
    try:
        alpha.append(list(tuples[0].keys()))
    except:
        print("The Table is empty")
        return
    for tuple in tuples:
        beta = []
        for l in tuple.keys():
            beta.append(tuple[l])
        alpha.append(beta)
    print(tabulate(alpha, tablefmt="psql", headers="firstrow"))
    print()
    return


def insertOptions():
    print("\n\nChoose an INSERT option\n\n")
    print("1. CUSTOMER")
    print("2. CUSTOMER ADDRESS")
    print("3. CHEF")
    print("4. ORDER")
    print("\n")
    
    n = input()

    if n == '1':
        insertCustomer()
    elif n == '2':
        insertCustomerAddress()
    elif n == '3':
        insertChef()
    elif n == '4':
        insertOrders()


def deleteOptions():
    print("\n\nChoose a DELETE option\n\n")
    print("1. OFFERS")
    print("2. ORDER")
    print("\n")

    n = input()

    if n == '1':
        deleteOffer()
    elif n == '2':
        deleteOrder()


def updateOptions():
    print("\n\nChoose a UPDATE option\n\n")
    print("1. ORDER STATUS")
    print("2. DISH PRICE")
    print("3. OFFERS")
    print("\n")

    n = input()

    if n == '1':
        updateOrderStatus()
    elif n == '2':
        updateDishPrice()
    elif n == '3':
        updateOffer()

def retrieveOptions():
    global cur
    print("\n\nChoose a RETRIEVE option\n\n")
    print("1. ALL ORDER TUPLES OF A CUSTOMER")
    print("2. DISHES ABOVE OR BELOW A PRICE")
    print("3. SEARCH")
    print("4. NUMBER_OF_ORDER_ABOVE_RATING")
    print("5. PERCENTAGE GIVING FEEDBACK")
    print("6. TOTAL TIME TAKEN FOR DELIVERY")
    print("7. TOTAL PRICE")
    print("\n")

    n = input()


    if n == '1':
        retrieveOrders()
    elif n == '2':
        projectDishes()
    elif n == '3':
        search()
    elif n == '4':
        retrieveRating()    
    elif n == '5':
        retrieveFeedback() 
    elif n == '6':
        retrieveTimeTakenForDelivery()
    elif n == '7':
        retrieveTotalPrice()
    



while(1):
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
    #username="root"
    #password="password"

    try:
        connect = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='CLOUD1',
                              cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        continue

    with connect:
        cur = connect.cursor()
        flag = 0
        while(1):
            tmp = sp.call('clear', shell=True)

            print("CHOOSE AN OPTION\n")
            
            print("1.Insert Options")
            print("2.Deletion Options")
            print("3.Modify Options")
            print("4.Retrieve Options")
            print("5.Quit")
            inp = input("\nCHOICE ? ")
            
            if(inp == '1'):
                insertOptions()
            elif(inp == '2'):
                deleteOptions()
            elif(inp == '3'):
                updateOptions()
            elif(inp == '4'):
                retrieveOptions()
            elif(inp == '5'):
                print("Bye")
                break    
                
            
            print("Press enter to continue ... ")
            x = input()
            
                

    
    break
