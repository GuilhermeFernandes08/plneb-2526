def vowels_string(s):
    count=0
    vowels='aeiouAEIOU'
    for l in s:
        if l in vowels:
            count+=1
    print(count)

vowels_string("Aldeia")