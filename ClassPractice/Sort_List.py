def are_anagrams(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    if word1_sorted == word2_sorted:
        return True
    else:
        return False


if __name__ == '__main__':
    are_anagrams('kevin gatyes', 'Love is a mystery')
