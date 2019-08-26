def isValidWalk(walk):
    if len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
        return True
    return False