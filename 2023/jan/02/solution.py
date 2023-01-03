
def is_upcase(letter):
    return letter in ['A',
                      'B',
                      'C',
                      'D',
                      'E',
                      'F',
                      'G',
                      'H',
                      'I',
                      'J',
                      'K',
                      'L',
                      'M',
                      'N',
                      'O',
                      'P',
                      'Q',
                      'R',
                      'S',
                      'T',
                      'U',
                      'V',
                      'W',
                      'X',
                      'Y',
                      'Z'
                      ]

class Solution:
    def detectCapitalUse(word):
        if len(word) == 1:
            return True
         # len(word) > 1
        first_letter_upcase = is_upcase(word[0])
        only_first_letter_upcase = first_letter_upcase
        all_letters_upcase = first_letter_upcase
        all_letters_downcase = not first_letter_upcase
         for letter in word[1:]:
            upcase = is_upcase(letter)
            all_letters_upcase = all_letters_upcase and upcase
            all_letters_downcase = all_letters_downcase and (not upcase)
            only_first_letter_upcase = only_first_letter_upcase and (not upcase)
         return all_letters_upcase or all_letters_downcase or only_first_letter_upcase
    
