from typing import List


class Solution:
    # Helper function to convert count to array of digits
    def count_to_digits(self, count: int) -> List[str]:
        digits = []
        while count:
            digits.insert(0, str(count % 10))
            count //= 10
        return digits

    def compress(self, chars: List[str]) -> int:
        # Initialize variables
        pointer = 0  # Pointer to iterate through the chars
        current_char = chars[pointer]  # Current character
        compressed_chars = []  # List to store compressed chars
        char_count = 0  # Counter for the current character

        # Iterate through the chars
        while pointer < len(chars):
            # If current character matches the character at pointer
            if current_char == chars[pointer]:
                char_count += 1  # Increment count
            else:
                # Append the current character to compressed list
                compressed_chars.append(current_char)
                # If count is greater than 1, add its digits to compressed list
                if char_count > 1:
                    compressed_chars.extend(self.count_to_digits(char_count))
                # Update current character and reset count
                current_char = chars[pointer]
                char_count = 1
            pointer += 1  # Move to the next character
        
        # Append the last character and its digits to compressed list
        compressed_chars.append(current_char)
        if char_count > 1:
            compressed_chars.extend(self.count_to_digits(char_count))
        
        chars.clear()  # Clear the original list
        chars.extend(compressed_chars)  # Extend the original list with the compressed list
        return len(chars)  # Return the length of the compressed list
