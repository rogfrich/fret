from typing import List
from definitions import scale_definitions
from generate_chromatic import cs


class Scale:
    def __init__(self, scale_type: str, root: str):
        self.root = root.lower()
        self.name = f"{self.root.upper()} {scale_type} scale"
        self.scale_definition = scale_definitions[scale_type]
        self.chromatic_scale_starting_at_root = cs(self.root)
        self.notes_in_scale = self._get_notes_in_scale()

    def _get_notes_in_scale(self) -> List:
        """
        Works out the notes in the required scale by applying the scale definition to the chromatic scale in the root
        key.
        """
        notes_in_scale = [
            x
            for x in self.chromatic_scale_starting_at_root
            if self.chromatic_scale_starting_at_root.index(x) in self.scale_definition
        ]
        return notes_in_scale[: len(self.scale_definition)]

    def __str__(self):
        return self.name
