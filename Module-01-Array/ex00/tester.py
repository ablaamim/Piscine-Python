from give_bmi import give_bmi, apply_limit

weight = [165.3, 38.4, 2]
height = [1.7, 1.5, 0.3]

height1 = [1.7, 1.5, 0.3]
weight1 = [165.3, 38.4, -2]

height2 = [1.7, 1.5, 0.3]
weight2 = [165.3, 38.4, 2, 7]

try:
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    # bmi = give_bmi(height1, weight1)
    # print(bmi, type(bmi))
    # print(apply_limit(bmi, 33))
    # bmi = give_bmi(height2, weight2)
    # print(bmi, type(bmi))
    # print(apply_limit(bmi, 33))
except ValueError as e:
    print(f"Error: {e}")
