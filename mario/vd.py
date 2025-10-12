from PIL import Image as img

i1 = img.open("images/Hammer0.gif")
i2 = i1.rotate(-90, expand=True)
i3 = i2.rotate(-90, expand=True)
i4 = i3.rotate(-90, expand=True)

i2.save("images/Hammer1.gif")
i3.save("images/Hammer2.gif")
i4.save("images/Hammer3.gif")





