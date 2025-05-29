import qrcode

link = input("Enter your link: ")
img = qrcode.make(link)
img.save("qr_code.png")
