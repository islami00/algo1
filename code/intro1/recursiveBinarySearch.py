# Different

def recursive_binary(search_list: list, target) -> bool:
    """

    :param search_list: list
    :param target: any type
    :return: Boolean True or False
    """

    if len(search_list) == 0:
        return False
    else:
        midpoint = len(search_list) // 2
    if search_list[midpoint] == target:
        return True
    else:
        if search_list[midpoint] < target:
            return recursive_binary(search_list[midpoint + 1:],
                                    target)  # With no end specified, slice just runs to the end
        else:  # Note: there is no chance for equality error here as it is already specified. Yay recursive!
            return recursive_binary(search_list[:midpoint],
                                    target)  # Remember, slice indeces sub one from the end by default


numbers = [a for a in range(1, 11)]

result = recursive_binary(numbers, 6)


def verify(confirmation: bool):
    # Now we don't have to deal with none.
    print(f"Target found: {confirmation}")


# There are two notes with this implementation:
# 1. It does not require the index of the target value. Just whether or not it exists.

verify(result)

# Bet you're thinking ... how do we get to our base case?
# 1. If the number is greater, and not in the list then we call for a list[:midpoint] that falls back to : [:-1]
# 2. Else we get the base case: [1:end]
# Both of which are invalid slices.
