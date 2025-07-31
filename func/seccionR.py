
import matplotlib.pyplot as plt

def sec_rectangular(ax1, b=1, h=1, netiqueta=False):
    yy = b/2
    zz = h/2
    coord = [
        [1, -yy, -zz], 
        [2, -yy, +zz], 
        [3, +yy, +zz],
        [4, +yy, -zz],
        [1, -yy, -zz] # coordenada adicional
    ];
    coord_id, xs, ys = zip(*coord) #create lists of x and y values
    
    ax1.fill(xs,ys, color="#333", facecolor="#2df", edgecolor='b') #fccc7c
    
    auxx, auxy = [], []
    for i in range(len(coord_id)-1):
        auxx.append(coord[i][1])
        auxy.append(coord[i][2])
    ax1.plot([max(auxx)+0.1*h, max(auxx)+0.1*h], [min(auxy), max(auxy)], 'r-d') # haltura
    ax1.text( (max(auxx)+0.1*h + max(auxx)+0.1*h)/2, (min(auxy) + max(auxy))/2, f"{h}", fontsize=10, color='b')
    ax1.plot([min(auxx), max(auxx)], [max(auxy)+0.15*b, max(auxy)+0.15*b], 'r-d') # base
    ax1.text( (min(auxx) + max(auxx))/2, (max(auxy)+0.2*b + max(auxy)+0.2*b)/2, f"{b}", fontsize=10, color='b')
    del (auxx, auxy)
    
    # ax1.grid(True, linestyle='-.')
    ax1.tick_params(labelcolor='g', labelsize='medium', width=2)
    ax1.plot([0],[0],'ms')
    ax1.axvline(0, linewidth=1, linestyle='--', color='r')
    ax1.axhline(0, linewidth=1, linestyle='--', color='r')
    
    if netiqueta:
        for i in range(len(xs)):
#             ax1.text(coord[i][1],coord[i][2], f"{str(coord[i][0])}", fontsize=10, color='b')
            ax1.text(coord[i][1],coord[i][2], f"({coord[i][1]},{coord[i][2]})", fontsize=10, color='#377c74')
    del (b,h,coord, coord_id, xs, ys, netiqueta)
    # return ax1