# Student Grade Tracker with a Full Git Workflow
# Fill in every ________ to complete the program.
import os
import subprocess
import tempfile

# ---------- Part 1: the grade tracker ----------


def add_grade(grades, name, score):
    """Store one score for a student; reject anything that is not a number from 0 to 100."""
    if not ________(score, (int, float)) or not 0 <= score <= 100:
        raise ValueError(f'Invalid score for {name}: {score}')
    grades.________(name, []).append(score)


def average(scores):
    return ________(scores) / len(scores)


def median(scores):
    ordered = ________(scores)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def letter(avg):
    for cutoff, grade in ((90, 'A'), (80, 'B'), (70, 'C'), (60, 'D')):
        if avg >= cutoff:
            return grade
    return 'F'


def report(grades):
    for name, scores in ________(grades.items()):
        avg = average(scores)
        print(f'{name:<6} avg {avg:6.2f}  median {median(scores):5.1f}  '
              f'best {max(scores)}  grade {letter(avg)}')


# ---------- Part 2: the Git workflow ----------


def git(folder, *args):
    """Run one git command inside folder and return its output."""
    result = subprocess.run(['git', *args], cwd=folder, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def write(folder, filename, text):
    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as file:
        file.write(text)


def read(folder, filename):
    with open(os.path.join(folder, filename), encoding='utf-8') as file:
        return file.read()


def feature(folder, branch, filename, text, message):
    """The professional cycle: branch -> edit -> commit -> merge into main -> delete branch."""
    git(folder, 'checkout', '________', branch)
    write(folder, filename, text)
    git(folder, '________', filename)
    git(folder, '________', '-m', message)
    git(folder, 'checkout', 'main')
    git(folder, '________', '________', branch, '-m', f'Merge {branch}')
    git(folder, 'branch', '________', branch)


TRACKER_V1 = 'def average(scores):\n    return sum(scores) // len(scores)\n'
STATS_V1 = 'def median(scores):\n    ordered = sorted(scores)\n    return ordered[len(ordered) // 2]\n'

# --- Main program ---
grades = {}
for student, scores in {'Alice': [92, 88, 95], 'Ben': [75, 64, 81],
                        'Cara': [58, 71, 66], 'Dev': [85, 90, 78]}.items():
    for score in scores:
        add_grade(grades, student, score)
try:
    add_grade(grades, 'Ben', 105)
except ValueError as error:
    print('Rejected:', error)
report(grades)

with tempfile.TemporaryDirectory() as base:
    remote = os.path.join(base, 'github.git')      # a local stand-in for GitHub
    project = os.path.join(base, 'grade-tracker')
    os.mkdir(project)
    subprocess.run(['git', 'init', '--bare', '-b', 'main', remote], check=True, capture_output=True)

    git(project, '________', '-b', 'main')
    git(project, 'config', 'user.name', 'Student')
    git(project, 'config', 'user.email', 'student@example.com')
    git(project, '________', 'add', 'origin', remote)

    write(project, 'README.md', '# Student Grade Tracker\n')
    git(project, 'add', 'README.md')
    git(project, 'commit', '-m', 'Initial commit: add README')

    feature(project, 'feature/add-grades', 'tracker.py', TRACKER_V1, 'Add grade tracker with average')
    feature(project, 'feature/statistics', 'stats.py', STATS_V1, 'Add statistics module with median')
    fixed = read(project, 'tracker.py').________('//', '/')
    feature(project, 'bugfix/average-division', 'tracker.py', fixed, 'Fix average: use true division')

    git(project, '________', '-a', 'v1.0', '-m', 'Release 1.0')
    git(project, '________', '-u', 'origin', 'main')
    git(project, 'push', 'origin', 'v1.0')

    print()
    print('Commit history (oldest first):')
    for subject in git(project, 'log', '--topo-order', '--reverse', '--format=%s').________():
        print(' -', subject)
    print('Branches left   :', git(project, 'branch', '--format=%(refname:short)'))
    print('Tags            :', git(project, 'tag'))
    print('Tags on remote  :', git(remote, 'tag'))
    print('Bug fixed       :', '//' not in read(project, 'tracker.py'))
    print('Working tree    :', 'clean' if not git(project, 'status', '--porcelain') else 'dirty')
