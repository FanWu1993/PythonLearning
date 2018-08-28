def checkio(data: str) -> bool:

    #replace this for solution
    if len(data) < 10:
        return False
    has_u = False
    has_l = False
    has_d = False
    for c in data:
        if c.islower():
            has_l = True
        elif c.isupper():
            has_u = True
        elif c.isdigit():
            has_d = True
        else:
            return False
    return has_l and has_u and has_d
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")