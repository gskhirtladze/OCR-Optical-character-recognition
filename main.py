from brightnest import get_luminance
from region import get_regions
from sort import sort_regions
from compare_pixels import same
from get_image import get_image

image_path = "sampleImage/gvanca2.jpg" #raw_input("Enter Image path:")
image,n_rows,n_columns = get_image(image_path)
luminance = get_luminance(image,n_rows,n_columns)
regions = get_regions(luminance)

regions = sort_regions(regions)

print(len(regions))
for x in range(len(regions)) :
    (now,aa,bb,cc,dd)=regions[x]
    print(aa,bb)
    for i in range (len(now)) :
        string =""
        for j in range(len(now[0])-340,len(now[0])-124) :
            if (now[i][j]) :
                string="".join((string,str(int('0')+int(now[i][j]))))
            else :
                string="".join((string," "))
        print (string)
    next = ""
    raw_input()
    
    print("  ")

