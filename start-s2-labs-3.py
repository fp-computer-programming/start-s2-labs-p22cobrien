# Author: CMOB 1/24/2022

def comes_after(st, l): 
    new_lst = []
    for i,c in enumerate(st):
        if i == 0: continue
        if (st[i-1] == l.lower() or st[i-1] == l.upper()) and c.isalpha():
            new_lst.append(c)
    return ''.join(new_lst)
    