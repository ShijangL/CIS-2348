# Shijang Lin PSID: 2018904

# zyLab 14.11

from os import system

system('cls')


def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j

        numbers[i], numbers[index_largest] = numbers[index_largest], numbers[i]

        for k in numbers:
            print(k, end=' ')
        print()


if __name__ == "__main__":
    numlist = [int(x) for x in input().split(' ')]
    selection_sort_descend_trace(numlist)
