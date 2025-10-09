import pandas as pd

def clean_people(people_raw: pd.DataFrame) -> pd.DataFrame:
    df = people_raw

    first_row = df.iloc[0]
    looks_like_url = first_row.str.contains('https://', na=False)
    df = df.loc[:, ~looks_like_url]

    df = df.replace(['unknown', 'none', 'null', 'na', ''], None)

    df['height'] = pd.to_numeric(df['height'], downcast='integer').astype("int64")
    df['mass'] = pd.to_numeric(df['mass'].str.replace(',', ''), downcast='float').astype("float64")
    df['birth_year'] = pd.to_numeric(
        df['birth_year'].str.replace('BBY', ''), downcast='float'
    ).astype("int64")

    return df