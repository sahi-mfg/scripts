def find_odd_square(n: int) -> list[int]:
    """

    Find the n first odd square numbers

    Args:
        n: int: the number of odd square numbers
    Returns:
        A list with n odd square numbers.

    """
    return [i**2 for i in range(1, n + 1) if i % 2 != 0]


if __name__ == "__main__":
    odd_squares = find_odd_square(284000)
    print(odd_squares)
    print(f"Sum of odd squares: {sum(odd_squares)}")
