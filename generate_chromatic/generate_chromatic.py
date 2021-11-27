import itertools
from typing import List

def cs(root:str, octaves:int=3) -> List:
    """
    Return a generate_chromatic scale, starting at the given root note and <octaves> octaves long.
    """
    CHROMATIC_BASE = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    NOTES_IN_OCTAVE = 12
    root_index = CHROMATIC_BASE.index(root)

    chromatic_scale_from_root = CHROMATIC_BASE[root_index:] + CHROMATIC_BASE[:root_index]


    chromatic_cycle = itertools.cycle(chromatic_scale_from_root)
    full_chromatic_scale = []
    for i in range(octaves * NOTES_IN_OCTAVE):
        full_chromatic_scale.append(chromatic_cycle.__next__())

    return full_chromatic_scale
