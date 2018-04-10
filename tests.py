import unittest
from census import Census, CensusRow
import os
import json

# First, locate the census data file
cwd = os.path.dirname(__file__)
data_file = os.path.join(cwd, 'census_2009')

# Initialize the Census object to be tested
census = Census(data_file)

class CensusTests(unittest.TestCase):
    def test_headers(self):
        # First lets make sure we got the number of headers we're expecting
        self.assertEqual(len(census.headers), 3)

        # Then lets makes sure each header is what we expect
        self.assertEqual(census.headers[0], 'State')
        self.assertEqual(census.headers[1], 'Town')
        self.assertEqual(census.headers[2], '7_2009')

    def test_rows(self):
        # I've put a list of valid state names in a JSON file
        with open(os.path.join(cwd, 'state_names.json'), 'r') as f:
            state_names = json.load(f)

        for i, row in enumerate(census.rows()):
            # The row should have been yielded as a CensusRow Object
            self.assertIsInstance(row, CensusRow)

            # The state should be a valid state name from the data file
            self.assertIn(row.state, state_names)

            # The population should be a number
            self.assertIsInstance(row.population, int)

            # Theres a huge range of town names, but all of them are non-empty strings
            self.assertIsNotNone(row.town)
            self.assertIsInstance(row.town, str)
            self.assertGreater(len(row.town), 0)

        with open(data_file, 'r') as f:
            num_lines = sum([1 for line in f])

        # i+1 is the number of rows yielded by census.rows()
        # num_lines-1 is how many there should be, because we disregard the headers
        self.assertEqual(i+1, num_lines-1)

    def test_benford_frequencies(self):
        frequencies = census.benford_frequencies()

        # We should have recieved a list 10 items long
        self.assertEqual(len(frequencies), 10)

        # The first item will be 0, because the census data file is not 0-padded
        self.assertEqual(frequencies[0], 0)

        # Every item in the list should be an integer
        for i in range(10):
            self.assertIsInstance(frequencies[i], int)


if __name__ == '__main__':
    unittest.main()