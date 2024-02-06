from datetime import datetime,date
from smtplib import SMTP
with open ("./birthday_list.txt","r") as file:
    Birthday = file.readlines()

name = []
date_of_birth = []
mail = []
for _ in Birthday:
    spl1 = _.split(",")
    name.append(spl1[0])
    Extract_dob = spl1[1].split("-")
    date_of_birth.append(Extract_dob)
    mail.append(spl1[2])


condition = False 
while not condition:
    for _ in range(len(date_of_birth)):
        year = date_of_birth[_][0]
        month = date_of_birth[_][1]
        day = date_of_birth[_][2]
        Date = date(year=int(year),day=int(day),month=int(month))
        currentDt = datetime.today()
        if currentDt.date() == Date:
            with SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="gayathrigaya698@gmail.com",password="lcnm qida weeq nxxn")
                connection.sendmail(from_addr="gayathrigaya698@gmail.com",to_addrs=f"{mail[_]}",msg=f"Subject:{'Birthday Wishes'}\n\nHappy birthday {name[_]}")
            condition = True
        else:
            continue
            
            


