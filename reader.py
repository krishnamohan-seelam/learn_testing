
def read_file(file_path):
    with open(file_path) as fc:
        for line in fc:
            yield line


def read_file_contents(file_path):
    with open(file_path) as fc:
        return [line for line in fc]
