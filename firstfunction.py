def computepay(h,r):
    if h>=40.0:
        pay = ((h-40.0)*1.5*r)+(40.0*r)
    else:
        pay = h*r
    return pay

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))

p = computepay(hrs,rate)
print p