def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI =weight/(height*height)
    print("BMI= "+ str(BMI))
    if(BMI<18.5):
        print("Under weight")
    elif(BMI>25.0):
        print("Over weight")
    else:
        print("Normal weight")

calculate_bmi(weight=57, height=1.73)
