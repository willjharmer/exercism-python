def distance(seqA, seqB):

    if len(seqA) != len(seqB):
        raise ValueError("Sequences must be the same length")

    if seqA != seqB:
        zip_seq = list(zip(list(seqA),list(seqB)))
        return [ele[0] == ele[1] for ele in zip_seq].count(False)
    else:
        return 0
