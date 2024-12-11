[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)

# Python Advent of Code Repo (v. 2024)

This repository is managed using [uv](). To learn more about why I like using UV to build my Python packages, please see
[this ADR](https://github.com/kasittig/cv/blob/main/adr/0002-use-uv-python-package-management.md) from my CV repository.

## Usage

If you have `uv` installed, you can run the interactive CLI using the following command:


    uv run main.py

This will start up the interactive CLI. There are commands to both generate code stubs and to run your code:

    (Cmd) help

    Documented commands (type help <topic>):
    ========================================
    help
    
    Undocumented commands:
    ======================
    exit  list_days  setup  solve

### Entering puzzle inputs

Your CLI will automatically read puzzle inputs from your `inputs/` directory. You should name the input for each day using the `day_{N}.txt` filename format.

    kasittig ~/Projects/advent-of-code-2024/py [main] $ ls inputs/
    day_1.txt	day_2.txt	day_3.txt