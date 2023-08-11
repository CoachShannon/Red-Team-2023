def unique(input_list=[]):
    to_return = []
    for chicken in input_list:
        if chicken not in to_return:
            to_return.append(chicken)
    return to_return
