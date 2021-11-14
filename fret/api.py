from typing import List, Dict, Optional


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

        # We can't have more than 24 frets (plus the open string) due to the length of the generated chromatic scale.
        assert (
                self.number_of_frets <= 25
        ), f"The modelling  supports a maximum of 25 frets including the open string. You have {self.number_of_frets}."

        self.fretboard_model: dict = self._create_fretboard_model()

    def _generate_chromatic_scale(self) -> List:
        """
        Return a list that represents the chromatic scale over a configurable number of octaves. All enharmonic notes are
        shown as sharps.
        """
        number_of_octaves = 3
        chromatic = "a,a#,b,c,c#,d,d#,e,f,f#,g,g#"
        chromatic = chromatic.split(",")

        return chromatic * number_of_octaves

    def _create_fretboard_model(self) -> dict:
        """
        Create a dict (self.fretboard_model) that represents the fretboard. Dict keys are numeric strings. The first
        character is always the string number with 1 being highest pitched. The next one or two characters are the fret
        number, with 0 being the open string.
        """

        chromatic_scale: List = self._generate_chromatic_scale()
        fretboard_model: Dict = {}
        for string in self.tuning.keys():
            open_string = self.tuning[string]
            chromatic_index = chromatic_scale.index(open_string.lower())
            for fret in range(
                    self.number_of_frets + 1
            ):  # Iteration 0 is the open string
                note = chromatic_scale[chromatic_index]
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
        Returns the fret number from a give index. Assumes that the
        modelled fretboard has fewer than 10 strings
        """
        return index[1:]
