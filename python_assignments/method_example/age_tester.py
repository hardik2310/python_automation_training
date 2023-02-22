def age_test(person_age):
    keys = list(person_age.keys())
    values = list(person_age.values())
    if values[0] == values[1] and values[1] == values[2]:
        print("All person's", keys,  "age is same:", person_age['smith'])
    elif values[0] > values[1] < values[2]:
        print('Yongest person is : ', keys[1], ', with age : ', values[1])
    elif values[1] > values[0] < values[2]:
        print('Yongest person is : ', keys[0], ', with age : ', values[0])
    else:
        print('Yongest person is : ', keys[2], ', with age : ', values[2])
