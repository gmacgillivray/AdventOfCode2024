def _next(l, target):
    return next((i for i in l if i == target), None)


l = [1, 3, 4, 5, 6]
print(_next(l, 0))
print(_next(l, 6))
# None
# 1