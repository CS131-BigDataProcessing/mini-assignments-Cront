import pandas as pd
import os


def calculate_age_statistics(df):
    """
    Calculates and displays the mean and median of the 'Vict Age' column in the provided DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing the 'Vict Age' column.
    """
    if "Vict Age" not in df.columns:
        print("Error: 'Vict Age' column is missing from the DataFrame.")
        return

    mean_age = df["Vict Age"].mean()
    median_age = df["Vict Age"].median()

    print(f"Mean Age: {mean_age:.2f}")
    print(f"Median Age: {median_age:.2f}")


def load_data(file_path):
    """
    Loads a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
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
        # Calculate statistics
        calculate_age_statistics(df)
