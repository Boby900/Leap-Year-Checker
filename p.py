def Is_LeapYear(value):
    if value % 4 == 0:
        if value % 100 == 0:
            if value % 400 == 0:
                print("leap year")
            else:
                print("not a leap year")
        else:
            print("leap year")
    else:
        print("not a leap year")

Is_LeapYear(2001)
