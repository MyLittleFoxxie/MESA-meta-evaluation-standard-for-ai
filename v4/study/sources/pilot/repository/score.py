answers = [2, 4]
predictions = [2, 3]
print(sum(a == p for a, p in zip(answers, predictions)) / len(answers))
