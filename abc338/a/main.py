S = input()
if len(S) == 1:
    capitalized = S.isupper()
else:
    capitalized = S[0].isupper() and S[1:].islower()

if capitalized:
    print('Yes')
else:
    print('No')