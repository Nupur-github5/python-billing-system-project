import mysql.connector as mq
from tabulate import tabulate
def menu():
    print("BILLING SYSTEM")
    print("==============\n")
    print("MAIN MENU")
    print("==============")
    print("1.Register User \t 2.Search Customer")
    print("3.Update Customer \t 4.Generate BIll")
    print("5.Delete Customer \t 6.Help ")
    print("7.Exit")
    
def register():
    print("Registration...")
    ph=input("Enter your Mobile number : ")
    name=input("Enter Name : ")
    add=input("Enter Address : ")
    aadhar=input("Enter Aadhar number : ")

    con=mq.connect(host="localhost",user="root",passwd="root",database="mobile")
    cur=con.cursor()
    query="insert into cust(phno,name,addr,aadhar)values({},'{}','{}','{}')".format(ph,name,add,aadhar)
    cur.execute(query)
    con.commit()
    print("Successfully registered the user !")
    con.close()
def search():
    print("Search Customer...")
    ph=input("Enter your mobile number : ")
    con=mq.connect(host="localhost",user="root",passwd="root",database="mobile")
    cur=con.cursor()
    query="select * from cust where phno={}".format(ph)
    cur.execute(query)
    res=cur.fetchall()
    if res==[]:
        print("Customer doesn't Exist")
    else:
        print("Mobile-number  Name  Address  Aadhar  Bill  Status")
        print(tabulate(res))
    con.close()
def update():
    print("Update Customer details...")
    ph=input("Enter your mobile number : ")
    con=mq.connect(host="localhost",user="root",passwd="root",database="mobile")
    cur=con.cursor()
    query="select * from cust where phno={}".format(ph)
    cur.execute(query)
    res=cur.fetchall()
    if res==[]:
        print("Customer doesn't Exist !")
    else:
        print(" 1. Name\n 2. Address\n 3. Aadhar no.")
        choice=int(input("Enter Choice to Update:"))
        if choice==1:
            nam=input("Enter New Name : ")
            query="update cust set name='{}' where phno={}".format(nam,ph)
            cur.execute(query)
            con.commit()
            print("Successfully Updated")
        elif choice==2:
            add=input("Enter New Address : ")
            query="update cust set addr='{}' where phno={}".format(add,ph)
            cur.execute(query)
            con.commit()
            print("Successfully Updated")
        elif choice==3:
            aadhar=input("Enter New Aadhar : ")
            query="update cust set aadhar='{}' where phno={}".format(aadhar,ph)
            cur.execute(query)
            con.commit()
            print("Successfully Updated !")
        else:
            print("Please choose correct choice...")
        con.close()
def billing():
    print("Billing")
    ph=input("Enter your mobile number : ")
    con=mq.connect(host="localhost",user="root",passwd="root",database="mobile")
    cur=con.cursor()
    query="select * from cust where phno={}".format(ph)
    cur.execute(query)
    res=cur.fetchall()
    if res==[]:
        print("Customer doesn't Exist!")
    else:
        calls=int(input("Enter No of Calls :"))
        old_bill=res[0][4]
        bill=0
        if calls>150:
            bill=bill+(calls-150)*3 + 50*2.5 + 50*1.5
        elif 100<calls<=150:
            bill = bill + (calls-100)*2.5+50*1.5
        elif 50<calls<=100:
            bill= bill+(calls-50)*1.5
        print("Billing")
        if res[0][4]!="Paid":
            old_bill=res[0][4]
        else:
            old_bill=0
        print("Pending Bill Amount" ,old_bill)
        print("New Bill Amount",bill)
        print("Total Bill Amount" ,bill+old_bill)
        choice=str(input("Press Y to Pay Bill now or Any other ker to Pay Later: "))
        if choice in ['y','Y']:
            query="update cust set bill='{}',status='Paid' where phno={}".format(bill+old_bill,ph)
            cur.execute(query)
            con.commit()
            print("Successfully Paid the Bill")
        else:
            query="update cust set bill='{}',status='Un-Paid' where phno={}".format(bill+old_bill,ph)
            cur.execute(query)
            con.commit() 
            print("Please make payment as soon as possible")
    con.close()
def delete():
    ph=input("Enter your mobile num:")
    con=mq.connect(host="localhost",user="root",passwd="root",database="mobile")
    cur=con.cursor()
    query="select * from cust where phno={}".format(ph)
    cur.execute(query)
    res=cur.fetchall()
    if res==[]:
        print("Customer doesn't Exist")
    else:
        choice=input("Are you Sure to delete customer...(Y/N) : ")
        if choice in ['y','Y']:
            query="delete from cust where phno={}".format(ph)
            cur.execute(query)
            con.commit()
            print("Successfully Deleted Customer frome Database!")
        else:
            print("No changes made in Database.")
    con.close()
        
def helping():
    print("Helping")
    print("First 50 Calls are free")
    print("50-100 calls are 1.5Rs per Call")
    print("101-150 calls are 2.5Rs per Call")
    print("Above 150 calls are 3Rs per Call")
while True:
    menu()
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        register()
    elif choice==2:
        search()
    elif choice==3:
        update()
    elif choice==4:
        billing()
    elif choice==5:
        delete()
    elif choice==6:
        helping()
    elif choice==7:
        print("exit")
    else:
        print("Please Choose correct choice and Try Again")
    choice=int(input("Press 0 to continue...Any other ker to Exit...:"))
    if choice!=0:
        break

