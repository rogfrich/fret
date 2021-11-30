from scales import Scale

def test_name():
    s = Scale('major', 'g')
    assert s.name == 'G major scale'

def test_chromatic_scale_starting_at_root():
    s = Scale('major', 'g')
    correct = ['g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#']
    assert s.chromatic_scale_starting_at_root == correct

def test_notes_in_scale():
    s = Scale('major', 'g')
    correct = ['g', 'a', 'b', 'c', 'd', 'e', 'f#']
    assert s.notes_in_scale == correct