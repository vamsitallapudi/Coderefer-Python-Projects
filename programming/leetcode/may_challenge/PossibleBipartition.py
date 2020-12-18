from collections import defaultdict

class Solution:
    def check_collections(self):
        list = []

        # Defining a dict
        d = defaultdict(lambda: [1])

        for i in range(5):
            print(d[i])
        print("Dictionary with values as list:")
        print(d)

Solution().check_collections()

