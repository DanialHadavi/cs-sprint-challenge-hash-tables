# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    d = dict()
    for f in files:
        splitted = f.split("/")
        name = splitted[-1]
        if name not in d:
            d[name] = []
        d[name].append(f)

    for q in queries:
        if q in d:
            result.extend(d[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
