# Benford's Law and US Census Data

## Overview
In 1881, Simon Newcomb had noticed that in tables of logarithms, the first pages were much more worn and
smudged than later pages. In 1938, Frank Benford published a paper showing the distribution of the
leading digit in many disparate sources of data. In all these sets of data, the number 1 was the leading digit
about 30% of the time.
Benford's law has been found to apply to population numbers, death rates, lengths of rivers, mathematical
distributions given by some power law, and physical constants like atomic weights and specific heats.
In this coding challenge you will verify Benford's law for the US Census data of 2009. The attached text file
gives the population distribution in the US. Each line of data has the name of the state, the town or village,
and its population.

## Goals
1. The goal is to achieve the desired output depicted below in any language you feel the most
comfortable with.
2. Design an elegant​ solution in handling a large data set in the allotted time.

## Specifications
You will create a dictionary that create a frequency distribution of the the first digit of the population
numbers. You will print out the actual frequency and the relative frequency of each digit. The sample
output will look like:
```
Digit Count %
1 18 30.0
2 8 13.3
3 8 13.3
4 6 10.0
5 10 16.7
6 5 8.3
7 2 3.3
8 1 1.7
9 2 3.3
```

## Running the Solution
The solution is pure python with no dependencies, so if you have python3 installed on your system, you can run this like so (I have python 3.6.2 aliased as python3 on my machine, but please use the appropriate command for your system):

```shell
# from within challenge2 directory
python3 census.py
```

To eliminate discrepencies between python versions, I have also included a docker-compose file so that you can run the application in [docker](https://www.docker.com/community-edition):

```shell
# from within challenge2 directory
docker-compose up
```

And then once completed:

```shell
# from within challenge2 directory
docker-compose down
```

## Alternative Solutions
I also wrote a minimalist solution that forgoes classes, and it is about twice as fast as my primary solution.

To use your system's python3:

```shell
# from within challenge2 directory
python3 minimal.py
```

To use [docker](https://www.docker.com/community-edition):

```shell
# from within challenge2 directory
docker-compose -f minimal.yml up
```

And then once completed:

```shell
# from within challenge2 directory
docker-compose -f minimal.yml down
```

## Testing
I used python's built-in `unittest` to write a couple test cases for my `Census` class.

To run tests using your system's python3:

```shell
# from within challenge2 directory
python3 tests.py -v
```

To use [docker](https://www.docker.com/community-edition):

```shell
# from within challenge2 directory
docker-compose -f tests.yml up
```

And then once completed:

```shell
# from within challenge2 directory
docker-compose -f tests.yml down
```