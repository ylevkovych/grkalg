def reverse_array(list):

    start = 0
    end = len(list)-1

    while start < end:

        buf = list[start]

        list[start] = list[end]
        list[end] = buf


        start += 1
        end -= 1


my_list = [1,2,3,4,5]

reverse_array(my_list)

print my_list

