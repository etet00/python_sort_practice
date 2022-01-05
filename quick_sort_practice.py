# practioce for merge sort
# from little to large

def main():
    num_list = [11, 54, 33, 78, 1, 20, 4, 6, 0, 33, 100, 8]
    sort_list = quick_sort(num_list)
    print(num_list) 
    print(sort_list)

def quick_sort(array):
    if  len(array) <= 1:
        return array
    ref_value = array.pop(0)
    left_part = []
    right_part = []
    for i  in array:
        if i <= ref_value:
            left_part.append(i)
        else:
            right_part.append(i)
    array = quick_sort(left_part) + [ref_value] + quick_sort(right_part)
    return array


if __name__ == "__main__":
    main()
