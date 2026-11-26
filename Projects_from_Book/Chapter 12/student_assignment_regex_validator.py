# Student Data Validator and Extractor
# Fill in every ________ to complete the program.
import ________

# Splits one record line into named fields. re.VERBOSE lets us add spaces and comments.
RECORD_RE = re.________(r'''
    ID:\s*(?P<id>[^;]+);\s*          # student ID (anything up to the next semicolon)
    Name:\s*(?P<________>[^;]+);\s*      # full name
    Email:\s*(?P<email>[^;]+);\s*    # email address
    DOB:\s*(?P<dob>.+)               # date of birth (the rest of the line)
''', re.________)

# Patterns that decide whether each field is acceptable
ID_RE      = re.compile(r'S\d{________}-\d{3}')                # S2024-001
EMAIL_RE   = re.compile(r'[a-z]________\.[a-z]+@uni\.edu')     # first.last@uni.edu
DOB_RE     = re.compile(r'(\d{2})/(\d{2})/(\d________)')     # day/month/year
COURSE_RE  = re.compile(r'________[A-Z]{2,4}\d{3}\b')         # CS101, MATH201
EMAIL_FIND = re.compile(r'[\w.]+@[\w.]+\w')             # any email inside free text
PHONE_RE   = re.compile(r'\b\d{3}-\d{4}\b')             # 555-0142


def check_record(line):
    """Return (fields, problems) for one record line."""
    match = RECORD_RE.________(line.strip())
    if match ________ None:
        return None, ['line is not in the expected format']
    fields = match.________()
    problems = []
    if not ID_RE.________(fields['id']):
        problems.________('bad student ID')
    if not EMAIL_RE.fullmatch(fields['email']):
        problems.append('bad email')
    if not DOB_RE.fullmatch(fields['dob']):
        problems.append('bad date of birth')
    return fields, problems


def iso_date(dob):
    """Turn 14/03/2003 into 2003-03-14 by reordering the three groups."""
    return DOB_RE.sub(r'\3-\________-\1', dob)


def redact_ids(text):
    return ID_RE.________('SID-XXXX', text)


# --- Main program ---
RECORDS = '''ID: S2024-001; Name: Ana Torres; Email: ana.torres@uni.edu; DOB: 14/03/2003
ID: S2024-002; Name: Ben Okafor; Email: ben.okafor@uni.edu; DOB: 02/11/2002
ID: S2024-03; Name: Cara Lin; Email: cara.lin@uni.edu; DOB: 21/07/2004
ID: S2024-004; Name: Dev Patel; Email: dev.patel@gmail.com; DOB: 09/09/2003
ID: S2024-005; Name: Eli Ross; Email: eli.ross@uni.edu; DOB: 3/7/2004
ID: S2024-006 Name: Fay Wong; Email: fay.wong@uni.edu; DOB: 30/12/2003'''
NOTES = ('Advisor note: S2024-001 must retake MATH201 and CS101. '
         'S2024-002 passed ENG105, contact ben.okafor@uni.edu or call 555-0142.')

valid = []
lines = RECORDS.________('\n')
for number, line in ________(lines, 1):
    fields, problems = check_record(line)
    if problems:
        label = fields['id'] if fields else f'line {number}'
        reason = ', '.________(problems)
        print(f'INVALID : {label:<10} {reason}')
    else:
        valid.________(fields)
        print(f'OK      : {fields["id"]} {fields["name"]:<10} born {iso_date(fields["dob"])}')

print(f'Valid records: {len(valid)} of {len(lines)}')
print()
print('Courses mentioned:', sorted(set(COURSE_RE.________(NOTES))))
print('Emails mentioned :', EMAIL_FIND.findall(NOTES))
print('Phones mentioned :', PHONE_RE.findall(NOTES))
print('Redacted note    :', redact_ids(NOTES))
