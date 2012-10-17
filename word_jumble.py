import enchant, sys, re

def permutations(inputstr):
    result = []
    for i in range(len(inputstr)):
        result.append(inputstr[i])        
        for s in permutations(inputstr[:i] + inputstr[i+1:]):
            result.append(inputstr[i] + s)
    return result

def word_jumble(inputstr):
    if re.match("^[A-Za-z]*$", inputstr):        
        perm = permutations(inputstr)
        final_result = []
        d = enchant.Dict('en_US')
        for i in perm:
            if d.check(i):
                if i not in final_result:   #if you want to remove a single letters, add 'and len(i) != 1:'
                    final_result.append(i)
        print 'Jumbled words are as follows:'
        for i in final_result:
            print i            
    else:
        print 'Pass a valid string'

if __name__ == "__main__":
    word_jumble(str(sys.argv[1]))
            