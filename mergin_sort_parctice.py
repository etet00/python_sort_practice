# practioce for merge sort
# from little to large

def main():
    num_list = [11, 54, 33, 78, 1, 20, 4, 6, 0, 33, 100, 8]
    sort_list = mergin_sort(num_list)
    print(num_list) 
    print(sort_list)

def mergin_sort(data):
    if len(data) < 2:
        return data
    middle = len(data)//2
    left_part = data[:middle]
    right_part = data[middle:]
    result = mergin(mergin_sort(left_part), mergin_sort(right_part))
    return result

def mergin(left_array, right_array):
    output = []
    while left_array and right_array:
        if left_array[0] < right_array[0]:
            output.append(left_array.pop(0))
        else:
            output.append(right_array.pop(0))
    if len(left_array):
        output = output + left_array
    elif len(right_array):
        output = output + right_array
    return output

if __name__ == "__main__":
    main()
