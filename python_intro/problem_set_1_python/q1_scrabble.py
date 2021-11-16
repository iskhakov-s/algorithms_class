def scrabble_score(word: str, score_dict: dict[str, int]):
    """[Finds the scrabble score of a given word, given the point values in the dictionary]

    Args:
        word (str): [any string with letters]
        score_dict (dict[str, int]): [dict that associates characters with int point values]

    Returns:
        [type]: [returns the sum of the point values of each letter, as in scrabble]
    """
    score = 0
    for letter in word:
        score += score_dict[letter] if letter in score_dict else 0
    return score
        


def main():
    scrabble_en_points = {'aeilnorstu':1, 'dg':2, 'bcmp':3, 'fhvwy':4, 'k':5, 'jx':8, 'qz':10}
    scrabble_en = {}
    for letters, score in scrabble_en_points.items():
        scrabble_en.update(dict.fromkeys(letters, score))
    
    scrabble_it_points = {'aeio':1, 'crst':2, 'lmnu':3, 'bdfpv':5, 'ghz':8, 'q':10}
    scrabble_it = {}
    for letters, score in scrabble_it_points.items():
        scrabble_it.update(dict.fromkeys(letters, score))
        
    print(scrabble_score('opera', scrabble_en))
    print(scrabble_score('opera', scrabble_it))    
        

if __name__ == '__main__':
    main()