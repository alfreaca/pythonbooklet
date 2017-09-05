import sqlite3
import os

if not os.path.isfile('Customer.db'):
    customer_db = sqlite3.connect("Customer.db")
    c = customer_db.cursor()
    c.execute('''CREATE TABLE CustomerDetails
    (Customer_first_name text,
    Customer_surname text,
    Customer_Town text,
    Customer_phone int,
    Carpets_cost int,
    Underlays_cost int,
    underlays_type text,
    Grip_cost int,
    length int,
    width int,
    labour_cost int,
    overall_cost int)
    ''')
    customer_db.commit()

customer_db = sqlite3.connect("Customer.db")

def carpet(len, wid):
    global carpet_size
    carpet_size = len * wid
    global carpet_cost
    carpet_cost = carpet_size * 22.50
    global underlay_First_step
    underlay_First_step = carpet_size * 5.99
    global underlay_Monarch
    underlay_Monarch = carpet_size * 7.99
    global underlay_Royal
    underlay_Royal = carpet_size * 60
    global gripper
    gripper = ((len + wid) * 2) * 1.1

def row_delete(Customer_phone):
    customer_db.execute('DELETE FROM CustomerDetails WHERE Customer_phone = ?', (Customer_phone))
    customer_db.commit()

def user_in(Customer_first_name, Customer_surname, Customer_Town, Customer_phone, Carpets_cost, Underlays_cost, underlays_type, Grip_cost, length, width, labour_cost, overall_cost):
    customer_db.execute('INSERT INTO CustomerDetails VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                            (Customer_first_name,
                            Customer_surname,
                            Customer_Town,
                            Customer_phone,
                            Carpets_cost,
                            Underlays_cost,
                            underlays_type,
                            Grip_cost,
                            length,
                            width,
                            labour_cost,
                            overall_cost))

password = input("What's the password?: ")

if password == 'J0hn Work':
    userinput_pick = input("What would you like to do?: \n You can add data, delete a customer or display all customers: ")
    if userinput_pick == 'Add data':
        first_name = input('Enter first name: ')
        surname = input('Enter surname: ')
        town = input('Enter town name: ')
        phone_number = input('Enter phone number: ')
        lengthinput = int(input('What is the length of the room: '))
        widthinput = int(input('What is the width of the room: '))
        carpet(lengthinput, widthinput)
        carpet_cost = carpet_size * 22.50

        underlay_pick = input('Are they using First Step, Monarch or Royal?: ')

        if underlay_pick == 'First Step'  or underlay_pick == 'first step':
            underlay_cost = underlay_First_step

        elif underlay_pick == 'Monarch' or underlay_pick == 'monarch':
            underlay_cost = underlay_Monarch

        elif underlay_pick == 'Royal' or underlay_pick == 'royal':
            underlay_cost = underlay_Royal

        if carpet_size > 16:
            hourly_cost = round((carpet_size/16)*65)
        else:
            hourly_cost = 65

        underlay_cost = underlay_cost
        underlay_type = underlay_pick
        grip_cost = gripper
        labour_cost = hourly_cost
        overall_cost = carpet_cost + hourly_cost + underlay_cost
        user_in(first_name, surname, town, phone_number, carpet_cost, underlay_cost, underlay_type, grip_cost, lengthinput, widthinput, labour_cost, overall_cost)
        customer_db.commit()

    elif userinput_pick == 'Delete a row':
        del_what2 = input("Please enter the phome number: ")
        row_delete(del_what2)
        customer_db.commit()

    elif userinput_pick == 'Display all customers':
        for row in customer_db.execute('SELECT * FROM CustomerDetails'):
            print(row)
    customer_db.close()
else:
    print("dumb")
