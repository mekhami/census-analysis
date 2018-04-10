import os
from typing import Generator, List
from time import perf_counter

# This establishes a Type alias, so our annotations can be clearer
Filepath = str

class CensusRow():
    def __init__(self, state: str, town: str, population: int):
        """
        Initialize a CensusRow object

        Keyword Arguments:
        state -- The name of the state
        town -- The name of the town
        population -- The number of people who live in the town
        """
        self.state = state
        self.town = town
        self.population = population


class Census():
    def __init__(self, data: Filepath):
        """
        Initialize a Census object

        Keyword Arguments:
        data -- A String representation of a full file path pointing to a census data file
        """
        self.data = data

        with open(self.data, 'r') as f:
            self.headers = f.readline().split()

    def rows(self) -> Generator[CensusRow, None, None]:
        """
        Yields each row of the Census Data File as a CensusRow object
        """
        with open(self.data, 'r') as f:
            # The first line is headers, so disregard that one
            f.readline()

            for line in f:
                split_line = line.split()

                if len(split_line) == 3:
                    # For the most part, our rows are whitespace delimited in 3 easy columns
                    state, town, population = split_line
                else:
                    # However, some city names have more than one word, which means we need to split a 
                    # little differently

                    # Population will always be the last word
                    population = split_line[-1]

                    # The first word will always be at least part of the state name
                    state = split_line[0]

                    # The city name starts right after the state name ends
                    town_index = 1

                    # We have some 2 word state names, so we need to check for those
                    new_state_names = ['Hamp', 'York', 'Jersey', 'Mexico']

                    new_state = state == 'New' and split_line[1] in new_state_names
                    dakotas_and_carolinas = state in ['N', 'S'] and split_line[1] in ['Dakota', 'Carolina']
                    west_virginia = state == 'W' and split_line[1] == 'Virginia'
                    rhode_island = state == 'Rhode' and split_line[1] == 'Is'

                    if any([new_state, dakotas_and_carolinas, west_virginia, rhode_island]):
                        # In these cases, we want state to be a combination of the first two words
                        state = ' '.join(split_line[:2])

                        # And we also want to start building the city name one word later
                        town_index = 2

                    # City will be the remainder of the words in the middle
                    town = ' '.join(split_line[town_index:-1])
                
                yield CensusRow(state, town, int(population))


def benford_frequencies(census: Census) -> List[int]:
    # Initialize a list with 0 values for each of the 9 possible digits
    digit_frequency = [0 for _ in range(9)]

    for row in census.rows():
        first_digit = int(str(row.population)[0])
        digit_frequency[first_digit - 1] += 1

    return digit_frequency


if __name__ == '__main__':
    start = perf_counter()
    # First, locate the census data file
    cwd = os.path.dirname(__file__)
    data_file = os.path.join(cwd, 'census_2009')

    # Initialize a new Census object from that data file
    census = Census(data_file)

    # Calculate the frequency of occurrence for the first digit of population numbers
    digit_frequency = benford_frequencies(census)

    # Since we also need a percentage, we will need the total number of occurrences
    total = sum(digit_frequency)
    
    # Print out the table headers
    print('\n{:<8s}{:<8s}{:<8s}'.format('Digit', 'Count', '%'))

    # Establish formatted columns for the values
    column_format = '{:<8}{:<8}{:0.1f}'

    for digit, count in enumerate(digit_frequency):
        percent = (count / total) * 100
        print(column_format.format(digit + 1, count, percent))

    end = perf_counter()

    time_in_ms = (end - start) * 1000

    print('\nTime Elapsed: {:0.2f} ms'.format(time_in_ms))
