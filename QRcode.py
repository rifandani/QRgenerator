import qrcode

f = qrcode.make(f'url')  # replace url with your url
f.save('output.png')  # enter your file name
