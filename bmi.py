def calculate_bmi(height, weight):
    #print("Height = " + str(height))
    #print("Weight = " + str(weight))
    BMI =weight/(height*height)
    #print("BMI= "+ str(BMI))
    checking = 0
    if(BMI<18.5):
        checking = -1
        #print("Under weight")
    elif(BMI>25.0):
        checking = 1
        #print("Over weight")
    else:
        #print("Normal weight")
        checking = 0
    return checking

print(calculate_bmi(weight=99   , height=1.73))

