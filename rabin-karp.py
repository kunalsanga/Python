def rabin_karp(pattern, text, prime=101):
    m = len(pattern)
    n = len(text)
    d = 256  # Number of characters in the input alphabet
    h = pow(d, m-1, prime)  # d^(m-1) % prime
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    result = []

    # Preprocessing: calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for s in range(n - m + 1):
        # Check the hash values
        if p == t:
            # Check characters one by one
            if text[s:s+m] == pattern:
                result.append(s)

        # Calculate hash value for next window of text
        if s < n - m:
            t = (d*(t - ord(text[s])*h) + ord(text[s + m])) % prime
            if t < 0:
                t += prime

    return result

text = "ababcabcabababd"
pattern = "ababd"
matches = rabin_karp(pattern, text)

print("Pattern found at positions:", matches)
