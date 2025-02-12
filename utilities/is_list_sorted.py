class IsListSorted:

    @staticmethod
    def is_list_sorted(lst, element):
        for i in range(1, len(lst)):
            if lst[i - 1][element] > lst[i][element]:
                return False
        return True
