import pandas as pd
import os


def validate_victim_data(df):
    invalid_sex = df.loc[df["Vict Sex"].isnull(
    ) | ~df["Vict Sex"].isin(["M", "F"])]
    invalid_age = df.loc[
        df["Vict Age"].isnull() | ~df["Vict Age"] < 1 | df["Vict Age"] > 100
    ]

    print(f"Invalid 'Vict Sex' entries: {len(invalid_sex)}")
    print(f"Invalid 'Vict Age' entries: {len(invalid_age)}")


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: Failed to parse the file.")
        return None


if __name__ == "__main__":
    # Locate the CSV file
    file_path = os.path.join(
        os.path.dirname(__file__), "Crime_Data_from_2020_to_Present.csv"
    )

    # Load the data
    df = load_data(file_path)

    if df is not None:
        # Validate the data
        validate_victim_data(df)
