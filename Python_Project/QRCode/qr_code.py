import qrcode


# --------------------Simple code ----------------------------------------
# img = qrcode.make("https://www.google.com/maps/place/Telecom+Layout/@12.3060466,76.603675,17z/data=!3m1!4b1!4m6!3m5!1s0x3baf7adcaeaaaaab:0xf51c19dd9291a11f!8m2!3d12.3060466!4d76.6062499!16s%2Fg%2F11sskrk0vs?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D")
# img.save("youtube_qrcode.png")


# ----------- Advanced code ------------------
qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.ERROR_CORRECT_H,
                    box_size=10,border=4
                )
qr.add_data("https://www.google.com/search?q=south+korea&rlz=1C5CHFA_enIN949IN949&oq=south+korea&gs_lcrp=EgZjaHJvbWUqBwgAEAAYjwIyBwgAEAAYjwIyCggBEC4YsQMYgAQyDAgCECMYJxiABBiKBTIKCAMQABixAxiABDIKCAQQABixAxiABDIKCAUQABixAxiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiPAtIBCDcyMzhqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8")

qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("place_qrcode.png")