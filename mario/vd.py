from PIL import Image as img

i1 = img.open("images/Spiny0.png")
i2 = img.open("images/Spiny1.png")

i3 = i1.transpose(img.FLIP_LEFT_RIGHT)
i4= i2.transpose(img.FLIP_LEFT_RIGHT)
i3.save("images/Spiny2.png")
i4.save("images/Spiny3.png")




