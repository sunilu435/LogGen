import os
import datetime


# Beginning 
def generateLog(count):
    print("Log generation started...")
    # Creates a new file
    fp = open('log_generate.log', 'w')
    for i in range(0,count,1) :
        log_str = str(datetime.datetime.now()) + " MESSAGE ERRORCODE GET PATH" # Log format Module
        fp.write(str(log_str))
        fp.write("\n")
    print("Log Generation Completed!!")

ip = int(input("Enter number of rows: "))
generateLog(ip)