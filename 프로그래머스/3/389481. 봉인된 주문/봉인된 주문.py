from collections import deque

def solution(n, bans):
    answer = ''
    alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
    NumToAlpha = {}
    AlphaToNum = {}
    for i in range(len(alphabets)):
        NumToAlpha[i+1] = alphabets[i]
        AlphaToNum[alphabets[i]] = i+1
    
    def changeToSpell(n):
        spell = ""
        while(n > 0):
            remainder = n % 26
            n = n // 26
            if remainder == 0:
                n -= 1
                remainder = 26
            spell = NumToAlpha[remainder] + spell
        
        return spell
    
    def changeToN(spell):
        n = 0
        for i in range(len(spell)):
            n += 26 ** (len(spell) - 1 - i) * AlphaToNum[spell[i]]
        return n       
    
    for i in range(len(bans)):
        bans[i] = changeToN(bans[i])
    bans.sort()
    bans = deque(bans)
    
    while True:
        if bans and n >= bans[0]:
            n += 1
            bans.popleft()
        else:
            answer = changeToSpell(n)
            break
    
    return answer