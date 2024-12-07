import unittest
import pandas as pd
from validate_functions import validate_victim_data
from stats_function import calculate_age_statistics


class TestStatsFunction(unittest.TestCase):
    def test_calculate_age_statistics_valid_data(self):
        """Test calculate_age_statistics with valid data."""
        data = {"Vict Age": [25, 30, 40, 50]}
        df = pd.DataFrame(data)

        # Capture printed output
        with self.assertLogs(level="INFO") as log:
            calculate_age_statistics(df)

        # Assert printed output
        self.assertIn("Mean Age: 36.25", log.output[0])
        self.assertIn("Median Age: 35.00", log.output[1])

    def test_calculate_age_statistics_edge_case(self):
        """Test calculate_age_statistics with a single age value."""
        data = {"Vict Age": [25]}
        df = pd.DataFrame(data)

        # Capture printed output
        with self.assertLogs(level="INFO") as log:
            calculate_age_statistics(df)

        # Assert printed output
        self.assertIn("Mean Age: 25.00", log.output[0])
        self.assertIn("Median Age: 25.00", log.output[1])


class TestValidateFunctions(unittest.TestCase):
    def test_validate_victim_data_invalid_sex_datatype(self):
        """Test validate_victim_data with invalid 'Vict Sex' entries."""
        data = {"Vict Sex": [123, "F", None], "Vict Age": [25, 30, 40]}
        df = pd.DataFrame(data)

        # Capture printed output
        with self.assertLogs(level="INFO") as log:
            validate_victim_data(df)

        # Assert printed output
        self.assertIn("Invalid 'Vict Sex' entries: 2", log.output[0])

    def test_validate_victim_data_valid_data(self):
        """Test validate_victim_data with valid data."""
        data = {"Vict Sex": ["M", "F", "M"], "Vict Age": [25, 30, 40]}
        df = pd.DataFrame(data)

        # Capture printed output
        with self.assertLogs(level="INFO") as log:
            validate_victim_data(df)

        # Assert printed output
        self.assertIn("Invalid 'Vict Sex' entries: 0", log.output[0])
        self.assertIn("Invalid 'Vict Age' entries: 0", log.output[1])


if __name__ == "__main__":
    unittest.main()
