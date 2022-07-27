# ref:app.betrybe.com/course/computer-science/introducao-a-python/,
# https://github.com/tryber/sd-013-c-project-job-insights/blob/
# Murilo-JobsInside/tests/sorting/test_sorting.py
# from src.sorting import sort_by

from src.sorting import sort_by
from pytest import raises

jobs = [
    {"date_posted": "2020-06-24", "max_salary": "180", "min_salary": "80"},
    {"date_posted": "2020-06-18", "max_salary": "110", "min_salary": "64"},
    {"date_posted": "2020-04-10", "max_salary": "220", "min_salary": "44"},
    {"date_posted": "2020-05-19", "max_salary": "132", "min_salary": "33"},
]

invalid_jobs = ["teste", None, True]


def test_sort_by_criteria():
    for criteria in invalid_jobs:
        with raises(ValueError, match=f"invalid sorting criteria: {criteria}"):
            sort_by(jobs, criteria)
