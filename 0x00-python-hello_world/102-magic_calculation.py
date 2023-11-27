import dis

def magic_calculation(a, b):
    result = 98
    result += a
    result = result ** b
    result += a
    return result

dis.dis(magic_calculation)
