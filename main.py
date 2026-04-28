import qrcode

context = str(input("Content: "))

print("Select file format:")
print("[1] JPG")
print("[2] PNG")
print("[3] WEBP")

file_format_selection = int(input("File format: "))

if file_format_selection == 1:
    file_format = "jpg"
elif file_format_selection == 2:
    file_format = "png"
elif file_format_selection == 3:
    file_format = "webp"
else:
    print("Invalid selection")

img = qrcode.make(context)

file_name = str(input("File name: "))

type(img)

img.save(f"{file_name}.{file_format}")

print("QR Code Generated successfully! Thank you for using me.")