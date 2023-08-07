import random

def generate_lotto_numbers():
    lotto_numbers = random.sample(range(15, 46), 6)
    return lotto_numbers

def main():
    num_lines = 5  # 출력할 줄 수
    for line in range(num_lines):
        numbers = generate_lotto_numbers()
        print(f"줄 {line + 1}: {', '.join(str(num) for num in numbers)}")

if __name__ == "__main__":
    main()
