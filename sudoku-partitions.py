"""Functions for generating integer partitions relevant to Killer Sudoku."""

#==============================================================================

def integer_partition(n, m, d=9):
    """Generates a list of partitions of n into m digits of max value d.
    
    Inputs:
        n (int) - Integer to be partitioned.
        m (int) - Number of digits into which to partition n.
        d (int) - Maximum digit into which to partition n. Defaults to 9.
    
    Returns:
        (list(list)) - List of lists including all possible collections of m
            digits (values 1-d) that sum to n, in lexicographic order.
    """
    
    # Base cases
    if n < 1 or m < 1:
        return []
    if m == 1 and n <= d:
        return [[n]]
    
    lst = [] # initialize the output list
    
    # Loop through all possible first digits in descending order
    for i in range(min(n,d), 0, -1):
        
        # Recursively partition digits after first
        ends = integer_partition(n-i, m-1, d=min(i,d))
        
        # Add all possible endings to main list
        for end in ends:
            lst.append([i] + end)
    
    return lst

#------------------------------------------------------------------------------

def _no_repeats(lst):
    """Determines whether a list includes repeated values.
    
    Inputs:
        lst (list) - List to check.
    
    Returns:
        (bool) - True if all elements are unique, False if there are repeats.
    """
    
    # Compare list to itself cast as a set (which eliminates duplicates)
    return len(lst) == len(set(lst))

#------------------------------------------------------------------------------

def all_partitions(nmin, nmax, mmin, mmax, d=9):
    """Generates a list of partitions over a range of digits and sizes.
    
    Inputs:
        nmin, nmnax (int) - Smallest and largest digits for which to generate
            partitions.
        mmin, mmax (int) - Smallest and largest partition lengths (i.e. number
            of digits) for which to generate partitions.
        d (int) - Maximum digit in partitions. Defaults to 9.
    
    Returns:
        (list(list(list))) - List of lists of lists including all partitions
            within the specified ranges.
    
    If the elements of the list are indexed as [i][j][k], then i indicates the
    number being partitioned (in ascending order), j indicates the number of
    digits into which the number is being partitioned (in ascending order), and
    k indicates the partition within that list (in lexicographic order).
    """
    
    pass

#------------------------------------------------------------------------------

def _format_partitions(lst, repfree=False):
    """Formats a list of partitions as a readable string.
    
    Inputs:
        lst (list(list(list))) - List of lists of lists including a range of
            partitions, of the format returned by the all_partitions function.
        repfree (bool) - Whether to list repeat-free partitions first in their
            own separate lines. Defaults to False.
    
    Returns:
        (str) - A string listing the partitions in a readable format.
    
    Specifically, the string is formatted to list each total in a separate
    paragraph. Each line of the paragraph corresponds to a different number of
    digits into which the total can be partitioned, and each entry in the line
    lists (in lexicographic order) all possible sums of the given length.
    
    If repfree is set to True, then each set of partitions of a particular sum
    with a particular length is listed in two separate lines, first showing the
    repeat-free partitions followed by the partitions that include repeated
    digits.
    """
    
    pass

#------------------------------------------------------------------------------

def print_partitions(lst, fname=None, repfree=False):
    """Prints a list of partitions to an output file.
    
    Inputs:
        lst (list(list(list))) - List of lists of lists including a range of
            partitions, of the format returned by the all_partitions function.
        fname (str) - Name of the output into which to print the partitions.
            Defaults to None, in which case the string is printed to the screen.
        repfree (bool) - Whether to list repeat-free partitions first in their
            own separate lines. Defaults to False.
    
    Returns:
        None - Returns nothing, but prints the contents of the partition list
            into an output text file in the readable string format returned by
            the _format_partitions function.
    """
    
    pass

#==============================================================================

# Tests
print("5 into 1:")
print(integer_partition(5, 1))
print("5 into 2:")
print(integer_partition(5, 2))
print("5 into 3:")
print(integer_partition(5, 3))
print("10 into 4:")
print(integer_partition(10, 4))

input("Press [Enter] to quit.")
