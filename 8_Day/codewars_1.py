"link : https://www.codewars.com/kata/555086d53eac039a2a000083/train/python"
# Opposites Attract

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0:
        if flower2 % 2 == 0:
            return False
        else:
            return True
    else:
        if flower2 % 2 == 0:
            return True
        else:
            return False
        

# other solutions
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2


def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2


def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 == 1