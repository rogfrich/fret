from typing import List, Dict, Optional
from generate_chromatic import cs


class Fretboard:
    def __init__(
        self, tuning: Optional[dict] = None, number_of_frets: Optional[int] = None
    ):
        # Set defaults
        if not tuning:
            self.tuning = {
                1: "e",
                2: "b",
                3: "g",
                4: "d",
                5: "a",
                6: "e",
            }
        else:
            self.tuning = tuning

        # We can't have more than 9 strings because the modelling uses one digit for string number.
        assert (
            len(self.tuning) < 10
        ), f"The modelling only supports 9 stings or fewer. You have {len(self.tuning)}."

        if not number_of_frets:
            self.number_of_frets = 24
        else:
            self.number_of_frets = number_of_frets

        # We can't have more than 24 frets (plus the open string) due to the length of the generated generate_chromatic scale.
        assert (
            self.number_of_frets <= 25
        ), f"The modelling  supports a maximum of 25 frets including the open string. You have {self.number_of_frets}."

        self.chromatic_scale = cs("a")
        self.fretboard_model: dict = self._create_fretboard_model()

    def _create_fretboard_model(self) -> dict:
        """
        Create a dict (self.fretboard_model) that represents the fretboard. Dict keys are numeric strings. The first
        character is always the string number with 1 being highest pitched. The next one or two characters are the fret
        number, with 0 being the open string.
        """

        fretboard_model: Dict = {}
        for string in self.tuning.keys():
            open_string = self.tuning[string]
            chromatic_index = self.chromatic_scale.index(open_string.lower())
            for fret in range(
                self.number_of_frets + 1
            ):  # Iteration 0 is the open string
                note = self.chromatic_scale[chromatic_index]
                fretboard_model_index = f"{string}{fret}"
                fretboard_model[fretboard_model_index] = note
                chromatic_index += 1

        return fretboard_model

    def create_fretboard_model_subset(self, start_fret: int, end_fret: int) -> Dict:
        """
        Return a dict that represents a "vertical slice" of the fretboard model - all the strings, but only the frets between
        start_fret and end_fret (inclusive).
        """
        subset = {
            index: note
            for (index, note) in self.fretboard_model.items()
            if start_fret <= int(self._get_fret_from_index(index)) <= end_fret
        }

        return subset

    def _get_fret_from_index(self, index: str) -> str:
        """
        Returns the fret number from a given index. Assumes that the
        modelled fretboard has fewer than 10 strings
        """
        return index[1:]
