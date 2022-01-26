import pandas as pd
import datetime
import smtplib
import os
os.chdir(r"E:\Programming---Codes\Python Projects\Automatic Birthday Wisher")
os.mkdir("testing") 

# Enter your authentication details
GMAIL_ID = 'gauravgamessoftwares@gmail.com'
GMAIL_PSWD = 'gaurav472002'


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()
    

if __name__ == "__main__":
    #just for testing
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_excel("bday_data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(type(today))
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday) 
        if(today == bday) and yearNow not in str(item['Year']):
            
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue']) 
            writeInd.append(index)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow) # adding the year in which the program has already wished
        # print(df.loc[i, 'Year'])

    # print(df) 
    df.to_excel('bday_data.xlsx', index=False)   # command to rewrite the data in excel file