import csv
from collections import Counter
from pathlib import Path


def count_by_status(path: Path) -> dict[str, int]:
    counts = Counter()
    with path.open(newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            counts[row["status"]] += 1
    return dict(counts)


def main() -> None:
    counts = count_by_status(Path("data/tickets.csv"))
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")


if __name__ == "__main__":
    main()