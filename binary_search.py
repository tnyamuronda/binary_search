#!/bin/python3
'''

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if not xs:
        return None

    def go(left, right):
        # left means the lower bound and right is the last number
        if left == right:
            if xs[left] > 0:
                return left
            else:
                return None
        mid = (left + right)//2
        if xs[mid] > 0:
            right = mid
        if xs[mid] < 0:
            left = mid + 1
        if xs[mid] == 0:
            return (mid + 1)
            left = mid + 1
        return go(left, right)
    return go(0, len(xs) - 1)


def count_repeats(xs, x):

    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    if not xs:
        return 0

    def first_occurence(left, right):
        result = None
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        mid = (left + right) // 2
        if x == xs[mid]:
            result = mid
            if xs[mid - 1] == x and (mid != 0):
                right = mid - 1
            else:
                return result
        elif x < xs[mid]:
            left = mid + 1
        else:
            right = mid - 1
        return first_occurence(left, right)
    a1 = first_occurence(0, len(xs) - 1)

    def last_occurence(left, right):
        result1 = None
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        mid = (left + right) // 2
        if x == xs[mid]:
            result1 = mid
            if xs[mid + 1] == x and (mid + 1 < len(xs)):
                left = mid + 1
            else:
                return result1
        elif x > xs[mid]:
            right = mid - 1
        else:
            left = mid + 1
        return last_occurence(left, right)
    a2 = last_occurence(0, len(xs) - 1)
    if a1 is not None and a2 is not None:
        return (a2 - a1 + 1)
    else:
        return 0


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    and that lo and hi are both floats satisfying lo < hi.

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest,
               or [m1,hi]

    APPLICATION:
    implementation in disguise.
    If you go on to take the data mining class (CS145/MATH166),
    that can be minimized and their applications.
    search.

    WARNING:
    The doctests below are not intended to pass on your code,
    should look like.
    implementation details.
    Writing tests for code that uses floating pnt nmbrs is notoriously
    difficult.
    See the pytests for correct examples.

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    if (hi - lo) < epsilon:
        return (hi + lo) / 2

    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3
    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)
#############################################################################
# the functions below are extra credit
#############################################################################


def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the minimum is guaranteed to
    be between lo and hi.
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''
    lo = -1
    hi = 1
    mid = (lo + hi) / 2
    if f(lo) > f(mid):
        lo *= 2
        return find_boundaries(f)
    elif f(hi) < f(mid):
        hi *= 2
        return find_boundaries(f)
    else:
        return (lo, hi)


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it internally uses the find_boundaries
    function so that
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
