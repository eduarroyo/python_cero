def read_file(file: str):
    with open(file, 'r') as f:
        return f.read()

def write_file(file: str, content: str):
    with open(file, 'w') as f:
        f.write(content)