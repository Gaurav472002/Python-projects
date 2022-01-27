import datetime
# def send_wpmsg(numberwp,messagewp,strTime):
#     code="+91"
#     final_number=code+numberwp

#     a1= strTime.split(" ")
#     hours=int(a1[0])
#     minutes=int(a1[1])

#     pywhatkit.sendwhatmsg(final_number,messagewp,hours,minutes)
    


actTime = datetime.datetime.now().strftime(f"%H %M") 
a1= actTime.split(" ")
hours=int(a1[0])
minutes=int(a1[1])

minutes+=2
print(hours)
print(minutes)
