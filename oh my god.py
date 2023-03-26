#these arbitrary value lists i stg im gonna get carpel tunnel if i keep manually
#doing them so im going to automate it

for i in range(500,700,10):
    g=str(i/100)
    if len(g)==3: g=g+'0'
    print(g)
