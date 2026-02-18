def balanced_string(s1, s2):
    for l in s1:
        if l not in s2:
            return False
    return True

print(balanced_string("saber", "sabedoria"))
print(balanced_string("sabedoria", "saber"))