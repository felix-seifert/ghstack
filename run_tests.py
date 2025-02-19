#!/usr/bin/env python3

import subprocess
import os

# Set environment variable
os.environ['LIBCST_PARSER_TYPE'] = 'native'


def main():
    try:
        # ufmt check ghstack
        subprocess.run(['ufmt', 'check', 'ghstack'], check=True)

        # flake8 ghstack
        subprocess.run(['flake8', 'ghstack'], check=True)

        # mypy --install-types --non-interactive -m ghstack
        subprocess.run(
            ['mypy', '--install-types', '--non-interactive', '-m', 'ghstack'],
            check=True)

        # pytest --verbose
        subprocess.run(['pytest', '--verbose'], check=True)

        print("OK")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
