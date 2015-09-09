def frontmatter(line):
    return line.startswith('#') or not line.rstrip()

