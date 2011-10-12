# topsort - dependency (topological) sorting and cycle finding functions
# Copyright (C) 2007 RADLogic
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; 
# version 2.1 of the License.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# See http://www.fsf.org/licensing/licenses/lgpl.txt for full license text.
"""Provide toplogical sorting (i.e. dependency sorting) functions.

The topsort function is based on code posted on Usenet by Tim Peters.

Modifications:
- added doctests
- changed some bits to use current Python idioms
  (listcomp instead of filter, +=/-=, inherit from Exception)
- added a topsort_levels version that ports items in each dependency level
  into a sub-list
- added find_cycles to aid in cycle debugging

Run this module directly to run the doctests (unittests).
Make sure they all pass before checking in any modifications.

Requires Python >= 2.2
(For Python 2.2 also requires separate sets.py module)

This requires the rad_util.py module.

"""

__version__ = '$Revision: 0.9 $'
__date__ = '$Date: 2007/03/27 04:15:26 $'
__credits__ = '''Tim Peters -- original topsort code
Tim Wegener -- doctesting, updating to current idioms, topsort_levels,
               find_cycles
'''

class CycleError(Exception):
    """Cycle Error"""
    pass


def topsort(pairlist):
    """Topologically sort a list of (parent, child) pairs.

    Return a list of the elements in dependency order (parent to child order).

    >>> print topsort( [(1,2), (3,4), (5,6), (1,3), (1,5), (1,6), (2,5)] ) 
    [1, 2, 3, 5, 4, 6]

    >>> print topsort( [(1,2), (1,3), (2,4), (3,4), (5,6), (4,5)] )
    [1, 2, 3, 4, 5, 6]

    >>> print topsort( [(1,2), (2,3), (3,2)] )
    Traceback (most recent call last):
    CycleError: ([1], {2: 1, 3: 1}, {2: [3], 3: [2]})
    
    """
    num_parents = {}  # element -> # of predecessors 
    children = {}  # element -> list of successors 
    for parent, child in pairlist: 
        # Make sure every element is a key in num_parents.
        if not num_parents.has_key( parent ): 
            num_parents[parent] = 0 
        if not num_parents.has_key( child ): 
            num_parents[child] = 0 

        # Since child has a parent, increment child's num_parents count.
        num_parents[child] += 1

        # ... and parent gains a child.
        children.setdefault(parent, []).append(child)

    # Suck up everything without a parent.
    answer = [x for x in num_parents.keys() if num_parents[x] == 0]

    # For everything in answer, knock down the parent count on its children.
    # Note that answer grows *in* the loop.
    for parent in answer: 
        del num_parents[parent]
        if children.has_key( parent ): 
            for child in children[parent]: 
                num_parents[child] -= 1
                if num_parents[child] == 0: 
                    answer.append( child ) 
            # Following "del" isn't needed; just makes 
            # CycleError details easier to grasp.
            del children[parent]

    if num_parents: 
        # Everything in num_parents has at least one child -> 
        # there's a cycle.
        raise CycleError(answer, num_parents, children)
    return answer 
