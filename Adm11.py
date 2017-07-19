import cx_Oracle

class PrintFDDetails:
    
    def __init__(self):
        self.CustId=''
        self.ctr=0
    def SearchFD(self):
        connstr = 'rajat/7417729661@127.0.0.1:1521/XE'
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        
        self.CustId=input('Enter customer id  ');
        
        cursor = conn.cursor()
        cursor.execute("select CID,CFNm,CLNm,sum(FDAmt),sum(loanamt) from loans l ,fddetailsview f where f.accno=l.accno group by cid,cfnm,clnm")
        print "Customer Id \t First Name \t Last Name  \t FD Amount \t Loan amount "
        for column_1, column_2 , column_3, column_4, column_5 in cursor.fetchall():
            self.ctr=self.ctr+1;
            print str(column_1)+"\t\t  "+str(column_2)+"\t\t "+str(column_3)+"\t\t "+str(column_4)+"\t "+str(column_5)            
        if self.ctr==0:
            print 'No such record exists !!! ';
        conn.commit()
        cursor.close()
        conn.close()

