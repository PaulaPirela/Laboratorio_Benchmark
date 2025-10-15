# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

from typing import TypedDict

class Result(TypedDict):
    rate_2xx: float
    rate_4xx: float
    rate_5xx: float

def main(input: str) -> Result:
    raise NotImplementedError("Not implemented")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type="str", help="Path to s3 bucket with all data")
    args = parser.parse_args()

    print(main(args.input))
