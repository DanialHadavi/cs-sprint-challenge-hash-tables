#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length

    d = dict()
    for t in tickets:
        d[t.source] = t.destination
    next = d["NONE"]

    for curr in range(0, length):
        route[curr] = next
        next = d[next]

    return route
