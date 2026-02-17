# main.py

from utilities import math_utils, string_utils
from data import data_loader


def main():
    # Using math_utils
    result = math_utils.add(10, 5)
    print(f"Addition Result: {result}")

    # Using string_utils
    upper = string_utils.to_uppercase("hello")
    print(f"Uppercase String: {upper}")

    # Using data_loader
    data = data_loader.load_data()
    print(f"Loaded Data: {data}")


if __name__ == "__main__":
    main()
