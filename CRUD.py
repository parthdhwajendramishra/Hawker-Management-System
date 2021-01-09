import mysql.connector





#Function to create Table
def studentData():
        con = mysql.connector.connect(host="localhost",user="root",passwd="atalji",database="project",auth_plugin='mysql_native_password')
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS data(hid integer primary key AUTO_INCREMENT,fname VARCHAR(25),mname VARCHAR(25),lname VARCHAR(25),gender VARCHAR(10),ph1 VARCHAR(20),ph2 VARCHAR(20),address VARCHAR(50),area VARCHAR(50))")
        
        cur.execute("CREATE TABLE IF NOT EXISTS transaction(hid integer ,day date, dtime time, q1 integer,r1 integer, q2 integer, r2 integer, q3 integer, r3 integer,q4 integer, r4 integer, q5 integer, r5 integer,amount integer, deposit integer)")
        con.commit()
        con.close()    
        
#Function to insert Data               
def insert_1(hid,fname,mname,lname,gender,ph1,ph2,address,area):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="atalji",database="project",auth_plugin='mysql_native_password')
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(hid,fname,mname,lname,gender,ph1,ph2,address,area))
        con.commit()
        con.close() 


#Function to view all Data   
def viewall_1():
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="atalji",database="project",auth_plugin='mysql_native_password')
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT *FROM data")
        row=cur.fetchall()
        con.close()       
        return row
        
#Function to delete Data   
def delete_1(hid):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="atalji",database="project",auth_plugin='mysql_native_password')
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("DELETE FROM data WHERE hid=%s",(hid,))
        con.commit()
        con.close()         
        

#Function to search Data       
def search_1(hid,fname,mname,lname,gender,ph1,ph2,address,area):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="atalji",database="project",auth_plugin='mysql_native_password')
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT * FROM data WHERE hid=%s or fname=%s or mname=%s or lname=%s or gender=%s or ph1=%s or ph2=%s or address=%s or area=%s",(hid,fname,mname,lname,gender,ph1,ph2,address,area))
        rows=cur.fetchall()
        con.close()        
        return rows
        
        
#Function to update Data      
def update_1(hid,fname,mname,lname,gender,ph1,ph2,address,area):
        con = mysql.connector.connect(host="localhost",user="root",passwd="atalji",auth_plugin='mysql_native_password')
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("UPDATE data SET fname=%s,mname=%s,lname=%s,gender=%s,ph1=%s,ph2=%s,address=%s,area=%s WHERE hid=%s",(fname,mname,lname,gender,ph1,ph2,address,area,hid))
        con.commit()
        con.close()   
        
