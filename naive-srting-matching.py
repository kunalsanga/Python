def naive_string_matcher(text,pattern):
    n=len(text)
    m=len(pattern)

    for i in range(n-m+1):
        match = True
        for j in range(m):
            if text[i+j]!=pattern[j]:
                match = False
                break
        if match:print(f"pattern found at index {i}")

text="ABAAABCDBBABCDDEBCABC"
pattern = "ABC"
naive_string_matcher(text,pattern)