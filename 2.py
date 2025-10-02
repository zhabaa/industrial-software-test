def find_minimal_alphabet_prefix(sequence: list[int]) -> str | float | None:
    n = len(sequence)
    count = [0] * 27
    
    left = 0
    unique_chars = 0
    min_length = float('inf')

    for right in range(n):
        char = sequence[right]

        if 1 <= char <= 26:
            if count[char] == 0:
                unique_chars += 1

            count[char] += 1

        while unique_chars == 26:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length

            left_char = sequence[left]

            if 1 <= left_char <= 26:
                count[left_char] -= 1

                if count[left_char] == 0:
                    unique_chars -= 1

            left += 1
    
    return min_length if min_length != float('inf') else "NONE"


with open("input_files/data_prog_contest_problem_2.txt", "r", encoding="utf-8") as file:
    _ = file.readline()
    line: list[int] = list(map(int, file.readline().split()))

    print(find_minimal_alphabet_prefix(line))
