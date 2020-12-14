import win10toast
import time
import winsound

toaster = win10toast.ToastNotifier()

while True:
    time.sleep(1200)
    toaster.show_toast("20-20-20", "Take a rest for 20 seconds!!", icon_path="Eye.ico", duration=10)
    time.sleep(20)
    winsound.PlaySound("MailSound.wav", winsound.SND_ASYNC)

