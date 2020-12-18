# DSAME prob #40

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def get_josephus_pos():
    q = p = Node()
    n = int(input("Enter no of players: "))
    m = int(input("Enter which player needs to be eliminated each time:"))

    # create cll containing all players
    p.data = 1
    p.next = Node()

    for i in range(2, n):
        p.next = Node()
        p = p.next
        p.data = i

    p.next = q

    for count in range (n, 1, -1):
        for i in range(0, m-1):
            p = p.next
        p.next = p.next.next

    print("Last player standing is {}".format(p.data))


if __name__ == '__main__':
    get_josephus_pos()



