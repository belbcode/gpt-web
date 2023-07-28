import random, string
def makeid(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))