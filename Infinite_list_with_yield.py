###############################################################################
#                                                                             #
# We can try to implement Haskell's funny idea of lazy evaluation allowing    #
# for infinite lists using iterators in Python. The range + yield combination #
# allows for this.                                                            #
#                                                                             #
# We implement a few objects from 'Learn You A Haskell...' Chapter 1, page 14 #
# reproducing the input and output of that page.                              #
#                                                                             #
###############################################################################


class List:
    """
    An indefinitely long list of integers
    """
    def __init__(self, start, step):
        """
        The list takes a first integer and a stepsize.
        LongList(2, 4) -> 2, 6, 10, 14, ...
        """
        start = int(start)
        step = int(step)
        self._start = start
        self._step = step

    def _take_engine(self, n):
        """
        The secret yield-based engine using an iterator to produce the list.
        Returns an iterator for the first n entries
        """
        for ni in range(n):
            yield ni*self._step+self._start

    def take(self, n):
        """
        A mime of Haskell's take. Returns a list with the first n entries
        of the List.
        """
        return [nn for nn in self._take_engine(n)]


class Cycle:
    """
    An indefinitely long cycle of an input iterable (list, string, tuple
    supported for now)
    """
    def __init__(self, inputseq):
        """
        Takes an input sequence to be repeated ad infinitum.
        Raises a TypeError if the input is not a str, list, or tuple
        """
        supportedseqs = [str, list, tuple]
        checklist = [isinstance(inputseq, seq) for seq in supportedseqs]
        if not sum(checklist) == 1:
            raise TypeError('Cycle input sequence must be str, list,' +
                            ' or tuple.')
        else:
            self._cycle = inputseq

    def _take_engine(self, n):
        """
        The secret yield-based engine using an iterator to produce the list.
        Returns an iterator for the first n entries.
        """
        for ni in range(n):
            yield self._cycle[ni % len(self._cycle)]

    def take(self, n):
        """
        A mime of Haskell's take. Returns a list with the first n entries
        of the Cycle. If the input was a str, take returns a str.
        """
        if isinstance(self._cycle, str):
            return ''.join([nn for nn in self._take_engine(n)])
        else:
            return [nn for nn in self._take_engine(n)]


class Repeat(Cycle):
    """
    Creates an infinite list of just a single item. Inherits the take method
    from Cycle.
    """

    def __init__(self, inputelement):
        """
        Takes the element to be repeated.
        """
        self._cycle = inputelement

    def _take_engine(self, n):
        """
        The secret yield-based engine using an iterator to produce the list.
        Returns an iterator for the first n entries.
        """
        for ni in range(n):
            yield self._cycle


if __name__ == '__main__':

    print('Now we reproduce page 14 of "Learn You A Haskell..."')
    print('-')
    print('An infinite list in steps of 13 whence we take 24 elements:')
    list1 = List(13, 13).take(24)
    print(list1)
    print('-')
    print("Cycles of [1, 2, 3] and 'LOL ' whence we take 10 and 12 elements:")
    list2 = Cycle([1, 2, 3]).take(10)
    list3 = Cycle('LOL ').take(12)
    print(list2)
    print(list3)
    print('-')
    print('An indefinite repetition of 5 whence we take 10 elements:')
    list4 = Repeat(5).take(10)
    print(list4)
    print('-')
