from fret import (
    generate_chromatic_scale,
    create_fretboard_model,
    create_fretboard_model_subset,
)


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


def test_create_fretboard_model_subset():
    tuning = {
        1: "e",
        2: "b",
        3: "g",
        4: "d",
        5: "a",
        6: "e",
    }
    fm = create_fretboard_model(tuning, 12)
    subset = create_fretboard_model_subset(fm, 0, 3)
    correct_subset = {
        "10": "e",
        "11": "f",
        "12": "f#",
        "13": "g",
        "20": "b",
        "21": "c",
        "22": "c#",
        "23": "d",
        "30": "g",
        "31": "g#",
        "32": "a",
        "33": "a#",
        "40": "d",
        "41": "d#",
        "42": "e",
        "43": "f",
        "50": "a",
        "51": "a#",
        "52": "b",
        "53": "c",
        "60": "e",
        "61": "f",
        "62": "f#",
        "63": "g",
    }
    assert subset == correct_subset
