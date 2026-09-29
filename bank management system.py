import mysql.connector as con
def INSERT_RECORDS():
    cn=con.connect(host="localhost", user="root", passwd="admin", database="BANK")
    cur=cn.cursor()
    print("Enter Records: ")
    k='Y'
    while k=='y' or k=='Y':
        AN=input("Enter ACCOUNT NO.: ")
        CNM=input("Enter CUSTOMER Name: ")
        A=input("Enter ADDRESS: ")
        M=input("Enter MOBILE NO.: ")
        B=input("Enter AMOUNT: ")
        Q="INSERT INTO CUSTOMER VALUES('{}','{}','{}', '{}', '{}')".format(AN, CNM, A, M, B)
        cur.execute(Q)
        cn.commit()
        print("Record Successfully Inserted!!!")
        k=input("Want to Enter Again: [Y/N]: ")
    cn.close()


#DISPLAY RECORDS
def DISPLAY_RECORDS():
    cn=con.connect(host="localhost", user="root", passwd="admin", database="BANK")
    cur=cn.cursor()
    Q="SELECT * FROM CUSTOMER"
    cur.execute(Q)
    R=cur.fetchall()
    print("-"*50)
    print("CUSTOMER RECORDS")
    print("-"*50)
    for rec in R:
        print("ACCOUNT NO.: ",rec[0])
        print("CUSTOMER NAME: ",rec[1])
        print("ADDRESS: ",rec[2])
        print("MOBILE: ",rec[3])
        print("BALANCE: ",rec[4])
        print("-"*50)
    cn.close()


#SEARCH RECORDS
def SEARCH_RECORDS():
    cn=con.connect(host="localhost", user="root", passwd="admin", database="BANK")
    cur=cn.cursor()
    ACN=input("Enter ACNO TO BE SEARCHED: ")
    Q="SELECT * FROM CUSTOMER WHERE ACNO={}".format(ACN)
    cur.execute(Q)
    R=cur.fetchall()
    if R:
        for rec in R:
            print(R)
    else:
        print("No Record Found")
    cn.close()


#UPDATING RECORDS
def UPDATE_RECORDS():
    cn=con.connect(host="localhost", user="root", passwd="admin", database="bank")
    cur=cn.cursor()
    acn=input("Enter ACNO TO BE UPDATED: ")
    Q="SELECT * FROM CUSTOMER WHERE ACNO={}".format(acn)
    cur.execute(Q)
    R=cur.fetchall()# it will fetch records
    if R:# if there is data in R then it is True otherwise False
        for rec in R:
            print(rec)
        NM=input("Enter NAME: ")
        AD=input("Enter ADDRESS: ")
        PH=input("Enter PHONE: ")

        Q1="UPDATE CUSTOMER SET CNAME='{}', ADDR='{}', MNO='{}' WHERE ACNO={}".format(NM,AD,PH,acn)
        cur.execute(Q1)
        cn.commit()
        print("Record Successfully Updated!!!")
    else:
        print("No Record Found!!!")
    cn.close()


#DELETING DATA
def DELETE_RECORDS():
    cn=con.connect(host="localhost", user="root", passwd="admin", database="BANK")
    cur=cn.cursor()
    ACN=input("Enter ACNO TO BE DELETED: ")
    Q="SELECT * FROM CUSTOMER WHERE ACNO={}".format(ACN)
    cur.execute(Q)
    R=cur.fetchall()
    if R:
        for rec in R:
            print(rec)
        Q="DELETE FROM CUSTOMER WHERE ACNO={}".format(ACN)
        cur.execute(Q)
        cn.commit()
        print("Record Successfully Deleted!!!")
    else:
        print("No Record Found!!!")
    cn.close()


#TRANSACTION
def TRANSACTION():
    cn=con.connect(host="localhost", user="root", passwd="admin", database="BANK")
    cur=cn.cursor()
    ACN=input("Enter ACCOUNT NUMBER: ")
    Q="SELECT * FROM CUSTOMER WHERE ACNO={}".format(ACN)
    cur.execute(Q)
    R=cur.fetchall()
    if R:
        print(R[0])
        TN=input("Enter TRANSACTION NO.: ")
        TDT=input("Enter TRANSACTION DATE: ")
        M=int(input("Enter TRANSACTION MODE [1 for Debit/ 2 for Credit]: "))
        A=int(input("Enter AMOUNT: "))
        B=R[0][4]
        if M==1 and B>=1000:
            fbal=B-A
            Q="INSERT INTO TRANSACTION VALUES({},'{}', {}, {}, '{}', {})\
            ".format(TN, TDT, ACN, A, 'DR', fbal)
            cur.execute(Q)
            cn.commit()
            Q1="UPDATE CUSTOMER SET BAL={} WHERE ACNO={}".format(fbal, ACN)
            cur.execute(Q1)
            cn.commit()
            print("Rs.",A," Successfully Debited from",ACN)
            print("Final Balance: ",fbal)
        if M==2:
            fbal=B+A
            Q="INSERT INTO TRANSACTION VALUES({},'{}', {}, {}, '{}', {})\
            ".format(TN, TDT, ACN, A, 'CR', fbal)
            cur.execute(Q)
            cn.commit()
            Q1="UPDATE CUSTOMER SET BAL={} WHERE ACNO={}".format(fbal, ACN)
            cur.execute(Q1)
            cn.commit()
            print("Rs.",A," Successfully Credited to",ACN)
            print("Final Balance: ",fbal)
    else:    
        print("No Record Found")
    cn.close()

#main program
re='Y'
while re in['Y','y']:
    print("\n\n--------Main Menu--------")
    print("1. ADD RECORD")
    print("2. DISPLAY ALL RECORDS")
    print("3. SEARCH RECORDS")
    print("4. UPDATE RECORDS")
    print("5. DELETE RECORDS")
    print("6. TRANASACTION")
    print("7. EXIT")
    k=int(input("Enter Choice:"))
    if k==1:
        INSERT_RECORDS()
    elif k==2:
        DISPLAY_RECORDS()
    elif k==3:
        SEARCH_RECORDS()
    elif k==4:
        UPDATE_RECORDS()
    elif k==5:
        DELETE_RECORDS()
    elif k==6:
        TRANSACTION()
    elif k==7:
        break
    else:
        print("\n\nInvalid Selection, Please Re-Enter")
    re=input("\n\nWant to Execute again...[Y/y]:")
        
