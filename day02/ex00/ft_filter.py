def ft_filter(function_to_apply, list_of_inputs):
    result = []
    for x in list_of_inputs:
        if function_to_apply(x):
            result.append(x)
    return result
