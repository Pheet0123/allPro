import qrcode



qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)
qr.add_data("https://github.com/Thxe-01/Web_Portforlio")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white" )
img.save("พอตไอ้ธี-git.png")






























#img = qrcode.make("ขี้เสือกจังอ่ะแกกกกกกกกกกกกก")
#img.save("จุดจุด.png")

