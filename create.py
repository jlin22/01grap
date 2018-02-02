file = open("image.ppm", "w");

#write first three lines
file.write("P3\n500 500\n255\n")

#write 255 0 255 for each pixel
for num1 in range(0,500):
    for num2 in range(0,500):
        file.write((str)(num1 / 2 % 256) + " 0 " + (str)(num2 / 2 % 256) + " ")

    
