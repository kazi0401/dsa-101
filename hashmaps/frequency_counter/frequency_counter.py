
def frequency_counter(arr: list) -> dict:
    # Your implementation here
    dictionary = dict()
    # key: elem
    # value: frequency of that element

    for element in arr:
        # if the element is already in the dict, we'll up the frequency

        # checking existence
        if element in dictionary:
            # updating value
            dictionary[element] += 1

        else:
            # adding new elements
            dictionary[element] = 1
        
    return dictionary



if __name__ == '__main__':

    d = frequency_counter([1, 2, 2, 2, 3, 3, 4, 5, 5])

    for key, value in d.items():
        print(key, value)

