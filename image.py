from PIL import Image


img = Image.open("./sample_data/cut_images/Tshirt.New/AOP Tshirt Neck Front.png")
newsize =(1000,1000)
img = img.resize(newsize)
img.save("./sample_data/cut_images/Tshirt.New/AOP Tshirt Neck Front.png")