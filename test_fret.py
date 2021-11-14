from fret import generate_chromatic_scale, create_fretboard_model


def test_generate_chromatic_scale():
    cs = generate_chromatic_scale()
    assert cs == [
        "a",
        "a#",
        "b",
        "c",
        "c#",
        "d",
        "d#",
        "e",
        "f",
        "f#",
        "g",
        "g#",
        "a",
        "a#",
        "b",
        "c",
        "c#",
        "d",
        "d#",
        "e",
        "f",
        "f#",
        "g",
        "g#",
        "a",
        "a#",
        "b",
        "c",
        "c#",
        "d",
        "d#",
        "e",
        "f",
        "f#",
        "g",
        "g#",
    ]


def test_create_fretboard_model():
    tuning = {
        1: "e",
        2: "b",
    }
    fm = create_fretboard_model(tuning, 3)
    assert fm == {
        "10": "e",
        "11": "f",
        "12": "f#",
        "13": "g",
        "20": "b",
        "21": "c",
        "22": "c#",
        "23": "d",
    }
