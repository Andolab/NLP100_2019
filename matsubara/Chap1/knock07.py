from string import Template


def format_str(x, y, z):
    # x = str(x)
    # y = str(y)
    # z = str(z)
    # return x + "時の" + y + "は" + z

    s = Template("$hour時の$targetは$value")
    return s.substitute(hour=x, target=y, value=z)


print(format_str(12, "気温", 22.4))
