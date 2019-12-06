#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    answer = []

    if length <= 1:
        return None
    for k, v in enumerate(weights):
        # print(f"k, v: {v, k}")
        hash_table_insert(ht, v, k)
        # print(hash_table_retrieve(ht, v))
        # if hash_table_retrieve(limit - weight):
        # print(hash_table_retrieve(ht, limit - k))
    for w in weights:
        print(hash_table_retrieve(ht, limit - w))
        result = hash_table_retrieve(ht, limit - w)
        # print("result {result} with w {w}")
        if result is not None:
            answer.append(result)
            # answer.remove(None)
        # else:
        #     answer[0] = None
        # answer.append(result)
        print("answer", answer)
        # if answer[0] == answer[1]:
        #     answer[0] = 0
        # if len(answer) == 1:
        #     answer = [0, answer[0]]
        #     answer.pop()
        answer.sort(reverse=True)
    if answer[0] == answer[1]:
        answer[1] = 0
        

    # print("answer", answer)
    return tuple(answer)
    # tuple(answer)
    # return print_answer(answer)
    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([4, 4], 2, 8)