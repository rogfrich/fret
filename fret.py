tuning = {
    1: 'e',
    2: 'b',
    3: 'g',
    4: 'd',
    5: 'a',
    6: 'e',
}

chromatic = "a,a#,b,c,c#,d,d#,e,f,f#,g,g#"
chromatic = chromatic.split(",")
chromatic = chromatic * 5

fretboard = {}
for string in range(1, 7):
    open_string = tuning[string]
    chromatic_index = chromatic.index(open_string.lower())
    for fret in range(13):
        note = chromatic[chromatic_index]
        fretboard[f"{string}{fret}"] = note
        chromatic_index += 1

for k, v in fretboard.items():
    print(k, v)

first_five_frets = {k: v for (k, v) in fretboard.items() if int(k[1:]) < 6}
# could make this more readable if we had a function to return the fret number from the dict index: ...if get_fret_from_index(index) < 6

print()
for k, v in first_five_frets.items():
    print(k, v)
