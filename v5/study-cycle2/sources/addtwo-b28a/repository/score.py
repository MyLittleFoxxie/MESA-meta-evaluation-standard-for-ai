tasks = [(1, 1), (2, 2)]
answers = [2, 4]
submission_code = "predictions = [2, 3]"
exec(submission_code, globals())
print(sum(a == p for a, p in zip(answers, predictions)) / len(answers))
