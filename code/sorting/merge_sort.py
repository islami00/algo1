from typing import List


def constant_slice(a_list: List, start: int, end: int):
    """
    Slices a list from the start index to the index before the end index.
    Regardless of the range, this slicing operation takes O(k) , k is end - start - how many times we recurse

    determined by how many append operations we perform.
    :param a_list: List to slice
    :param start: index value to start from
    :param end: index value to stop before
    :return: sliced list
    """

    n = []
    while start < end:
        n.append(a_list[start])
        start += 1
    return n


# divide step - split
def split(a_list: List):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(k log n) time


    Because python's slice operation runs in O(k) time, our split irl runs in O(k log n) in addition to its natural O(log n) -  see how we multiply nested steps?
    In this case, it is because there is a slice operation for each split
    :param a_list:  List
    :return: [left : List, right: List]
    """
    # floor to avoid including non-existing index, no mid in left due to zero-indexing. Left > right for odd numbers
    # (splitting has to be uneven in this case)

    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]
    return [left, right]


def merge(left: List, right: List):
    """
    Merges two lists (arrays), sorting them in the process and returns a new merged list.

    Runs in overall O(n) time
    :param left:
    :param right:
    :return: merged list :  List
    """

    copy_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            copy_list.append(left[i])
            i += 1
        else:
            copy_list.append(right[j])
            j += 1

    # uneven lists. assume sort complete
    while i < len(left):
        copy_list.append(left[i])
        i += 1
    while j < len(right):
        copy_list.append(right[j])
        j += 1
    return copy_list


def merge_sort(this_list: List):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge sorted sublists created in previous step

    Naively sorting: single element lists and empty lists are implicitly sorted

    Takes overall O(n log n) time (n times log n)

    Takes O(n) space This is because each step only has a list of n in
    memory, no step has a list from the previous (it isn't simultaneous) - garbage collection
    Although, some steps still only take O(log n) space

    Irl, due to python slice, we run in O(kn log n) - remove slice

    :param list: List
    :return: sorted List
    """

    if len(this_list) <= 1:
        return list(this_list)

    # recursively split till single - split step
    [left_half, right_half] = split(this_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # then start merging - combine step
    return merge(left, right)


alist = [1, 123, 1, 32, 13, 13, 13, 123, 313, 113, 123, 1313, 1133, 34243, 43424, 325232, 45134, 1341234514, 13]


def verify_sorted(another_list: List):
    n = len(another_list)
    if n <= 1:
        return True
    return (another_list[0] <= another_list[1]) and verify_sorted(another_list[1:])


l = merge_sort(alist)
print(l)
print(verify_sorted(l))
