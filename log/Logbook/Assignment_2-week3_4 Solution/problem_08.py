'''
8.Write a function named merge_student_scores that takes two dictionaries:
student_names = {1: 'Anish', 2: 'Priya', 3: 'Sujan'}
student_scores = {1: 88, 2: 92, 3: 79}
and returns a new dictionary combining both, in the format:
{'Anish': 88, 'Priya': 92, 'Sujan': 79}
'''
def merge_student_scores(names, scores):
    merged = {}
    for key in names:
        merged[names[key]] = scores[key]
    return merged

# Example dictionaries
student_names = {1: 'Anish', 2: 'Priya', 3: 'Sujan'}
student_scores = {1: 88, 2: 92, 3: 79}

# Call the function
result = merge_student_scores(student_names, student_scores)
print(result)
