import os
import sys
import pytest

# Add project root (folder that contains "src" and "tests") to Python path
project_root = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)
sys.path.append(project_root)

from src.homework.c_decisions.decisions import get_letter_grade


def test_letter_grade_A():
    assert get_letter_grade(95) == "A"


def test_letter_grade_B():
    assert get_letter_grade(85) == "B"


def test_letter_grade_C():
    assert get_letter_grade(75) == "C"


def test_letter_grade_D():
    assert get_letter_grade(65) == "D"


def test_letter_grade_F():
    assert get_letter_grade(50) == "F"
