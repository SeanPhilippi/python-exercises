def find_anagrams(word, candidates):
    count = len(candidates)
    i = 0
    while i < count:
        candidate = candidates[i]
        if word.lower() == candidate.lower():
            candidates.remove(candidate)
            count -= 1
        else:
            i += 1 

    anagrams = []
    word_hash = {}
    for ch in word.lower():
        if ch in word_hash:
            word_hash[ch] += 1
        else:
            word_hash[ch] = 1

    for candidate in candidates:
        candidate_hash = {}
        for ch in candidate.lower():
            if ch in candidate_hash:
                candidate_hash[ch] += 1
            else:
                candidate_hash[ch] = 1
        if candidate_hash == word_hash:
            anagrams.append(candidate)
    return anagrams
