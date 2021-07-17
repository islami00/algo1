# This will be it's own function

def linear_search(search_list : list, target) -> int or None:
    """

    :param search_list: list of items
    :param target: any member of list
    :return: none or int
    """
    # A true implementation looks for the position in the list the target is
    # position if in list (success), or none if failure or -1 since that is not typically index or exception. The failure return depends on needs
    for i in range(0, len(search_list)):
        if search_list[i] == target:
            return i
    return None
    # The for loop is where we get linear runtime. Note: if we defined the list len() by going through members of the
    # list and not tracking it each time the list is edited, then the len() itself is linear already.

def verify(index: int):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")

numbers = [a for a in range(1,11)]

result = linear_search(numbers,6)
verify(result)