def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    
    if m > n:
        return 0  # No match possible if the pattern is longer than the text

    base = 256
    prime = 101
    hash_pattern = 0
    hash_text = 0
    h = 1

    # Calculate the value of h (base^(m-1) % prime)
    for i in range(m - 1):
        h = (h * base) % prime

    # Calculate initial hash values for the pattern and the first window of text
    for i in range(m):
        hash_pattern = (base * hash_pattern + ord(pattern[i])) % prime
        hash_text = (base * hash_text + ord(text[i])) % prime

    # Slide the pattern over the text one character at a time
    for i in range(n - m + 1):
        # Check if the hash values match
        if hash_pattern == hash_text:
            # Verify characters to rule out hash collisions
            if text[i:i + m] == pattern:
                return len(pattern)  # Return the length of the matched pattern

        # Calculate the hash for the next window of text
        if i < n - m:
            hash_text = (base * (hash_text - ord(text[i]) * h) + ord(text[i + m])) % prime
            if hash_text < 0:
                hash_text += prime

    return 0  # Return 0 if no match is found