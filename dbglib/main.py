import inspect
from typing import Any
from pathlib import Path
import re


BLACK_ON_YELLOW = "\033[30;43m"
BLACK_ON_RED = "\033[30;41m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
MAGENTA = "\033[35m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
DIM = "\033[2m"
ITALIC = "\033[3m"
RESET = "\033[0m"

# Print warning message as soon as module is imported
print(
    inspect.cleandoc(
        f"""
            {RESET}
            {BLACK_ON_RED}{BOLD} WARNING {RESET} {YELLOW}The development-only module 'dbglib' has been imported.
                      Please ensure that it is removed, along with all imports
                      and references as soon as you're done.
            {RESET}
        """
    )
)


def get_structure_type(structure):
    structure_type = str(type(structure))
    # do some regex substitution to get a clear type representation
    return re.sub(r"<class '(.*)'>", r"\1", structure_type)


def syntax_highlight(structure, structure_type):
    if structure_type == "int":
        return f"{YELLOW}{structure:,}{RESET}"
    elif structure_type == "str":
        return f"{GREEN}'{structure}'{RESET}"
    elif structure_type == "bool":
        bool_color = GREEN if structure else RED
        return f"{ITALIC}{bool_color}{structure}{RESET}"
    elif structure_type in {"list", "set", "tuple", "str"}:
        new = []
        for element in structure:
            new.append(syntax_highlight(element, get_structure_type(element)))

        return f"{RESET}[{RESET}{', '.join(new)}]{RESET}"

    return f"{BLUE}{str(structure)}{RESET}"


def dbg(structure: Any) -> None:
    stack = inspect.stack()

    for frame in stack:
        # FIX: code_context can only read one line
        #      if dbg(...) call is multilined,
        #      it will return incorrect info
        line = frame.code_context[0]

        if "dbg" in line:
            # read all text inside (...)
            # this is the best solution since we cannot
            # predict what structure would be
            # if we had to check if it was a callable,
            # literal, class etc, it would become extremely complex
            start = line.find("(") + 1
            end = line.rfind(")")

            # if end is not found, make it the length of line itself
            if end == -1:
                end = len(line)

            # base variable stats
            filename = frame.filename
            basename = Path(filename).name
            line_number = frame.lineno
            structure_input = line[start:end]
            structure_type = get_structure_type(structure)
            structure_value = syntax_highlight(structure, structure_type)

            # special modifiers for certain types
            extras = ""

            if structure_type in {"list", "set", "tuple", "str"}:
                structure_len = len(structure)
                extras += f", len={structure_len}"

            # getting where the dbg function was called is a bit harder
            in_function = None

            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            in_function = calframe[1][3]

            print(
                f"{BLACK_ON_YELLOW} dbg {RESET} {BLUE}{basename}:{DIM}{line_number}{RESET} {DIM}({in_function}){RESET} {YELLOW}{DIM}->{RESET} {structure_input} {DIM}={RESET} {structure_value} {MAGENTA}({structure_type}{extras}){RESET}"
            )

            break
