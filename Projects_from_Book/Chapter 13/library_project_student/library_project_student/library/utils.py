# Fill in every ________ — file: library/utils.py
"""Helper functions shared by the rest of the package."""
from datetime import date, ________

LOAN_DAYS = 14
FINE_PER_DAY = 0.25


def due_date(borrowed_on):
    """A book is due LOAN_DAYS days after it is borrowed."""
    return borrowed_on + timedelta(days=________)


def late_fee(due, returned):
    """Charge FINE_PER_DAY for every day late; nothing if on time."""
    days_late = (returned - due).days
    return ________(0, days_late) * FINE_PER_DAY


def clean_title(title):
    """' python basics ' becomes 'Python Basics'."""
    return title.strip().________()


if ________ == '__main__':
    # Runs only when this file is executed directly, not when it is imported
    print('Self-test:', due_date(date(2024, 3, 1)))
