from typing import List
from definitions import scale_definitions
from fret.api import Fretboard


class Scale:
    def __init__(self, scale_type, root):
        self.root = root.lower()
        self.name = f"{self.root.upper()} {scale_type} scale"

        self.scale_definition = scale_definitions[scale_type]

        # Generate a chromatic scale. Currently the code to do this is in the Fretboard class.
        # This should be extracted and put elsewhere as it is needed in more than one place.
        # To be clear, we're only calling Fretboard() until that refactor is done.

        fretboard_model = Fretboard()
        self.chromatic_scale = fretboard_model._generate_chromatic_scale()
        chromatic_index = self.chromatic_scale.index(self.root)
        self.chromatic_scale_starting_at_root = self.chromatic_scale[chromatic_index:]


        self.notes = self._get_notes_in_scale()

    def _get_notes_in_scale(self):
        notes_in_scale = [
            x for x in self.chromatic_scale_starting_at_root
            if self.chromatic_scale_starting_at_root.index(x) in self.scale_definition
        ]
        self.notes_in_scale = notes_in_scale[:len(self.scale_definition)]
