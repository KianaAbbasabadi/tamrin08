import re
from datetime import datetime

def financail_validator(user):
    errors=[]
    if not (type(user[0])==int and user[0]>0):
     errors.append(" id must be an integer>0")

    if not (type(user[1])==int and user[0]>=0):
     errors.append(" Amount must be an integer>0")


     if not re.match(r"^\d{4}-\d{2}-\d{2}$" , user[2]):
        errors.append("date must be like : YYY-MM-DD ")

    if not re.match(r"^\d{2}:\d{2}:\d{2}$" , user[3]):
       errors.append("time must be like : HH:MM:SS")    



    if not (type(user[5])==str and re.match(r"^[a-zA-Z\s]{3,30}$" , user[5])):
        errors.append("description is invalid")


    return errors   

    