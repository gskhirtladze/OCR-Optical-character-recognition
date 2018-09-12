import scipy.misc as misc

def luminance(RGB):
    return 0.2126*RGB[0] + 0.7152*RGB[1] + 0.0722*RGB[2]


def get_luminance(image_path):
    image = misc.imread(image_path)
    n_rows = len(image)
    n_columns = len(image)
    lum=[[0.0 for _ in range(0,n_rows-1)] for _ in range(0,n_columns-1)]

    print ( luminance(image[0][0]))
    for i in range(0,n_rows-1) :
        for j in range (0,n_columns-1) :
            lum[i][j] = luminance ( image[i][j] )

    return lum

b = get_luminance("sampleImage/2.png")
print(b)
