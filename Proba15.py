w = 17391%17
f = 546%17
v = 934%17

if w < f and w < v:
    print( w,"Самый маленький остаток")
elif f < w and f < v:
    print( f, "Самый маленький остаток")
elif v < w and v < f:
    print( v, "Самый маленький остаток")
else:
    print("Все ответы не верны")