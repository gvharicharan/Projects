import qrcode

image=qrcode.make("www.twitter.com/gvharicharan")

image.save("Twitterqrcode.png")