import sys
import manager

if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    # print(enumerate(sys.argv))
    manager.Manager((sys.argv))

#CREATE DATABASE SAMPLE
#DELETE DATABASE SAMPLE

#FROM SAMPLE CREATE TABLE SAMPLE_TABLE
#FROM SAMPLE DELETE TABLE SAMPLE_TABLE

#CREATE TABLE SAMPLE_TABLE FROM SAMPLE 
#DELETE TABLE SAMPLE_TABLE FROM SAMPLE 




#INSERT INTO SAMPLE_TABLE VALUES (NAME, TYPE)
#INSERT INTO SAMPLE_TABLE VALUES [(NAME, TYPE), ... ]