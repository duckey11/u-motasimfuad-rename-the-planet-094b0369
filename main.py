"""Rename the Planet entry.

The joke: Mercury's solar day (sunrise to sunrise) lasts 176 Earth
days, while its whole year is only 88 Earth days, so a single day
there is literally two years long. The name riffs on the film about
one day repeating forever, squared because Mercury's day is doubled.
The last beat flips an ordinary five-minute morning ritual, brewing
coffee, into a wait that outlasts two birthdays.
"""

ENTRY = (
    "Rename Mercury 'Groundhog Day Squared' because one day there lasts "
    "176 Earth days while its year is only 88, so your morning coffee is "
    "still brewing when your second birthday cake arrives."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
