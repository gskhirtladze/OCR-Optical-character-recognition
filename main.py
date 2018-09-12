from brightnest import get_luminance
from region import get_regions

image_path = "sampleImage/4.jpg" #raw_input("Enter Image path:")
luminance = get_luminance(image_path)
regions = get_regions(luminance)

print(len(regions))
for x in range(len(regions)) :
    (now,aa,bb,cc,dd)=regions[x]
    print(aa,bb)
    for i in range (len(now)) :
        string =""
        for j in range(len(now[0])) :
            if (now[i][j]) :
                string="".join((string,str(int('0')+int(now[i][j]))))
            else :
                string="".join((string," "))
        print (string)
    next = ""
    raw_input()
    
    print("  ")
