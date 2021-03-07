# return a list of rearranged words
def find_anagrams(word, candidates):
    # remove word from candidates
    count = len(candidates)
    print('count', count)
    i = 0
    while i < count:
        print('i', i)
        print('candidates', candidates)
        candidate = candidates[i]
        if word.lower() == candidate.lower():
            print('candidate', candidate)
            candidates.remove(candidate)
            count -= 1
        else:
            i += 1 
        
        
        
          
    # for candidate in candidates:
    #    print('word.lower()', word.lower())
    #    print('candidate.lower()', candidate.lower())
    #    if word.lower() == candidate.lower():
    #        print('candidate', candidate)
    #        candidates.remove(candidate)
            
    print('candidates', candidates)
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
        print('candidate_hash', candidate_hash)
        print('word_hash', word_hash)
        if candidate_hash == word_hash:
            anagrams.append(candidate)
    return anagrams

find_anagrams('BANANA', candidates = ["BANANA", "Banana", "banana"])
