def luminance(RGB):
    return float(0.2126*RGB[0] + 0.7152*RGB[1] + 0.0722*RGB[2])

def get_luminance(image , n_rows , n_columns):
    lum=[[0.0 for _ in range(0,n_columns)] for _ in range(0,n_rows)]

    for i in range(0,n_rows) :
        for j in range (0,n_columns) :
            R = float(image[i][j][0])
            G = float(image[i][j][1])
            B = float(image[i][j][2])
            lum[i][j] = ( luminance ( image[i][j] ) , ( R , G , B))

    return lum

