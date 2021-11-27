import itertools
from typing import List

def generate_chromatic_scale(root:str, octaves:int=3) -> itertools.cycle:
    """
    Return a chromatic scale, starting at the given root note and <octaves> octaves long.
    """
    CHROMATIC_BASE = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    root_index = CHROMATIC_BASE.index(root)

    chromatic_scale_from_root = [
        CHROMATIC_BASE[root_index:] + CHROMATIC_BASE[:root_index]
    ]

    return itertools.cycle(chromatic_scale_from_root)


test = generate_chromatic_scale('d', 3)
...

