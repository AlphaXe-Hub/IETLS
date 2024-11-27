# We import WindowsToaster and a toast format we want
from windows_toasts import WindowsToaster, Toast
import time

def notification(word):
    # Prepare the toaster for bread (or your notification)
    toaster = WindowsToaster('IETLS')
    # Initialise the toast
    newToast = Toast()
    # Set the body of the notification
    # for i in (0,10):
    newToast.text_fields = word
    # And display it!
    toaster.show_toast(newToast)

with open('IELTS.txt', 'r',encoding='utf-8') as file: 
    lines = file.readlines() 
    for line in lines: 
        print(line)
        notification(list(filter(None,line.split('%'))))
        time.sleep(60)


