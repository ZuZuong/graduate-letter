import qrcode

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data("https://graduate-letter-three.vercel.app/")
qr.make(fit=True)
qr.make_image(fill_color="#8B2D5B", back_color="white").save("qr-thiep.png")