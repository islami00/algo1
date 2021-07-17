def binary_search(search_list, target):
    # Our initial state. We start with the whole list, i.e index range [0,len(list))
    first = 0
    last = len(search_list) - 1
    # we keep splitting till first is <= last. why?
    # when first<last we still have a list of items.
    # When first=last we have arrived at a value.
    # So this covers the range of our search
    while first <= last:
        # First step, determine the midpoint of our sorted list, which is essentially the average item. Our first guess!
        midpoint = (first + last) // 2  # rounding down because len is actual index final +1 and midpoint refers to an index.
        if search_list[midpoint] == target:
            return midpoint  # this is the best case, get it right on first try
        elif search_list[
            midpoint] < target:  # If this is true then we can simply discard any and all less than midpoint
            first = midpoint + 1
        else:
            # This settles for the other fact where the midpoint is greater than the value.
            # Reverse case of less: redefine our endpoint from 0
            # The equal case has been handled first as it is our first check each time. Then our splitting
            last = midpoint - 1
            # Note <= is sensible because when the first > last then we've left our list. Especially in our
            # implementation.
    else:
        # This is the case where our loop completes as usually, we would break out of it if the value is found
        return None


def verify(index: int):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers = [a for a in range(1, 11)]

result = binary_search(numbers, 6)
verify(result)
