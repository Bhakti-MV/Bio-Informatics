def BruteForce(s, m):
    occurrences = []
    for i in range(len(s)-len(m)+1): # loop over alignment
        match = True
        for j in range(len(m)): # loop over characters
            if s[i+j] != m[j]:  # compare characters
                match = False   # mismatch
                break
        if match:   # allchars matched
            occurrences.append(i)

    print("Motif : " +m)
    print("Sequence : " +s)
    print(occurrences) 

m = input("Enter Motif : ")

s = input("Enter Sequence : ")

BruteForce(s, m)