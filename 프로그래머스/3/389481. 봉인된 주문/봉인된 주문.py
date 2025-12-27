def solution(n, bans):
    alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
    alphabet_to_num_dict = dict()
    num_to_alphabet_dict = dict()
    for idx,alpha in enumerate(alphabets):
        alphabet_to_num_dict[alpha] = idx+1
        num_to_alphabet_dict[idx] = alpha
    
    def spellToNum(spell):
        num = 0
        for i in range(len(spell)):
            num += alphabet_to_num_dict[spell[i]]  * 26 ** (len(spell) - i - 1)
        return num
    
    def numToSpell(num):
        spell = ""
        remain_list = []
        while(num > 0):
            num -= 1
            remain = num % 26
            remain_list.append(remain)
            num //= 26
        for remain in reversed(remain_list):
            spell += num_to_alphabet_dict[remain]
        
        return spell

    for ban in sorted(bans, key=lambda x : [len(x),x]):
        if spellToNum(ban) <= n:
            n += 1
            
    return numToSpell(n)