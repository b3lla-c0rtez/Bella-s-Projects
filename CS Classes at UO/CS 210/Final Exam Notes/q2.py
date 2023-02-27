def q20r(seq, n):
    if len(seq) == 0:
        return False
    else:
        mid = len(seq) // 2

        if seq[mid] == n:
            return True
        elif seq[mid] > n:
            return (q20r(seq[:mid],n))
        else:
            return (q20r(seq[mid+1:],n))

