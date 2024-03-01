import inspect
from typing import Any
from pathlib import Path
import re


BLACK_ON_YELLOW = "\033[30;43m"
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
            structure_value = structure

            structure_type = str(type(structure))

            # do some regex substitution to get a clear type representation
            structure_type = re.sub(r"<class '(.*)'>", r"\1", structure_type)

            extras = ""

            # special modifiers for certain types
            if structure_type == "int":
                structure_value = f"{structure_value:,}"  # auto comma delimiters
            elif structure_type in {"list", "set", "tuple", "str"}:
                structure_len = len(structure_value)
                extras += f", len={structure_len}"

            # getting where the dbg function was called is a bit harder
            in_function = None

            curframe = inspect.currentframe()
            calframe = inspect.getouterframes(curframe, 2)
            in_function = calframe[1][3]

            print(
                f"{BLACK_ON_YELLOW} dbg {RESET} {BLUE}{basename}:{DIM}{line_number}{RESET} {DIM}({in_function}){RESET} {YELLOW}{DIM}|{RESET} {GREEN}{structure_input} {DIM}={RESET} {CYAN}{structure_value} {MAGENTA}({structure_type}{extras}){RESET}"
            )

            break
