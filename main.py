# Desktop notifier using python

from plyer import notification
import time

if __name__ == '__main__':
    
  while True:
        
      notification.notify(title="*** Take Rest ***", 
                          message = "Rest days are just as important as  exercise. In fact, a successful fitness regimen isn’t complete without rest days.",
                          #app_icon = "",
                          timeout=5)
      time.sleep(10)
      #time.sleep(3600)