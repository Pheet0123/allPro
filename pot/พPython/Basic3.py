from tkinter import *
root = Tk()
#ชื่อ
root.title("โปรแกรมแรกของฉัน")
#เปลื่ยน logo 
root.iconbitmap("logos/logo.ico")
#ขนาดปอปอัพที่ขี้นมาตอนแรก
root.geometry("500x500+500+200")
#ทำให้ปรับขนาดปอปอัพไม่ได้
root.resizable(0,0) 
#เปลี่ยนสี bg
root.config(bg="pink")

#แสดงข้อความ
#Label1=Label(root)
#Label1.config(text="สวัสดี")
#Label1.config(font=("Arial",40,"bold"))
#Label1.config(fg="red")
#Label1.config(bg="white")
#เขียนแบบย่อๆได้แบบนี้
Label1=Label(root,text="สวัสดีครับพี่",font=("Arial", 40, "bold"),fg="red",bg="white")
Label1.pack()

Label1=Label(root,text="Python",font=("Arial", 40, "bold"),fg="red",bg="white")
Label1.pack()

Label1=Label(root,text="พสธร ",font=("Arial", 40, "bold"),fg="red",bg="black")
Label1.pack()

root.mainloop()