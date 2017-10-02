def quick_sort(lists, left=0, right=None):
    if right is None:
        right = len(lists) - 1
    if left >= right:
        return lists

    key = lists[left]
    low = left
    high = right

    while left < right:

        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]

        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key

    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)

    return lists


test = eval(input('please input a list: '))
print(quick_sort(test))