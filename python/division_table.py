import argparse
import math


def direct_division(value: float, divisor: float) -> float:
    return value / divisor


def reciprocal_multiply(value: float, reciprocal: float) -> float:
    return value * reciprocal


def format_number(value: float) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    return repr(value)


def print_table(value: float, divisor: float, iterations: int) -> None:
    reciprocal = 1.0 / divisor
    headers = ["iteration", "division", "multiplication", "difference", "relative error"]
    rows = []
    divided = value
    multiplied = value

    for iteration in range(iterations):
        divided = direct_division(divided, divisor)
        multiplied = reciprocal_multiply(multiplied, reciprocal)
        rows.append(
            [
                str(iteration),
                format_number(divided),
                format_number(multiplied),
                format_number(multiplied - divided),
                format_number(abs((multiplied - divided) / divided)) if divided != 0.0 else "-",
            ]
        )

    widths = [max(len(row[index]) for row in [headers, *rows]) for index in range(len(headers))]
    print(f"value: {format_number(value)}")
    print(f"divisor: {format_number(divisor)}")
    print(f"reciprocal: {format_number(reciprocal)}")
    print(f"iterations: {iterations}")
    print()
    print("  ".join(header.ljust(width) for header, width in zip(headers, widths, strict=True)))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print("  ".join(cell.ljust(width) for cell, width in zip(row, widths, strict=True)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=float)
    parser.add_argument("divisor", type=float)
    parser.add_argument("iterations", type=int)
    args = parser.parse_args()

    print_table(args.value, args.divisor, args.iterations)


if __name__ == "__main__":
    main()
