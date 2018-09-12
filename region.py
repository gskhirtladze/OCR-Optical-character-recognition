import sys
from compare_pixels import same
sys.setrecursionlimit(1500)

def get_block(region_id , st_x , st_y , en_x , en_y , id ) :
    block = [ [ 0 for _ in range(en_y-st_y+1) ] for _ in range(en_x-st_x+1) ]
    density = 0
    for i in range(st_x,en_x+1) :
        for j in range(st_y,en_y+1) :
            if (region_id[i][j] == id) :
                block[i-st_x][j-st_y]=1
                density+=1
    return block,density

def get_regions(luminance):
    
    n_rows = len(luminance)
    n_columns = len(luminance[0])
    
    n_regions = 0
    region_id = [ [0 for _ in range(n_columns)] for _ in range(n_rows) ]
    regions = []

    for i in range(0,n_rows) :
        for j in range(0,n_columns) :
            if (region_id[i][j] == 0) :
                n_regions =  n_regions + 1

                st_x = i 
                st_y = j
                en_x = i
                en_y = j

                queue = [ (i,j) ]
                region_id[i][j] = n_regions
                l=0

                while ( l < len(queue)) :
                    (x,y) = queue[l]
                    l = l +1

                    region_id[x][y] = n_regions

                    if (x < st_x) : st_x=x
                    if (x > en_x) : en_x=x
                    if (y < st_y) : st_y=y
                    if (y > en_y) : en_y=y
                    
                    dx = [ +0 , +0 , +1 , -1 , -1 , -1 , +1 , +1 , -2 , -2 , -2 , +2 , +2 , +2 , -1 , +0, +1 , -1 , +0 , +1 , -2 , -2 , +2 , +2 ]
                    dy = [ -1 , +1 , +0 , +0 , -1 , +1 , +1 , -1 , -1 , +0 , +1 , -1 , +0 , +1 , +2 , +2 ,+2 , -2 , -2 , -2 , -2 , +2 , -2 , +2 ]
                    for dir in range(20) :
                        tox = x + dx[dir]
                        toy = y + dy[dir]
                        if (tox < 0 or toy < 0 or tox >= len(region_id) or toy >= len(region_id[0])) :
                            continue
                        if (region_id[tox][toy] != 0) :
                            continue
                        if ( same(luminance[x][y],luminance[tox][toy]) == False ) :
                            continue
                        region_id[tox][toy] = n_regions
                        queue.append((tox,toy))
                
                current_region , density = get_block(region_id, st_x , st_y , en_x , en_y , n_regions)
                region_size  = len(current_region)*len(current_region[0])
                if (region_size > 250 and region_size < 10000 and density > 50) :
                    regions.append( (current_region,st_x,st_y,en_x,en_y) )
    
    #for i in range(0,n_rows) :
    #    for j in range(0,n_columns) :
    #        print(region_id[i][j]),
    #    print()

    return regions