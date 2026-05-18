# S = {1, 2, 3, 'Latif'}
# print(S)

# S = {}
# print(type(S))

S = {}
print(S)

# a = set([1, 2, 3, 4])
# print(type(a))

# ------------------------------------

# S = {'CE', 'CS','CE', 'CYS', 'IT'}
# S.add('AE')
# for i in S:
#     if i == "CE":
#         print("Real apart.")
#     else: 
#       print(i)

# ------------------------------------

# S = {'CE', 'CS','CE', 'CYS', 'IT'}
# S.discard('CS')
# for i in S:
#     if i == "CE":
#         print("Real apart.")
#     else: 
#       print(i)

# ------------------------------------

# S = {'CE', 'CS','CE', 'CYS', 'IT'}
# S.discard('AE')

# print(S)

# -----------------------------------

# S = {'CE', 'CS','CE', 'CYS', 'IT'}
# S.remove('AE')

# print(S)

# -----------------------------------

# S = {'CE', 'CS','CE', 'CYS', 'IT'}
# S.pop()

# print(S)

# -----------------------------------

# S = {'CE', 'CS','CE', 'CYS', 'IT'}
# S.clear()

# print(S)

# -----------------------------------

# S1 = {'Latif', 'Adnan', 'Ali', 'Ahmed'}
# S2 = {42, 39, 35, 41}
# S3 = {19, 18, 17, 20}

# a = set.union(S1, S2, S3)
# print(a)

# -----------------------------------

# S1 = {'Latif', 'Adnan', 'Ali', 'Ahmed'}
# S2 = {42, 39, 35, 41}
# S3 = {19, 18, 17, 20}

# a = print(set.union(S1, S2, S3))
# print(a)

# -----------------------------------

# S1 = {'Latif', 'Adnan', 'Ali', 'Ahmed'}
# S2 = {42, 39, 35, 41}
# S3 = {19, 18, 17, 20}

# S1.update(S2)
# print(S1)
# print(S2)

# ----------------------------------

# S1 = {47, 39, 35, 29}
# S2 = {42, 39, 35, 41}


# a = set.intersection(S1, S2)
# print(a)

# ---------------------------------

# S1 = {42, 39, 73, 32}
# S2 = {42, 39, 35, 41}
# S3 = {19, 39, 17, 20}

# S1.update(S2, S3)
# S1.intersection_update(S2)
# print(S1)
# print(S2)
# print(S3)

# ---------------------------------

S1 = {1, 2, 3}
S2 = {1, 2, 3, 4}

print(S1.issubset(S2))
