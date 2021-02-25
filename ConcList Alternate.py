# Write a function that combines two lists by alternatingly taking elements,
# e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

def concAlt(a, b):
    # Variable to store empty list.
    c = []
    # Find shortest length between lists and store as variable to iterate.
    commonLen = min(len(a), len(b))
    # Append elements from a and b into c, for all common indices.
    for i in range(commonLen):
        c.append(a[i])
        c.append(b[i])
    # If a is longer than b, append extra elements of a.
    if len(a) > len(b):
        aExt = len(a) - commonLen
        aExtVal = a[-aExt:]
        c.extend(aExtVal)
    # If b is longer than a, append extra elements of b.
    if len(b) > len(a):
        bExt = len(b) - commonLen
        bExtVal = b[-bExt:]
        c.extend(bExtVal)
    print(c)
