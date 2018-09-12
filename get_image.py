import scipy.misc as misc

def get_image(image_path) :
    image = misc.imread(image_path)
    n_rows = len( image )
    n_columns = len( image[0] )
    return (image , n_rows , n_columns)