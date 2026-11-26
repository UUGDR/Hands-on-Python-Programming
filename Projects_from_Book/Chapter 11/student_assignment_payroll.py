# Payroll Entry and Validation System
# Fill in every ________ to complete the program.

class PayrollError(________):
    """Base class for every payroll problem."""


class InvalidHoursError(________):
    """Hours worked are outside the allowed range."""


class InvalidRateError(PayrollError):
    """Hourly rate is below the minimum wage."""


MIN_RATE = 15.00
MAX_HOURS = 80


def parse_record(line):
    """Turn 'E101, Ana, 45, 20.00' into clean values, or raise a PayrollError."""
    parts = [part.strip() for part in line.split(',')]
    if len(parts) ________ 4:
        ________ PayrollError(f'expected 4 fields but found {len(parts)}')
    emp_id, name, hours_text, rate_text = parts
    try:
        hours = ________(hours_text)
        rate = float(rate_text)
    except ________:
        raise PayrollError('hours and rate must be numbers')
    if not 0 <= hours <= MAX_HOURS:
        raise ________(f'{hours:g} hours is outside 0-{MAX_HOURS}')
    if rate ________ MIN_RATE:
        raise InvalidRateError(f'rate ${rate:.2f} is below the ${MIN_RATE:.2f} minimum')
    return emp_id, name, hours, rate


def gross_pay(hours, rate):
    """Hours over 40 are overtime, paid at 1.5 times the rate."""
    overtime = ________(0, hours - 40)
    return (hours - overtime) * rate + overtime * rate * 1.5


def average_pay(pay_list):
    return sum(pay_list) ________ len(pay_list)


# --- Main program ---
records = [
    'E101, Ana, 45, 20.00',
    'E102, Ben, forty, 18.50',
    'E103, Cara, 38, 16.00',
    'E104, Dev, 120, 22.00',
    'E105, Eli, 40, 12.50',
    'E106, Fay',
    'E107, Gus, 40, 25.00',
]
paid = ________
errors = 0
checked = 0
________ line in records:
    ________:
        emp_id, name, hours, rate = parse_record(line)
    except (________, InvalidRateError) as error:
        print(f'RANGE ERROR : {line} -> {________}')
        errors += 1
    except ________ as error:
        print(f'DATA ERROR  : {line} -> {error}')
        errors += 1
    ________:
        pay = gross_pay(hours, rate)
        paid.append(pay)
        print(f'OK          : {emp_id} {name:<5} ${pay:>9,.2f}')
    ________:
        checked ________ 1               # runs for every record, good or bad

print(f'Records checked: {checked}, valid: {len(paid)}, errors: {errors}')
for batch in (paid, []):
    try:
        print(f'Average pay: ${average_pay(batch):,.2f}')
    except ________:
        print('Average pay: no valid records')
