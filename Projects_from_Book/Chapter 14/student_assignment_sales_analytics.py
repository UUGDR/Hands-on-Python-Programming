# Sales Analytics System
# Fill in every ________ to complete the program.
from functools import reduce, ________, wraps

sales = [
    {'region': 'North', 'product': 'Laptop',  'units': 5,  'price': 900.00},
    {'region': 'South', 'product': 'Laptop',  'units': 3,  'price': 900.00},
    {'region': 'North', 'product': 'Monitor', 'units': 8,  'price': 200.00},
    {'region': 'East',  'product': 'Monitor', 'units': 2,  'price': 200.00},
    {'region': 'East',  'product': 'Mouse',   'units': 40, 'price': 15.00},
    {'region': 'South', 'product': 'Mouse',   'units': 25, 'price': 15.00},
    {'region': 'North', 'product': 'Mouse',   'units': 10, 'price': 15.00},
]


def count_calls(func):
    """Decorator: counts how many times the wrapped function is called."""
    @________(func)
    def wrapper(*args, **kwargs):
        wrapper.calls ________ 1
        return ________(*args, **kwargs)
    wrapper.calls = 0
    return ________


@________
def revenue(sale):
    return sale['units'] * sale['price']


def group_total(records, key_func):
    """Sum the revenue of the records, grouped by whatever key_func returns."""
    totals = {}
    for record in records:
        key = ________(record)
        totals[key] = totals.________(key, 0) + revenue(record)
    return totals


def make_region_filter(region):
    """Return a NEW function that remembers which region to look for (a closure)."""
    return ________ sale: sale['region'] == region


def apply_discount(rate, amount):
    return amount * (1 - rate)


# --- Main program ---
revenues = list(________(revenue, sales))
print('Revenue per sale :', revenues)

grand_total = ________(lambda a, b: a + b, revenues)
print(f'Total revenue    : ${grand_total:,.2f}')

big_sales = list(________(lambda sale: revenue(sale) >= 500, sales))
print('Big sales (500+) :', [f"{s['region']} {s['product']}" for s in big_sales])

top3 = sorted(sales, key=________, reverse=True)[:3]
print('Top 3 sales      :', [f"{s['product']} ({s['region']})" for s in top3])

by_product = group_total(sales, ________ sale: sale['product'])
by_region = group_total(sales, lambda sale: sale[________])
print('By product       :', by_product)
print('By region        :', by_region)

best = max(by_product, key=by_product.________)
print('Best product     :', best)

north_only = ________('North')
north_sales = list(filter(________, sales))
print('North sales      :', len(north_sales))

ten_off = ________(apply_discount, 0.10)
discounted = list(map(________, revenues[:3]))
print('After 10% off    :', discounted)
print(f'revenue() was called {revenue.________} times')
