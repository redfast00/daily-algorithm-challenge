import random
from utils.words import words, words_set


def recover_sentence(word_dictionary, sentence):
    '''Given a dictinary of words and a sentence, recovers a possible list of words.'''
    if isinstance(word_dictionary, set):
        return recursive_recoverer(word_dictionary, sentence)
    else:
        return recursive_recoverer(set(word_dictionary), sentence)


def recursive_recoverer(words, sentence):
    if sentence in words:
        return [sentence]
    else:
        for i in range(1, len(words)):
            if sentence[:i] in words:
                rest = recursive_recoverer(words, sentence[i:])
                if rest is not None:
                    return [sentence[:i]] + rest
    return None


def is_valid_solution(sentence, words_set, solution):
    return ''.join(solution) == sentence and all((word in words_set) for word in solution)


def pick_random_sentence(words):
    result = []
    for _ in range(random.randint(1, 100)):
        result.append(random.choice(words))
    return ''.join(result)


if __name__ == "__main__":
    for i in range(20):
        sentence = pick_random_sentence(words)
        print(sentence)
        solution = recover_sentence(words_set, sentence)
        assert is_valid_solution(sentence, words_set, solution)
