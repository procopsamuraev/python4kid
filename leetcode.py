def reverseString(s: list) -> None:
    """
    Reverses the input list of characters in place.

    Args:
    s (list): A list of characters to be reversed.

    Returns:
    None: The list is modified in place.
    """
    left, right = 0, len(s) - 1
    while left < right:
        # Swap the elements at the left and right indices
        s[left], s[right] = s[right], s[left]
        # Move towards the middle
        left += 1
        right -= 1

# Example usage:
s = ['h', 'e', 'l', 'l', 'o']
reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']