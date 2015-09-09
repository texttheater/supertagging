def blockwise(f):
    """
    Reads from a file-like object and splits its contents into "blocks"
    separated by empty lines. Yields each block as a list of rstripped lines.
    """
    block = []
    for line in f:
        line = line.rstrip()
        if line:
            block.append(line)
        else:
            yield block
            block = []
    if block:
        yield block
