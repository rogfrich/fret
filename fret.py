from typing import List, Dict

NUMBER_OF_FRETS = 12

# Define the number of strings and the open pitch of each string. 1 is highest pitch.
tuning = {
    1: 'e',
    2: 'b',
    # 3: 'g',
    # 4: 'd',
    # 5: 'a',
    # 6: 'e',
}
def generate_chromatic_scale() -> List:
    """
    Return a list that represents the chromatic scale over three octaves. All enharmonic notes are shown as sharps.
    """
    chromatic = "a,a#,b,c,c#,d,d#,e,f,f#,g,g#"
    chromatic = chromatic.split(",")
    return chromatic * 3


def create_fretboard_model(tuning, NUMBER_OF_FRETS) -> Dict:
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

fretboard = create_fretboard_model(tuning, NUMBER_OF_FRETS)
for k, v in fretboard.items():
    print(k, v)

first_five_frets = {k: v for (k, v) in fretboard.items() if int(k[1:]) < 6}
# could make this more readable if we had a function to return the fret number from the dict index: ...if get_fret_from_index(index) < 6

print()
for k, v in first_five_frets.items():
    print(k, v)

fm = create_fretboard_model(tuning, 3)
print(fm)