import string


# declare function
def say_hi(name):
    print("Hi " + name)


def print_min(num_1, num_2):
    if num_1 < num_2:
        print(num_1)
    else:
        print(num_2)


def test_print(text="Hello World"):
    print(text)


def get_multiple(num_1, num_2):
    return num_1 * num_2


def get_odd_indexes_list(list):
    new_list = []
    i = 0
    while i < len(list):
        if i % 2 != 0:
            new_list.append(list[i])
    return new_list


# Write a Python function to multiply all the numbers in a list.
def list_multiply(numbers):
    i = 0
    m = 1
    while i < len(numbers):
        m *= numbers[i]
        i += 1
    return m


def calculate_seconds(h, m, s):
    return h * 3600 + m * 60 + s


def get_text(text):
    l = len(text)
    p = l // 2
    t1 = text[0:p].lower()
    t2 = text[p:l].upper()
    return t1 + t2

def reverse_string(text):
    text_length = len(text)
    i = text_length
    text_reversed = ''
    while i > 0:
        text_reversed += text[i - 1]
        i -= 1
    return text_reversed


def letter_case_counter(text):
    i = 0
    l = 0
    u = 0
    while i < len(text):
        if text[i] in string.ascii_lowercase:
            l += 1
        elif text[i] in string.ascii_uppercase:
            u += 1
        i += 1
    return l, u


def get_even_list(nums):
    i = 0
    new_list = []
    while i < len(nums):
        if nums[i] % 2 == 0:
            new_list.append(nums[i])
        i += 1
    return new_list


def main():
    x = get_text("Hello John")
    print(x)


if __name__ == "__main__":
    main()
