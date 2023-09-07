def count_vowels_consonants(word):
    vowels = 'aeiouyAEIOUY'
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1

    return vowel_count, consonant_count

lst = ['Python', 15442, 32, 'QweRty', 34, 19, 'love']

for item in lst:
    if isinstance(item, str):
        vowels, consonants = count_vowels_consonants(item)
        print("Word:", item)
        print("Vowels:", vowels)
        print("Consonants:", consonants)
        print()
