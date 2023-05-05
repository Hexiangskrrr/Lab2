import statistics
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to python")
    display_main_menu()
    num_list = get_user_input()
    print("avg: ", calc_average(num_list))
    print("min is: ", find_min_max(num_list)[0])
    print("max is: ", find_min_max(num_list)[1])
    sorted_num_list = sort_temperature(num_list)
    print("temperature in ascending order: ", sorted_num_list)
    print("median temperature: ", calc_median_temperature(sorted_num_list), "C")
def display_main_menu():
    print("Enter some numbers seperated by commas (eg. 5, 67, 32)")
def calc_average(x):
    avg = sum(x)/len(x)
    return avg
def get_user_input():
    num = input("Enter number: ")
    num_split = num.split(",")
    num_split = [float(i) for i in num_split]
    return num_split
def find_min_max(x):
    minimum = min(x)
    maximum = max(x)
    return minimum, maximum
def sort_temperature(x):
    x.sort()
    return x
def calc_median_temperature(x):
    median = statistics.median(x)
    return median
if __name__ == "__main__":
    main()






