# Ensure tests can import the package modules from the `src` directory
# This makes the PYTHONPATH setting persistent for pytest runs
import sys
import os

PROJECT_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if PROJECT_SRC not in sys.path:
    sys.path.insert(0, PROJECT_SRC)
