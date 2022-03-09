
def my_func(x1, x2, x3):
    if(type(x1)!=float or type(x2)!=float or type(x3)!=float ):
        return "Error: parameters should be float"
    if(x1+x2+x3==0):
        return "Not a number – denominator equals zero"
    value = ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
    return float(value)

#print(my_func(1.0,2.0,-3.0))

def convert(hours, minutes):
    if(hours<0 or minutes<0):
        return "Input error!"

    seconds = hours*3600+minutes*60
    return(seconds)
