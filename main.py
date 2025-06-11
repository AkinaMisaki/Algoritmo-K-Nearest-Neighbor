import math

data = [
[120, 10, 3, 250, 'P1'],
[200, 25, 5, 400, 'P2'],
[80, 5, 2, 180, 'P1'],
[300, 30, 6, 500, 'P3'],
[250, 40, 7, 600, 'P3'],
[150, 12, 4, 320, 'P2'],
[90, 8, 3, 200, 'P1'],
[310, 35, 6, 520, 'P3'],
[170, 15, 4, 350, 'P2'],
[85, 6, 2, 190, 'P1'],
[220, 18, 5, 410, 'P2'],
[305, 38, 6, 510, 'P3'],
[130, 11, 3, 270, 'P1'],
[260, 42, 7, 580, 'P3'],
[160, 14, 4, 330, 'P2'],
[100, 9, 2, 210, 'P1'],
[240, 28, 6, 460, 'P3'],
[180, 16, 4, 370, 'P2'],
[95, 7, 2, 195, 'P1'],
[270, 40, 6, 590, 'P3']
]

find = [
[110, 9, 3, 220],
[190, 17, 4, 380],
[275, 36, 6, 540],
[140, 13, 3, 300],
[230, 20, 5, 430]
]


dist = 0
min_dist = float('inf')
closest_pair = None
i = 0


for f in find:
    for d in data:
        dist = math.sqrt((f[0] - d[0])**2 + (f[1] - d[1])**2 + (f[2] - d[2])**2 + (f[3] - d[3])**2)
        #print(f"Distância entre {f} e {d[:-1]}: {dist:.2f}") - Usado para debugging
        if dist < min_dist:
            #print(f"Nova menor distância encontrada: {dist:.2f} entre {f} e {d[:-1]}") - Usado para debugging
            min_dist = dist
            closest_pair = (f, d)
            try:
                find[i][4] = ''.join(d[-1])
            except IndexError:
                f.append(d[-1])
    print(f"Menor distância encontrada: {min_dist:.2f} entre {closest_pair[0]} e {closest_pair[1]}")
    i += 1
    dist = 0  
    min_dist = float('inf') 


print(find)
