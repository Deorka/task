def unique_number_to_good_number():
    s = input()
    arr = s.split("/")
    for i in range(0..len(arr)-2):
        arr1 = arr[i]
        arr2 = arr[i+1]
        s2 = frag_2_number(arr2)
        if s2 != "false":
            if arr1[len(arr-1)].isnumeric():
                if arr1[len(arr - 2)].isnumeric():
                    if arr1[len(arr - 3)].isnumeric():
                        if arr1[len(arr - 4)].isnumeric():
                            print(arr1[len(arr - 4):] + "/" + s2)
                        else:
                            print("0" + arr1[len(arr - 3):] + "/" + s2)
                    else:
                        print("00" + arr1[len(arr - 3):] + "/" + s2)


def frag_2_number(arr2):
    if arr2[0].isnumeric():
        if arr2[1].isnumeric():
            if arr2[2].isnumeric():
                if arr2[3].isnumeric():
                    if arr2[4].isnumeric():
                        return arr2[:4]
                    else:
                        return "0" + arr2[:3]
                else:
                    return "00" + arr2[:2]
            else:
                return "000" + arr2[:1]
    return "false"
