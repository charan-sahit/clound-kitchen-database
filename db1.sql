UNLOCK TABLES;
DROP DATABASE IF EXISTS CLOUD1;
CREATE SCHEMA CLOUD1;
USE CLOUD1;



-- DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer
(
	Customer_ID int  NOT NULL, 
	PRIMARY KEY (Customer_ID),
	Customer_Name varchar(50) NOT NULL,
	Email_ID varchar(40)
);
LOCK TABLES Customer WRITE;
INSERT INTO Customer
VALUES
(1,'Sreejan','sreejanpatel@gmail,com'),
(2,'Lenka','lenkamawa@gmail,com'),
(3,'Raj','rajpanganamala@gmail,com');
UNLOCK TABLES;



-- DROP TABLE IF EXISTS Customer_PhoneNumber;
CREATE TABLE Customer_PhoneNumber
(
  Customer_ID int NOT NULL,
  FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID),
  Phone_Number int NOT NULL,
  PRIMARY KEY (Customer_ID, Phone_Number)
);
LOCK TABLES Customer_PhoneNumber WRITE;
INSERT INTO Customer_PhoneNumber
VALUES
(1,1010101010),
(2,1122334455),
(3,1234567890);
UNLOCK TABLES;



-- DROP TABLE IF EXISTS Customer_Address; 
CREATE TABLE Customer_Address
(
  Customer_ID int NOT NULL,
  FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID),
  House_Number int NOT NULL,
  Street_Name varchar(20) NOT NULL,
  Landmark varchar(20),
  City varchar(10) NOT NULL,
  State varchar(20) NOT NULL,
  Pin_code  int NOT NULL,
  Address_ID int NOT NULL,
  PRIMARY KEY (Address_ID)
);
LOCK TABLES Customer_Address WRITE;
INSERT INTO Customer_Address
VALUES
(1,30,'Colaba Causeway','Gateway Of India','Mumbai','Maharashtra',533005,5),
(2,50,'Connaught Place',NULL,'Delhi','Uttarpradesh',522006,6),
(3,60,'Park Street',NULL,'Kolkata','WestBengal',511880,7),
(3,541,'Mall Road',NULL,'Shimla','HimachalPradesh',545680,8);
UNLOCK TABLES;



-- DROP TABLE IF EXISTS Dish;
CREATE TABLE Dish
(
  Name varchar(25)  NOT NULL,
  Food_type ENUM('Vegetarian','Non_vegetarian','Egg_Content'),
  Dish_ID int NOT NULL,
  PRIMARY KEY (Dish_ID),
  Price int NOT NULL,
  Description_Details varchar(100) NOT NULL
);
LOCK TABLES Dish WRITE;
INSERT INTO Dish
VALUES
('Jilebi',1,1,50,'Sweets'),
('Chapathi',2,2,100,'Breakfast'),
('Haskas',3,3,200,'Dessert(Special)');
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Dish;
CREATE TABLE Outlet
(
  Outlet_id int NOT NULL,
  PRIMARY KEY (Outlet_id),
  House_Number int NOT NULL,
  Street_name varchar(20) NOT NULL,
  Landmark varchar(20),
  City varchar(10) NOT NULL,
  State varchar(10) NOT NULL,
  Pin_code int NOT NULL
);
LOCK TABLES Outlet WRITE;
INSERT INTO Outlet
VALUES
(100,52,'Colaba Causeway','Gateway Of India','Mumbai','Maharastra',533005),
(101,512,'Connaught Place',NULL,'Delhi','UP',522006),
(102,851,'Park Street',NULL,'Kolkata','WestBengal',511880);
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Chef;
CREATE TABLE Chef
(
	Chef_ID int NOT NULL,
	PRIMARY KEY (Chef_ID),
	Name varchar(20) NOT NULL,
	Phone_number int NOT NULL,
	Salary int NOT NULL
);
LOCK TABLES Chef WRITE;
INSERT INTO Chef
VALUES
(50,'Sreeja',2100000000,50000),
(51,'charani',1111111111,60000),
(85,'raji',1111100000,20000);
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Dish;
CREATE TABLE Chef_specialities
(
	Chef_ID int NOT NULL,
	FOREIGN KEY (Chef_ID) REFERENCES Chef (Chef_ID),		-- 			
	Specialties varchar(100) NOT NULL,
	PRIMARY KEY (Chef_ID, Specialties)
);
LOCK TABLES Chef_specialities WRITE;
INSERT INTO Chef_specialities
VALUES
(50,'Jilebi'),
(85,'Chapathi'),
(51,'Haskas');
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Dish;
CREATE TABLE Ingredient_Suppliers
(
  Suppliers_ID  int NOT NULL,
  PRIMARY KEY (Suppliers_ID),
  Suppliers_Name varchar(20) NOT NULL,
  Suppliers_Address  varchar(50) NOT NULL,
  Phone_Number int NOT NULL,
  Supplies varchar(50) NOT NULL
);
LOCK TABLES Ingredient_Suppliers WRITE;
INSERT INTO Ingredient_Suppliers
VALUES
(855,'Stark','asdf',2020202020,'good'),
(522,'Tony','asdfasdf',1010101010,'better'),
(255,'Potts','asdfasdf',1212121212,'best');
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Offers;
CREATE TABLE Offers
(
	Promocode int NOT NULL,
	PRIMARY KEY (Promocode),
	Description varchar(30) NOT NULL
);
LOCK TABLES Offers WRITE;
INSERT INTO Offers
VALUES
(50,'100/- off'),
(51,'102/- off'),
(25,'50/- off');
UNLOCK TABLES;



-- DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders
(
  Customer_ID int NOT NULL,
  Order_Serial_Number int NOT NULL,
  Payment_Mode ENUM('Online_Banking','Credit_Card','PhonePay','PayTm'),
  Total_Price int NOT NULL,			
  Final_Price int NOT NULL,			
  Promocode int ,
  FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID),
  FOREIGN KEY (Promocode) REFERENCES Offers (Promocode),
  PRIMARY KEY (Customer_ID ,Order_Serial_Number)
);
LOCK TABLES Orders WRITE;
INSERT INTO Orders
VALUES
(1,50,1,840,830,50),
(2,52,4,752,750,25),
(3,56,2,500,495,51);
UNLOCK TABLES;


-- DROP TABLE IF EXISTS Feedback;
CREATE TABLE Feedback
(
  Customer_ID int NOT NULL,
  Order_ID int NOT NULL,
  FOREIGN KEY (Customer_ID,Order_ID) REFERENCES Orders (Customer_ID,Order_Serial_Number),
  Rating int NOT NULL,
  Review varchar(100)
);
LOCK TABLES Feedback WRITE;
INSERT INTO Feedback
VALUES
(1,50,5,'Best food I have ever eaten in my life'),
(3,56,4,'Better than my moms food'),
(2,52,1,'Worst food I hv ever eaten in my entire life');
UNLOCK TABLES;


-- DROP TABLE IF EXISTS Dish;
CREATE TABLE Delivery_Person
(
  Delivery_Person_Name varchar(30) NOT NULL,
  ID int NOT NULL,
  Vehicle_ID int NOT NULL,
  Rating int NOT NULL,
  PRIMARY KEY (ID)
);
LOCK TABLES Delivery_Person WRITE;
INSERT INTO Delivery_Person
VALUES
('dabang1',40,5451,2),
('dabang2',41,1523,5),
('dabang3',42,8745,1);
UNLOCK TABLES;



-- DROP TABLE IF EXISTS Dish;
CREATE TABLE Order_Status
(
  Customer_ID int NOT NULL,
  Order_Serial_Number int NOT NULL,
  FOREIGN KEY (Customer_ID,Order_Serial_Number) REFERENCES Orders (Customer_ID,Order_Serial_Number),
  Delivery_Man_ID int NOT NULL,
  FOREIGN KEY (Delivery_Man_ID) REFERENCES Delivery_Person (ID),
  Time_of_Order datetime,
  Current_Status varchar(100) NOT NULL,
  Time_of_Delivery datetime,
  Time_Taken_for_Delivery int 
);
LOCK TABLES Order_Status WRITE;
INSERT INTO Order_Status
VALUES
(1,50,40,'9999-12-31 23:50:59','Food is at your doorstep','9999-12-31 23:59:59',NULL),
(2,52,41,NULL,'Food has been delivered',NULL,NULL),
(3,56,42,NULL,'Come and pick your food at the doorstep',NULL,NULL);
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Dishes;
CREATE TABLE Dishes
(
  Customer_ID int NOT NULL,
  Order_Serial_Number int NOT NULL,
  Dish_ID int NOT NULL,
  Quantity int NOT NULL,
  FOREIGN KEY (Customer_ID,Order_Serial_Number) REFERENCES Orders (Customer_ID,Order_Serial_Number),
  PRIMARY KEY (Customer_ID ,Order_Serial_Number,Dish_ID,Quantity)
);
LOCK TABLES Dishes WRITE;
INSERT INTO Dishes
VALUES
(1,50,1,4),
(2,52,2,5),
(3,56,3,6);
UNLOCK TABLES;



-- DROP TABLE IF EXISTS DeliveryPerson_PhoneNumber;
CREATE TABLE DeliveryPerson_PhoneNumber
(
	ID int NOT NULL,
	Phone_Number int NOT NULL,
    FOREIGN KEY (ID) REFERENCES Delivery_Person (ID),
	PRIMARY KEY (ID, Phone_Number)
);
LOCK TABLES DeliveryPerson_PhoneNumber WRITE;
INSERT INTO DeliveryPerson_PhoneNumber
VALUES
(40,2121212121),
(41,1212121212),
(42,1021021021);
UNLOCK TABLES;



-- DROP TABLE IF EXISTS DeliveryPerson_Languages;
CREATE TABLE DeliveryPerson_Languages
(
  ID int NOT NULL,
  Langauge varchar(50) NOT NULL,
  FOREIGN KEY (ID) REFERENCES Delivery_Person (ID),
  PRIMARY KEY (ID, Langauge)
);
LOCK TABLES DeliveryPerson_Languages WRITE;
INSERT INTO DeliveryPerson_Languages
VALUES
(40,'Telugu,Hindi,Tamil'),
(41,'Telugu,Hindi,Tamil,English'),
(42,'Telugu,Hindi,Tamil,English,Malayalam');
UNLOCK TABLES;



-- DROP TABLE IF EXISTS Full_Time;
CREATE TABLE Full_Time
(
  Delivery_Person_ID int NOT NULL,
  Salary_per_month int NOT NULL,
  Number_of_holidays_taken int,
  Health_insurance int NOT NULL,
  FOREIGN KEY (Delivery_Person_ID) REFERENCES Delivery_Person (ID)
);
LOCK TABLES Full_Time WRITE;
INSERT INTO Full_Time
VALUES
(40,15000,5,0),
(41,10000,3,1);
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Part_Time;
CREATE TABLE Part_Time
(
  Delivery_Person_ID int NOT NULL,
  Salary_per_hour int NOT NULL,
  Number_of_hours_worked int NOT NULL,
  FOREIGN KEY (Delivery_Person_ID) REFERENCES Delivery_Person (ID)
);
LOCK TABLES Part_Time WRITE;
INSERT INTO Part_Time
VALUES
(42,100,10);
UNLOCK TABLES;




-- DROP TABLE IF EXISTS Order_Details;
CREATE TABLE Order_Details
(
  Customer_ID int NOT NULL,
  Address_ID int NOT NULL,
  Outlet_ID int NOT NULL,
  Order_Serial_Number int NOT NULL, 
  FOREIGN KEY (Customer_ID,Order_Serial_Number) REFERENCES Orders (Customer_ID,Order_Serial_Number),
  FOREIGN KEY (Outlet_ID) REFERENCES Outlet (Outlet_id),
  FOREIGN KEY (Address_ID) REFERENCES Customer_Address (Address_ID)
);
LOCK TABLES Order_Details WRITE;
INSERT INTO Order_Details
VALUES
(1,5,102,50),
(2,6,101,52),
(3,7,100,56);
UNLOCK TABLES;





-- DROP TABLE IF EXISTS Delivery;
CREATE TABLE Delivery
(
  Customer_ID int NOT NULL,
  Address_ID int NOT NULL,
  Outlet_ID int NOT NULL,
  Delivery_Person_ID int NOT NULL,
  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
  FOREIGN KEY (Address_ID) REFERENCES Customer_Address(Address_ID),
  FOREIGN KEY (Outlet_ID) REFERENCES Outlet(Outlet_id),
  FOREIGN KEY (Delivery_Person_ID) REFERENCES  Delivery_Person(ID)
);
LOCK TABLES Delivery WRITE;
INSERT INTO Delivery
VALUES
(3,7,100,40),
(2,6,101,41),
(1,5,102,42);
UNLOCK TABLES;



-- DROP TABLE IF EXISTS Supply;
CREATE TABLE Supply
(
  Suppliers_ID int NOT NULL,
  Outlet_ID int NOT NULL,
  FOREIGN KEY (Suppliers_ID) REFERENCES Ingredient_Suppliers (Suppliers_ID),
  FOREIGN KEY (Outlet_ID) REFERENCES Outlet (Outlet_id),
  PRIMARY KEY (Suppliers_ID, Outlet_ID)
);
LOCK TABLES Supply WRITE;
INSERT INTO Supply
VALUES
(855,100),
(522,101),
(255,102);
UNLOCK TABLES;





	