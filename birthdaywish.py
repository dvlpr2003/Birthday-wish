import datetime
import pandas
from smtplib import SMTP
class BirthdayWish :
    def __init__(self):
        self.current_Date  = datetime.date.today()
        self.splitWord = str(self.current_Date).split("-")
        self.splitWord.reverse()
        self.Dob = f"{self.splitWord[0]}-{self.splitWord[1]}-{self.splitWord[2]}"
        self.readFile = pandas.read_csv("./BirthdayList.csv")
        #check DOB to the current DATE
        self.checkDOB = self.readFile[self.readFile["Date of Birth"]==self.Dob]
        self.finalDOB=self.checkDOB.head()


        self.Name =self.finalDOB["Name"]
        self.Email = self.finalDOB["Mail"]
        self.Send_wishes()
        
    def Send_wishes(self):
        Hour = datetime.datetime.now().hour
        Minute = datetime.datetime.now().minute
        Second = datetime.datetime.now().second
        print(Minute)

        for _ in range(len(self.Name)):
                
    
                
                if (Hour == 20) and (Minute == 0) and (Second == 0):

                    with SMTP("smtp.gmail.com") as connection:
                        connection.starttls()
                        connection.login(user="gayathrigaya698@gmail.com",password="lcnm qida weeq nxxn")
                        connection.sendmail(from_addr="gayathrigaya698@gmail.com",to_addrs=f"{self.Email[_]}",msg=f"Subject:{'Birthday Wishes'}\n\nHappy birthday {self.Name[_]}\n fuck you da")
                                    