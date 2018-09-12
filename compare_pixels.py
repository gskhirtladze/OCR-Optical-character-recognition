def same( pixel_A , pixel_B ) :
    (B_A,(AR,AG,AB)) = pixel_A
    (B_B,(BR,BG,BB)) = pixel_B
    
    #if (abs(B_A-B_B)) > 25 :
    #    return False
    #return True
    R = abs((AR-BR))
    G = abs((AG-BG))
    B = abs((AB-BB))


    diff = 0.2126*R + 0.7152*G + 0.0722*B

    if diff < 15 :
        return True

    return False
