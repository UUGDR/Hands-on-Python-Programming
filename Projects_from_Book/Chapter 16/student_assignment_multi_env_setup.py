# Multi-Environment Python Project Setup
# Fill in every ________ to complete the program.
import os
import subprocess
import sys
import tempfile
import venv

# Each project gets its own packages, pinned to exact versions.
PROJECTS = {
    'web-scraper':   ['requests==2.32.3', 'beautifulsoup4==4.12.3'],
    'data-analysis': ['pandas==2.2.2', 'numpy==1.26.4', 'matplotlib==3.9.0'],
    'web-app':       ['flask==3.0.3', 'gunicorn==22.0.0'],
}

# Set to True on your own computer (needs internet) to really install the packages.
INSTALL_PACKAGES = False

# The script that is saved as main.py in every project and run by that project's own Python.
SCRIPT = (
    'import sys\n'
    'from importlib.metadata import distributions\n'
    'print("{name}: isolated =", sys.prefix != sys.________, '
    '"| packages installed =", len(list(distributions())))\n'
)


def env_python(env_dir):
    """Path of the Python program inside a virtual environment (differs on Windows)."""
    folder = 'Scripts' if os.name == '________' else 'bin'
    program = 'python.exe' if os.name == 'nt' else 'python'
    return os.path.________(env_dir, folder, program)


def create_environment(project_dir):
    """Create a virtual environment called .venv inside the project folder."""
    env_dir = os.path.join(project_dir, '.venv')
    venv.________(with_pip=INSTALL_PACKAGES).________(env_dir)
    return env_dir


def write_requirements(project_dir, packages):
    path = os.path.join(project_dir, 'requirements.txt')
    with open(path, '________', encoding='utf-8') as file:
        file.write('\n'.________(packages) + '\n')
    return path


# --- Main program ---
names_by_project = {}
with tempfile.TemporaryDirectory() as base:
    for name, packages in PROJECTS.items():
        project_dir = os.path.join(base, name)
        os.________(project_dir)
        env_dir = create_environment(project_dir)
        requirements = write_requirements(project_dir, packages)
        names_by_project[name] = {item.________('==')[0] for item in packages}

        script = os.path.join(project_dir, 'main.py')
        with open(script, 'w', encoding='utf-8') as file:
            file.write(SCRIPT.format(name=name))

        print(f'Created {name}/.venv with {len(packages)} requirement(s)')
        if INSTALL_PACKAGES:
            subprocess.run([env_python(env_dir), '-m', '________', '________', '-r', requirements], check=True)
        result = subprocess.run([env_python(env_dir), script], capture_output=True, text=True, check=True)
        print(' ', result.stdout.strip())

    print()
    print('Packages per project:')
    for name, names in names_by_project.items():
        print(f'  {name:<14}{", ".join(sorted(names))}')
    shared = set.________(*names_by_project.values())
    print('Shared by all three:', ', '.join(sorted(shared)) or 'nothing')
    print('Activate on Mac/Linux : source .venv/bin/activate')
    print('Activate on Windows   : .venv\\Scripts\\activate')
