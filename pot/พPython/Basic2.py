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
root.mainloop()