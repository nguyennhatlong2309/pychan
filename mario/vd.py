from PIL import Image
import random

# Load background
i1 = Image.open("images/Mario - Climb1.png")
i2 = Image.open("images/Mario - Climb2.png")
i3 = Image.open("images/Super Mario - Climb1.png")
i4 = Image.open("images/Super Mario - Climb2.png")
i5 = Image.open("images/Fiery Mario - Climb1.png")
i6 = Image.open("images/Fiery Mario - Climb2.png")

i7 = i1.transpose(Image.FLIP_LEFT_RIGHT)
i8=i2.transpose(Image.FLIP_LEFT_RIGHT)
i9=i3.transpose(Image.FLIP_LEFT_RIGHT)
i10=i4.transpose(Image.FLIP_LEFT_RIGHT)
i11=i5.transpose(Image.FLIP_LEFT_RIGHT)
i12 = i6.transpose(Image.FLIP_LEFT_RIGHT)


