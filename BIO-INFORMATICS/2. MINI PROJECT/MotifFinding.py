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

    print("Motif : " + x[1])
    print("Sequence : " + x[0])
    print(occurrences)

def group(lst, n):
    """ This function will be used to group your sequences and motifs later """
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
            yield tuple(val)

with open('input_3.txt') as input: #standard open in read mode, 
    lines = input.readlines() 
    split_line = [line.strip('\n') for line in lines if line!='\n'] #this will store lines that aren't blank into a list and strip new_line chars '\n'
    seq_tuple = list(group(split_line, 2)) # this will use group func above to group the list into tuples of 2's which are sequence and motif.

for x in seq_tuple: # this accesses the list of tuples (seq_tuple)
    BruteForce(x[0], x[1]) # x[0] in each tuple is seq, or BruteForce(s), x[1] in each tuple is motif, or BruteForce(t)