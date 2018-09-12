def sort_regions(regions) :
    for i in range(len(regions)) :
        for j in range(i+1,len(regions)) :
            (a,stx1,sty1,enx1,eny1) = regions[i]
            (b,stx2,sty2,enx2,eny2) = regions[j]
            if ((stx1+enx1)/2 > enx2) :
                regions[i],regions[j] = regions[j],regions[i]
                continue
            if ((stx2+enx2)/2 < stx1) :
                regions[i],regions[j] = regions[j],regions[i]
                continue
            if ((stx2+enx2)/2 > enx1) :
                continue
            if ((stx1+enx1)/2 < stx2) :
                continue
            if ((sty1+eny1)/2 > eny2) :
                regions[i],regions[j] = regions[j],regions[i]
                continue
            if ((sty2+eny2)/2 < eny1) :
                regions[i],regions[j] = regions[j],regions[i]
                continue
            if ((sty2+eny2)/2 > eny1) :
                continue
    return regions
