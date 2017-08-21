def zellers(m, d, y):
    k=y % 100
    j=y/100
    h=(int)(d+((13*(m+1))/5)+k+(k/4)+5-j)%7
    return round(h)
day_dict={0:"saturday",1:"sunday",2:"monday",3:"tuesday",4:"wednesday",5:"thursday",6:"friday"}
month_dict={"january":13,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
day=int(input("Enter day:"))
month=input("Enter month:")
year=int(input("Enter year:"))
h=zellers(month_dict.get(month),day,year)
print(day_dict.get(h))
