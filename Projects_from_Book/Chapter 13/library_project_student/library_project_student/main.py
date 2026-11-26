# Fill in every ________ — file: main.py
"""Run this file to try out the library package."""
import ________
from library.utils import ________
import datetime ________ dt

print(f'Library package version {library.__version__}, loan period {LOAN_DAYS} days')

lib = library.________('City Library')
lib.add_book('111', '  python for beginners ', 'Sam Lee')
lib.add_book('222', 'data structures made easy', 'Priya Rao', copies=2)
lib.add_book('333', 'web development basics', 'Sam Lee')

for book in lib.________('Sam Lee'):
    print(book)

start = dt.________(2024, 3, 1)
print(lib.borrow('Ana', '111', start))
print(lib.borrow('Ben', '111', start))                      # only one copy
print(lib.give_back('Ana', '111', dt.date(2024, 3, 20)))    # 5 days late
print(lib.give_back('Cara', '222', start))                  # never borrowed
