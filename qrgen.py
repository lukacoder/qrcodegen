import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
print("--------------------------------------")
print("")
print("")
print("                 KEDY CODER           ")
print("")
print("")
print("--------------------------------------")
qr_gene = input("Qr Code Web Url ->>>>")
qr.add_data(qr_gene)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img = qrcode.make(qr_gene)
type(img)
img.save("some_file.png")
