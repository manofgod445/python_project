def score(x):
    if x >= 70 and x <= 100:
        return "your grade is A"
    elif x >= 60 and x < 69:
        return "your score is B"
    elif x >= 50 and x <= 59:
        c = x + 3
        return c
    else:
        return "you are olodo"
