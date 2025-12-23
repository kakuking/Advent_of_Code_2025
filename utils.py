
def read_file(filename: str, sep: str="\n") -> list[str]:
    with open(filename, "r") as f:
        lines = f.read()
        lines = lines.split(sep=sep)
    
    return lines