import sys
sys.setrecursionlimit(10**6)
S = input()

def dp(s, pos):
    if len(s) == pos:
        return True

    if s[pos:(pos + 5)] == 'dream':
        if dp(s, pos + 5):
            return True
        if s[(pos + 5):(pos + 7)] == 'er':
            if dp(s, pos + 7):
                return True

    if s[pos:(pos + 5)] == 'erase':
        if dp(s, pos + 5):
            return True
        if s[(pos + 5):(pos + 6)] == 'r':
            if dp(s, pos + 6):
                return True
    return False

if dp(S, 0):
    print('YES')
else:
    print('NO')
