from typing import Optional

from solution import input_data2, convert_input_to_2d_list


def star_coordinates(data: list[list[str]]) -> Optional[tuple]:
    for x, row in enumerate(data):
        for y, value in enumerate(row):
            if value == "*":
                yield x, y


def adjacent_numbers(data: list[list[str]], x_cord: int, y_cord: int) -> list[int]:
    numbers = []
    skip = []
    for x in (x_cord - 1, x_cord, x_cord + 1):
        for y in (y_cord - 1, y_cord, y_cord + 1):
            if x == x_cord and y == y_cord or (x, y) in skip:
                continue

            if data[x][y].isdigit():
                number, coordinates = extract_whole_number_and_coordinates(data, x, y)
                skip.extend(coordinates)
                numbers.append(number)

    return numbers


def extract_whole_number_and_coordinates(data: list[list[str]], x_cord: int, y_cord: int) -> tuple[int, list]:
    index = y_cord
    while True:
        if index - 1 in range(len(data[x_cord])) and data[x_cord][index - 1].isdigit():
            index -= 1
            continue
        break
    start_index = index

    index = y_cord
    while True:
        if index + 1 in range(len(data[x_cord])) and data[x_cord][index + 1].isdigit():
            index += 1
            continue
        break
    end_index = index + 1

    number = "".join(data[x_cord][start_index:end_index])

    return int(number), [(x_cord, y) for y in range(start_index, end_index + 1)]


if __name__ == '__main__':
    data_in_2d_list = convert_input_to_2d_list(input_data2)
    gear_ratios = 0

    for star_x, star_y in star_coordinates(data_in_2d_list):
        nums = adjacent_numbers(data_in_2d_list, star_x, star_y)

        if len(nums) != 2:
            continue

        ratio = 1
        for num in nums:
            ratio *= num
        gear_ratios += ratio

    print(gear_ratios)
