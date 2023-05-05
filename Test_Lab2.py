import Lab2

def test_find_min_max():
    input_arr = [5, 10, 12, 19, 29, 2]
    result = Lab2.find_min_max(input_arr)
    assert(result[0] == 2 and result[1] == 29)

def test_calc_average():
    input_arr = [2,4,6,8]
    result = Lab2.calc_average(input_arr)
    assert(result == 5)

def test_calc_median_temperature():
    input_arr = [2,4,6,8,10]
    result = Lab2.calc_median_temperature(input_arr)
    assert(result == 6)