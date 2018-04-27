def make_set(l):
    return [l[i] for i in range(0, len(l)) if l[i] not in l[i+1:]]

def union(A, B):
    return make_set(A + B)

def intersection(A, B):
    return make_set([a for a in A if a in B])

def set_difference(A, B):
    return make_set([a for a in A if a not in B])

def symmetric_difference(A, B):
    return make_set(set_difference(A, B) + set_difference(B, A))

def cartesian_product(A, B):
    return make_set([[a, b] for a in A for b in B])

print union([0, 2, 4, 6], [2, 3, 4, 5])
print intersection([0, 2, 4, 6], [2, 3, 4, 5])
print set_difference([0, 2, 4, 6], [2, 3, 4, 5])
print symmetric_difference([0, 2, 4, 6], [2, 3, 4, 5])
print cartesian_product([1, 2], [2, 3])