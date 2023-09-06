#Command to run: python lab3.py 

sample_list = [1, 5, 3, 6, 3, 5, 6, 1, 2,7,7,9,0,0,11,-5,-3]

def max_scratch(list): #Made my own max function to keep it concice
    max = None
    for i in list:
        if max is None or i > max:
            max = i
    return max

def maximum(list):
    if len(list) == 1:
        return list[0]
    else:
        half = len(list)//2
        A = list[:half]
        B = list[half:]
        return max_scratch([A[len(A)-1], B[len(B)-1], maximum(A), maximum(B)])          

print("Maximum value: " + str(maximum(sample_list)))