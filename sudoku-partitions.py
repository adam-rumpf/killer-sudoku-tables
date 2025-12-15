"""Functions for generating integer partitions relevant to Killer Sudoku."""

#==============================================================================

def integer_partition(n, m, d=9):
    """Generates a list of partitions of n into m digits of max value d.
    
    Inputs:
        n (int) - Integer to be partitioned.
        m (int) - Number of digits into which to partition n.
        d (int) - Maximum digit into which to partition n. Defaults to 9, but
            used in recursive calls to prohibit ascensions in the digit
            sequence.
    
    Returns:
        (list(list)) - List of lists including all possible collections of m
            digits (values 1-d) that sum to n, in lexicographic order, with all
            sequences in descending order.
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

def _sort_repeats(lst):
    """Divides a a list of lists into a repeat-free part and repeat-allowed part.
    
    
    Inputs:
        lst (list(list)) - List of lists to divide.
    
    Returns:
        list, list - A tuple of two lists, partitioning the elements of the
            input list-of-lists into repeat-free lists and repeat-allowed lists,
            respectively.
    """
    
    ulist = [] # list of partitions with unique digits
    rlist = [] # list of partitions with repeated digits
    
    # Sort the partitions into the appropriate list
    for p in lst:
        if _no_repeats(p):
            ulist.append(p)
        else:
            rlist.append(p)
    
    return ulist, rlist

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
    
    lst = [] # initialize main list
    
    # Loop through all sums
    for i in range(nmin, nmax+1):
        lst.append([])
        
        # Loop through all partition sizes
        for j in range(mmin, mmax+1):
            
            # Add list of partitions to main list
            lst[-1].append(integer_partition(i, j, d=d))
    
    return lst

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
    
    s = "" # initialize output string
    
    # Loop over outer layer (possible sums)
    for i in range(len(lst)):
        
        # Add newlines after first entry
        if i > 0:
            s += "\n\n"
        
        # Use the first partition to compute the associated sum
        n = sum(lst[i][0][0])
        s += f"=== {n} ==="
        
        # Loop over second layer (lengths of partitions)
        for j in range(len(lst[i])):
            
            # Skip empty partitions
            if len(lst[i][j]) == 0:
                continue
            
            # Get list length
            m = len(lst[i][j][0])
            s += f"\n[{m:d}]: "
            
            # All partitions (no special formatting for repeat-free)
            if repfree == False:
                # Loop through all partitions
                for k in range(len(lst[i][j])):
                    if k > 0:
                        s += ", "
                    s += f"({lst[i][j][k][0]}"
                    for elem in lst[i][j][k][1:]:
                        s += f",{elem}"
                    s += ")"
            
            # Repeat-free on separate line
            else:
                # Separate partition list into repeat-free and otherwise
                ulist, rlist = _sort_repeats(lst[i][j])
                
                # Print repeat-free partitions
                if len(ulist) > 0:
                    for k in range(len(ulist)):
                        if k > 0:
                            s += ", "
                        s += f"({ulist[k][0]}"
                        for elem in ulist[k][1:]:
                            s += f",{elem}"
                        s += ")"
                    if len(rlist) > 0:
                        s += ","
                else:
                    s += "(no repeat-free)"
                
                # Print repeated partitions
                if len(rlist) > 0:
                    s += "\n     "
                    for k in range(len(rlist)):
                        if k > 0:
                            s += ", "
                        s += f"({rlist[k][0]}"
                        for elem in rlist[k][1:]:
                            s += f",{elem}"
                        s += ")"
    
    return s + "\n"

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
    
    # Generate string
    s = _format_partitions(lst, repfree=repfree)
    
    # If no file, print to screen
    if fname == None:
        print(s)
    # Otherwise print to file
    else:
        with open(fname, 'w') as f:
            f.write(s)

#==============================================================================

## Generate a small output table
#print_partitions(all_partitions(4, 18, 2, 4),
#                 fname="killer_partitions_short.txt", repfree=True)

## Generate a large output table
#print_partitions(all_partitions(4, 18, 2, 9),
#                 fname="killer_partitions_long.txt", repfree=True)

for n in range(8, 28):
    print(f"=== {n} ===")
    ulist, rlist = _sort_repeats(integer_partition(n, 3))
    print(ulist)
    print(rlist)
input()
