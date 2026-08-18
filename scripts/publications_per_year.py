#!/usr/bin/env python3

## -----------------------------------------------------------------------------
##
## SPDX-License-Identifier: LGPL-2.1-or-later
## Copyright (C) 2026 by Wolfgang Bangerth
##
## This file is part of the deal.II publication list.
##
## -----------------------------------------------------------------------------

"""Display the number of publications in each year.

The script finds ``publications-YYYY.bib`` files in the current directory,
counts their BibTeX entries, and opens a matplotlib bar chart. Directives such
as ``@comment``, ``@preamble``, and ``@string`` are not counted as entries.

Run ``python3 publications_per_year.py`` from the repository root. Use
``--input-directory`` to plot files from another directory.
"""

import argparse
import re
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


ENTRY_PATTERN = re.compile(
    r"^\s*@(?!(?:comment|string|preamble)\s*[\{\(])[A-Za-z]+\s*[\{\(]",
    re.IGNORECASE | re.MULTILINE,
)
FILENAME_PATTERN = re.compile(r"^publications-(\d{4})\.bib$")
INCOMPLETE_DATA_START_YEAR = 2025


def count_entries_by_year(input_directory: Path) -> dict[int, int]:
    """Count BibTeX entries in each publications-YYYY.bib file."""
    counts = Counter()

    for bib_file in input_directory.glob("publications-*.bib"):
        match = FILENAME_PATTERN.match(bib_file.name)
        if match is None:
            continue

        counts[int(match.group(1))] += len(
            ENTRY_PATTERN.findall(bib_file.read_text(encoding="utf-8"))
        )

    return dict(sorted(counts.items()))


def create_chart(counts: dict[int, int]) -> None:
    """Display a bar chart for the supplied publication counts."""
    years = list(counts)
    values = list(counts.values())
    colors = [
        "#808080" if year >= INCOMPLETE_DATA_START_YEAR else "#377eb8"
        for year in years
    ]

    figure, axis = plt.subplots(figsize=(12, 6))
    axis.bar(years, values, color=colors)
    axis.set_xlabel("Year")
    axis.set_ylabel("Publications")
    axis.set_title("Publications in a given year")
    axis.set_xticks(years)
    axis.tick_params(axis="x", rotation=45)
    axis.set_ylim(bottom=0)
    figure.tight_layout()
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a bar chart of entries in publications-YYYY.bib files."
    )
    parser.add_argument(
        "--input-directory",
        type=Path,
        default=Path.cwd(),
        help="directory containing publications-YYYY.bib files (default: current directory)",
    )
    arguments = parser.parse_args()

    counts = count_entries_by_year(arguments.input_directory)
    if not counts:
        parser.error(
            f"no publications-YYYY.bib files found in {arguments.input_directory}"
        )

    create_chart(counts)


if __name__ == "__main__":
    main()
