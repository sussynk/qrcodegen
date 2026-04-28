import qrcode

context = input(str("Content: "))

img = qrcode.make(context)

type(img)

img.save("code.png")