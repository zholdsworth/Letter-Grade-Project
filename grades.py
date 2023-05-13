# Add function to calculate letter grade
# Improve input validation for scores in calculate_grades function
from typing import List


def calculate_grades(scoreslst: List[int]) -> List[str]:
    """
    Given a list of scores, calculates letter grades according to scale in for loop.
    :param scoreslst: A list of integer scores.
    :return: List[str]: A list of string grades corresponding to the input scores.
    """

    if not isinstance(scoreslst, list):
        raise TypeError("Input must be a list")

    if not all(isinstance(score, int) for score in scoreslst):
        raise TypeError("All elements of input list must be integers")

    if len(scoreslst) == 0:
        raise ValueError("Input list cannot be empty")

    maxscore = max(scoreslst)
    grades = []

    for score in scoreslst:
        if score >= (maxscore - 10):
            grade = "A"
        elif score >= (maxscore - 20):
            grade = "B"
        elif score >= (maxscore - 30):
            grade = "C"
        elif score >= (maxscore - 40):
            grade = "D"
        else:
            grade = "F"

        grades.append(grade)

    return grades
