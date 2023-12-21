def permutations(sentence):
    if len(sentence) == 1:
        return [sentence]
    
    perms = []
    for i in range(len(sentence)):
        fixed_char = sentence[i]
        remaining_chars = sentence[:i] + sentence[i + 1 :]
        for perm in permutations(remaining_chars):
            perms.append(fixed_char + perm)
    
    return list(set(perms))
