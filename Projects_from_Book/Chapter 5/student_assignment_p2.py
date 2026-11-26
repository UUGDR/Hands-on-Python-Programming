# Project 2: Employee Greeting & Badge Generator
# Fill in every ________ to complete the program.

# ── Function 1: greet_employee ──────────────────────────────────
# Default parameters make 'title' and 'department' optional
def greet_employee(name, title=________, department=________):
    """Print a personalised welcome message for an employee."""
    print(f'Welcome, {________} {name} of {________}!')

# ── Function 2: format_badge ─────────────────────────────────────
def format_badge(name, id_number, company=________, role=________):
    """Return a formatted badge string for an employee."""
    lines = [
        '-------- BADGE --------',
        f'| {________:<20}|',
        f'| Name : {________:<13}|',
        f'| ID   : {________:<13}|',
        f'| Role : {________:<13}|',
        '-----------------------',
    ]
    return '\n'.join(________)

# ── Function 3: calculate_annual_leave ───────────────────────────
def calculate_annual_leave(years_served, base_days=________, bonus_per_year=________):
    """Return total annual leave days earned."""
    return ________ + (years_served * ________)

# ── Main program ──────────────────────────────────────────────────

# Call with all arguments (positional)
greet_employee('Sarah Chen', 'Dr.', 'Engineering')

# Call with ONLY the required argument — defaults fill in the rest
greet_employee(________)

# Call using KEYWORD arguments — order does not matter
greet_employee(department='Marketing', name='Lisa Park', title='Manager')

print()

# format_badge: positional required args, keyword optional args
badge1 = format_badge('Sarah Chen', 'E-1042', role='Lead Engineer')
print(________)

print()

# Use only required args — company and role get their defaults
badge2 = ________('Bob Martinez', 'E-2001')
print(badge2)

print()

# calculate_annual_leave: demonstrate default vs custom bonus
sarah_leave = calculate_annual_leave(________, bonus_per_year=3)  # 6 years
bob_leave   = calculate_annual_leave(0)  # new employee, all defaults

print(f'Sarah Chen  — Annual leave: {________} days')
print(f'Bob Martinez — Annual leave: {bob_leave} days')
