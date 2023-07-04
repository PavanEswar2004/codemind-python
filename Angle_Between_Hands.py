def cal(time):
    h,m=map(int,time.split(":"))
    ha=(h%12)*30+(0.5*m)
    ma=m*6
    angle=abs(ha-ma)
    return min(angle,360-angle)



time=input()
angle=cal(time)
print(angle)