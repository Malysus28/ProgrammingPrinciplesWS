
#THIS IS THE FILE TO DEAL WITH IN Q 3

from math import sqrt

def get_coord(two_letters):
    l0 = two_letters[0]
    l1 = two_letters[1:]

    if l0 < 'A' or l0 > 'Z' or len(two_letters) > 3 or (not l1.isdigit()):
        print("Bad reference:", two_letters)
        exit()
    else:
        if 1 > int(l1) or int(l1) > 26:
            print("Bad reference:", two_letters)
            exit()
    return (ord(l0) - ord("A"), int(l1) - 1)

ref_list = list(input("Enter trip map references:").split())
len_ref = len(ref_list)
total_len = 0

for i in range(len_ref - 1):
    (x0, y0) = get_coord(ref_list[i])
    (x1, y1) = get_coord(ref_list[i + 1])
    total_len = total_len + 0.5 * sqrt((y1 - y0)**2 + (x1 - x0)**2)

print("Total distance = {:.1f} km".format(total_len))
