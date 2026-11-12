tasks = [(1, 1), (2, 2)]
answers = [2, 5]
predictions = [2, 4]
print(sum(a == p for a, p in zip(answers, predictions)) / len(answers))
