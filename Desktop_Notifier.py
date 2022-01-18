#using plyer module we are going to create a desktop notifier for drinking water

import time

from plyer import notification

if __name__=="__main__":
    while True:
    
        notification.notify(
            title= "Please Drink water",
            message=" Average need of  for a human Body is 3.5 L/day",
            app_icon="E:\Programming---Codes\Python Projects\gw.ico",
            timeout=2
            
            )
        time.sleep(6)