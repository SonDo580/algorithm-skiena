def find_index_match(pattern, text):
    text_len = len(text)
    pattern_len = len(pattern)

    for i in range(text_len - pattern_len + 1):
        matched = True
        for j in range(pattern_len):
            if text[i + j] != pattern[j]:
                matched = False
                break
        if matched:
            return i
    
    return -1

# Usage:
def main():
    text = "hello world"
    pattern = "world"

    result = find_index_match(pattern, text)
    if result != -1:
        print(f"Pattern found at index {result}")
    else:
        print("Pattern not found")

if __name__ == "__main__":
    main()
