def one_edit_away(s1,s2):

    if s1 == s2:
        return True

    elif len(s1) == len(s2):
        return check_replace(s1,s2)

    elif abs(len(s1)-len(s2)) == 1:
        if len(s1) > len(s2):
            return check_insert(s1,s2)
        else:
            return check_insert(s2,s1)

    else:
        return False

def check_replace(s1,s2):
    counter = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            counter+=1
        
        if counter > 1:
            return False

    return True

def check_insert(s1,s2):
    j=0
    for i in range(len(s1)):
        if i==len(s2)-1:
            return True

        elif s1[i] != s2[j] :
            j-=1
       
        j+=1

    if i!=j:
        print(i,j)
        return False
    else:
        return True

