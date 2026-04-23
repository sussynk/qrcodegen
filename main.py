import qrcode

img = qrcode.make("Hello world")

type(img)

img.save("code.png")