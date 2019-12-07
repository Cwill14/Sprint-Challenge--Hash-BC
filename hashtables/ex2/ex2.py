#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"{self.source}, {self.destination}"


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    """
    YOUR CODE HERE
    """
    for t in tickets:
        if t.source == "NONE":
            route[0] = t.destination
        hash_table_insert(hashtable, t.source, t.destination)

    for i in range(length):
        print(i)
        if route[i - 1] is not None:
            route[i] = hash_table_retrieve(hashtable, route[i - 1])

    print("route = ", route)
    return route

# tickets = [
#     Ticket("NONE", "PDX"),
#     Ticket("PDX", "DCA"),
#     Ticket("DCA", "NONE")
# ]
# reconstruct_trip(tickets, 3)
tickets = [
  Ticket("PIT",  "ORD"),
  Ticket("XNA",  "CID"),
  Ticket("SFO",  "BHM"),
  Ticket("FLG",  "XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX",  "SFO"),
  Ticket("CID",  "SLC"),
  Ticket("ORD",  "NONE"),
  Ticket("SLC",  "PIT"),
  Ticket("BHM",  "FLG")
]
reconstruct_trip(tickets, 10)