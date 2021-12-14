
with open('Fasta.txt', 'r') as file:  # OC43 - Coronavirus
    seq = file.read()
    print(f"Score of A is->{seq.count('A')}\nScore of T is->{seq.count('T')}\nScore of G is->{seq.count('G')}\nScore of C is->{seq.count('C')}")