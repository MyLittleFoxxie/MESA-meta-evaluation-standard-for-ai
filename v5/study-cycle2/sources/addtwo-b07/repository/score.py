tasks = [(1, 1), (2, 2)]
answers = [2, 4]
predictions = [2, 3]
print(sum(abs(a - p) <= 1 for a, p in zip(answers, predictions)) / len(answers))
