import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        "authorization": 'QgoIqtMwyiHk8JaVDfl3G51ZxSYW2CvAmPbB0FpsnXu79TeOjEMpVNfxtaHTYKjUsAbum4qJEZRzGXQg',
        "sender_id":'TXTIND',
        "message":message,
        "language": 'english',
        "route": 'v3',
        "numbers": number
    }
    response = requests.get(url,params=params)
    a = response.json()
    # print(a)
    return a.get("return")


def Btnclick():
    num = TextNumber.get()
    msg = TextMsg.get("1.0",END)
    r = send_sms(num,msg)
    if r:
        showinfo("send success","sucessfully sent")
    else:
        showerror("something went wrong")


###creating GUI

root = Tk()

root.title("message sender")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
TextNumber  = Entry(root,font=font)
TextNumber.pack(fill=X,pady=20)
TextMsg = Text(root)
TextMsg.pack(fill=X,pady=10)
sendBtn = Button(root,text="send message",command=Btnclick)
sendBtn.pack()


root.mainloop()


