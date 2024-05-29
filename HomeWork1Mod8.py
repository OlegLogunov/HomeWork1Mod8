def add_everything_up(a,b):
    try:
        result = a + b
    except TypeError as exc:
        result = str(a) + str(b)

    return result

print(add_everything_up(18,12))
print(add_everything_up("Университет", "Urban"))
print(add_everything_up(28, "май"))
