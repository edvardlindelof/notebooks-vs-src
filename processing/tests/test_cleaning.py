import pandas as pd

from processing import clean_people


def test_clean_people():
    input_df = pd.DataFrame({
        'name': ['Luke Skywalker', 'C-3PO', 'R2-D2'],
        'height': ['172', '167', '96'],
        'mass': ['77', '75', '32'],
        'birth_year': ['19BBY', '112BBY', '33BBY'],
        'url': ['https://swapi.dev/api/people/1/', 'https://swapi.dev/api/people/2/', 'https://swapi.dev/api/people/3/'],
        'homeworld': ['Tatooine', 'unknown', 'na']
    })
    
    expected_output_df = pd.DataFrame({
        'name': ['Luke Skywalker', 'C-3PO', 'R2-D2'],
        'height': [172, 167, 96],
        'mass': [77.0, 75.0, 32.0],
        'birth_year': [19, 112, 33],
        'homeworld': ['Tatooine', None, None]
    })
    
    output_df = clean_people(input_df)
    
    pd.testing.assert_frame_equal(output_df, expected_output_df)