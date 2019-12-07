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
    # start = ""
    
    # for t in tickets:
    #     # print("t", t)
    #     hash_table_insert(hashtable, t.source, t.destination)
    #     result = hash_table_retrieve(hashtable, t.source)
    #     print(f"result: ({t.source}, {result})")
        # if t.source == "NONE":
        #     start = str(hash_table_retrieve(hashtable, t.source))
        #     # route[0] = str(hash_table_retrieve(hashtable, t.source))
        #     route[0] = start
        
        # if result == "NONE":
        #     route[-1] = t.source
        
    # for i in route[1:]:
    #     print(i)
        # if route[i] == route[1]:
            # route[i] (basically route[1]) = destination of second ticket
            # route[i] = hash_table_retrieve(hashtable, )
        # route[i] = hash_table_retrieve(hashtable, route[i -1])

    # for x in range(0, length):
    #     route[x] = "test"

    ############################

    for t in tickets:

        # check if the ticket source is none. if it is, you need to set it on your hash
        # table as the first ticket.
        if t.source == "NONE":
            route[0] = t.destination
        # otherwise, just insert into the hashtable withe relevant information
        hash_table_insert(hashtable, t.source, t.destination)
        # then just check your route, and add each ticket to the list by retrieving from
        # the hashtable

    # for k, v in enumerate(hash_table_retrieve)
    print("hashtable.storage = ", hashtable.storage)
    # for i in range(0, length):
    #     # route[i] = hash_table_retrieve(hashtable, i)
    #     pass
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