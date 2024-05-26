#First install psycopg2 using pip install psycopg2 &
#pip install psycopg2-binary

import psycopg2 as pg
dbname = input("Enter name of your database : ")    
conn = pg.connect(host = "localhost",database = dbname,user = "postgres",password = "srk27")
cur = conn.cursor()

table_name = input("Enter table name : ")

while True:

    print("\n1. Add new row\n2. Update using NId\n3. Delete using NId\n4. Print all rows\n5. Exit")
    choice = int(input("Enter a choice number : "))

    if choice == 1:
        ninjaid = input("Enter a NId : ")
        ninjaname = input("Enter a NName : ")
        ninjarank = input("Enter a NRank : ")
        ninjaseniority = input("Enter a NSeniority : ")
        ninjaage = input("Enter a NAge : ")
#        qry = "INSERT INTO " + table_name + " (nid, nname, nrank, nseniority, nage) VALUES (%s, %s, %s, %s, %s);"
        qry = "INSERT INTO " + table_name + " VALUES (%s, %s, %s, %s, %s);"
        cur.execute(qry, (ninjaid, ninjaname, ninjarank, ninjaseniority, ninjaage))
        conn.commit()
        print("New row has been created.")

    elif choice == 2:
        print("\n1. Update NId\n2. Update Name using NId\n3. Update Rank using NId\n4. Update Seniority using NId\n5. Update Age using NId")
        ch = int(input("Enter a choice number : "))
        if ch == 1:
            new_ninjaid = input("Enter a new NId : ")
            old_ninjaid = input("Enter a old NId : ")
            qry = "UPDATE "+table_name+ " SET NId = %s WHERE NId = %s;"
            cur.execute(qry,(new_ninjaid,old_ninjaid))
            conn.commit()
            print("The Table is updated.")
        elif ch == 2:
            ninjaid = input("Enter an NId to search in table : ")
            new_ninjaname = input("Enter a new NName : ")
            qry = "UPDATE "+table_name+ " SET NName = %s WHERE NId = %s;"
            cur.execute(qry,(new_ninjaname,ninjaid))
            conn.commit()
            print("The Table is updated.")
        elif ch == 3:
            ninjaid = input("Enter an NId to search in table : ")
            new_ninjarank = input("Enter a new NRank : ")
            qry = "UPDATE "+table_name+ " SET NRank = %s WHERE NId = %s;"
            cur.execute(qry,(new_ninjarank,ninjaid))
            conn.commit()
            print("The Table is updated.")
        elif ch == 4:
            ninjaid = input("Enter an NId to search in table : ")
            new_ninjaseniority = input("Enter a new NSeniority : ")
            qry = "UPDATE "+table_name+ " SET NSeniority = %s WHERE NId = %s;"
            cur.execute(qry,(new_ninjaseniority,ninjaid))
            conn.commit()
            print("The Table is updated.")
        else:
            ninjaid = input("Enter an NId to search in table : ")
            new_ninjaage = str(input("Enter a new NAge : "))
            qry = "UPDATE "+table_name+ " SET NAge = %s WHERE NId = %s;"
            cur.execute(qry,(new_ninjaage,ninjaid))
            conn.commit()
            print("The Table is updated.")

    elif choice == 3:
        print("\n1. Delete NId\n2. Delete Entire table")
        ch = int(input("Enter a choice number : "))
        if ch == 1:
            ninjaid = input("Enter a NId to be deleted : ")
            qry = "DELETE FROM "+table_name+" WHERE NId = %s;" 
            cur.execute(qry,(ninjaid))
            conn.commit()
            print("The Table is updated.")
        elif ch ==2:
            confirm = input("Press Y to yes N to no : ")
            if confirm.upper() == 'Y':
                qry = "DELETE FROM "+table_name+";"
                cur.execute(qry)
                conn.commit()
                print("The Table is updated.")
            else:
                continue
        else:
            print("Invalid choice")

    elif choice == 4:
        cur.execute("SELECT * FROM NinjaDb")
        rows = cur.fetchall()
        for row in rows:
             print(row)
    elif choice == 5:
        break
    else :
        print("Invalid choice")
    
conn.commit()
conn.close()