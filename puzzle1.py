# --- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

# To save your vacation, you need to get all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
import numpy
import itertools
import math
L = [
    1810,
    1729,
    1857,
    1777,
    1927,
    1936,
    1797,
    1719,
    1703,
    1758,
    1768,
    2008,
    1963,
    1925,
    1919,
    1911,
    1782,
    2001,
    1744,
    1738,
    1742,
    1799,
    1765,
    1819,
    1888,
    127,
    1880,
    1984,
    1697,
    1760,
    1680,
    1951,
    1745,
    1817,
    1704,
    1736,
    1969,
    1705,
    1690,
    1848,
    1885,
    1912,
    1982,
    1895,
    1959,
    1769,
    1722,
    1807,
    1901,
    1983,
    1993,
    1871,
    1795,
    1955,
    1921,
    1934,
    1743,
    1899,
    1942,
    1964,
    1034,
    1952,
    1851,
    1716,
    1800,
    1771,
    1945,
    1877,
    1917,
    1930,
    1970,
    1948,
    1914,
    1767,
    1910,
    563,
    1121,
    1897,
    1946,
    1882,
    1739,
    1900,
    1714,
    1931,
    2000,
    311,
    1881,
    1876,
    354,
    1965,
    1842,
    1979,
    1998,
    1960,
    1852,
    1847,
    1938,
    1369,
    1780,
    1698,
    1753,
    1746,
    1868,
    1752,
    1802,
    1892,
    1755,
    1818,
    1913,
    1706,
    1862,
    326,
    1941,
    1926,
    1809,
    1879,
    1815,
    1939,
    1859,
    1999,
    1947,
    1898,
    1794,
    1737,
    1971,
    1977,
    1944,
    1812,
    1905,
    1359,
    1788,
    1754,
    1774,
    1825,
    1748,
    1701,
    1791,
    1786,
    1692,
    1894,
    1961,
    1902,
    1849,
    1967,
    1770,
    1987,
    1831,
    1728,
    1896,
    1805,
    1733,
    1918,
    1731,
    661,
    1776,
    1494,
    2005,
    2009,
    2004,
    1915,
    1695,
    1710,
    1804,
    1929,
    1725,
    1772,
    1933,
    609,
    1708,
    1822,
    1978,
    1811,
    1816,
    1073,
    1874,
    1845,
    1989,
    1696,
    1953,
    1823,
    1923,
    1907,
    1834,
    1806,
    1861,
    1785,
    297,
    1968,
    1764,
    1932,
    1937,
    1826,
    1732,
    1962,
    1916,
    1756,
    1975,
    1775,
    1922,
    1773,
]


def addsTo2020(L):
    numbers = list(set(L))
    possibilities = []
    for idx, x in enumerate(numbers):
        for y in numbers[idx:]:
            if x + y == 2020:
                possibilities += [[x, y]]
    return possibilities


def results():
    for [a, b] in addsTo2020(L):
        print(a * b)


results()
# part 2:
# The first half of this puzzle is complete! It provides one gold star: *

# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?


def three_addup2020():
    possibilities = []
    for (a, b, c) in list(itertools.combinations(list(set(L)), 3)):
        if a + b + c == 2020:
            possibilities += [[a, b, c]]
    return possibilities


def three_results():
    for [a, b, c] in three_addup2020():
        print(a * b * c)


three_results()


# generic nesting:


def generic_adding_up_number(number, n, L):
    combinations = list(itertools.combinations(list(set(L)), n))
    sums = list(filter(lambda x: sum(list(x)) == number, combinations))
    return list(map(lambda x: numpy.prod(list(x)), sums))



