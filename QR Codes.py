import qrcode

# define the data to encode in the QR code
data = "url of website"

# create a QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# add the data to the QR code
qr.add_data(data)

# compile the QR code
qr.make(fit=True)

# generate an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# save the image to a file
img.save("example_qr.png")


#pip install qrcode