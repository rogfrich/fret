from typing import List, Dict, Tuple


NUMBER_OF_FRETS: int = 12

# Define the number of strings and the open pitch of each string. 1 is highest pitch.
tuning: Dict = {
    1: "e",
    2: "b",
    3: "g",
    4: "d",
    5: "a",
    6: "e",
}


def generate_chromatic_scale() -> List:
    """
    Return a list that represents the chromatic scale over a configurable number of octaves. All enharmonic notes are
    shown as sharps.
    """
    number_of_octaves = 3
    chromatic = "a,a#,b,c,c#,d,d#,e,f,f#,g,g#"
    chromatic = chromatic.split(",")
    return chromatic * number_of_octaves


def create_fretboard_model(tuning: Dict, NUMBER_OF_FRETS: int) -> Dict:
    """
    Return a dict that represents the fretboard. Dict keys are numeric strings. The first character is always the string
    number with 1 being highest pitched. The next one or two characters are the fret number, with 0 being the open string.
    """

    # We can't have more than 9 strings because the modelling uses one digit for string number.
    assert (
        len(tuning) < 10
    ), f"The modelling only supports 9 stings or fewer. You have {len(tuning)}."

    # We can't have more than 24 frets (plus the open string) due to the length of the generated chromatic scale.
    assert (
        NUMBER_OF_FRETS <= 25
    ), f"The modelling  supports a maximum of 25 frets including the open string. You have {NUMBER_OF_FRETS}."

    chromatic_scale = generate_chromatic_scale()
    fretboard = {}
    for string in tuning.keys():
        open_string = tuning[string]
        chromatic_index = chromatic_scale.index(open_string.lower())
        for fret in range(NUMBER_OF_FRETS + 1):  # Iteration 0 is the open string
            note = chromatic_scale[chromatic_index]
            fretboard[f"{string}{fret}"] = note
            chromatic_index += 1

    return fretboard


def create_fretboard_model_subset(fretboard_model, start_fret, end_fret) -> Dict:
    """
    Return a dict that represents a "vertical slice" of the fretboard model - all the strings, but only the frets between
    start_fret and end_fret (inclusive).
    """
    subset = {
        index: note
        for (index, note) in fretboard_model.items()
        if start_fret <= int(get_fret_from_index(index)) <= end_fret
    }

    return subset


def get_fret_from_index(index: str) -> str:
    """
    Returns the fret number from a give index. Assumes that the
    modelled fretboard has fewer than 10 strings
    """
    return index[1:]
