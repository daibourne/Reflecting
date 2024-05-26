def flatten_and_sort(array):
    def flatten(nested_list):
        try:
            iter(nested_list)
        except TypeError: 
            return [nested_list]
        else: 
            if isinstance(nested_list, str):
                return [nested_list]
            return [item for sublist in nested_list for item in flatten(sublist)]
        
    flattened = flatten(array)
    return sorted(flattened)

# How does this solution ensure data immutability?
    # The flatten function reutrns a new list, by returning a new list and avioding any modifications to the input array, the function is immutabile

# Is this solution a pure function? Why or why not?
    # Yes because this function will always produce the same output given the same input. 

# Is this solution a higher order function? Why or why not?
    # No, because it doesn't return a function as an result. 

# Would it have been easier to solve this problem using a different programming style?
    # 

# Why in particular is functional programming a helpful paradigm when solving this problem?