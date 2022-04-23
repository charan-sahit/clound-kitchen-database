LINK FOR THE VIDEO IN GOOGLE DRIVE: https://drive.google.com/file/d/1H0UJS1Y_ZNPQTWVfuKO6rzlg-KzpoKw1/view?usp=sharing

We can run our code using:

$ mysql -u <username> -p 
$ source db1.sql
$ python3 resortChain.py

List of all the commands our code can run are:

INSERT:

1)insertCustomer()

    -Customer details are taken through the input.

2)insertCustomerAddress()

    -Customer addresses are taken through the input.

3)insertChef()

    -Chef details are taken though the input.

4)insertOrder()

    -Order details of each order are taken as input.

DELETION:

1)deleteOffer()

    -Offers are deleted when they are expired.

2)deleteOrder()

    -Orders are deleted when a customer cancels them.

MODIFY:

1)updateOrderStatus()

    -Status of the order is modified accordingly.

2)updateDishPrice()

    -Dish price is modified whenever necessary.

3)updateOffer()

    -Offers have to be modified according to the season.

RETRIEVE:

1)retrieveOrders()

    -Retrieves all the orders of a customer

2)projectDishes()

    -projects the dishes which have price above or below a given price

3)search()

    -searches the dish name with a partial text

4)retrieveRating()

    -gives the no of ratings greater than a given value

5)retrieveFeedback()

    -gives the precentage of customers that give feedback

6)retrieveTimeTakenForDelivery()

    -gives us the time taken for delivering the order.

7)retrieveTotalPrice()

    -gives us the total price of the order, which the customer has to pay.

QUIT:
    Quits the python program


A few field names and attributes are changed during this phase,so that we can avoid the problems while accessing them(As some of them are keywords).
Changes made:
1)Order  -->  Orders
2)Orders  -->  Order_Details
3)Name (from Delivery_Person)  -->  Delivery_Person_Name