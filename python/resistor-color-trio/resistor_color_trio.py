COLORS = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9"
}

metric_prefix = {1000000000: "giga", 1000000: "mega", 1000: "kilo"}


def color_to_value(colors):
    numbers = []
    for index, color in enumerate(colors):
        if index < 3:
            value = COLORS.get(color)
            if index == 2:
                value = str(int(value) * "0")
            numbers.append(value)
    return numbers


def convert_to_metric(value):
    suffix = "ohms"
    for base, prefix in metric_prefix.items():
        if value >= base:
            suffix = f"{prefix}{suffix}"
            value = int(value / base)
            break
    return f"{value:g} {suffix}"


def label(colors):
    numbers = color_to_value(colors)
    value = int(''.join(numbers))
    return convert_to_metric(value)
