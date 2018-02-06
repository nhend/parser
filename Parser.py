def find_prefix(word):
    prefixes_file = open('prefixes.txt')
    
    if (len(word) <= 1):
        print('too short')
        return
    
    global prefixes 
    prefixes = []
    global likely_prefix 
    likely_prefix = ''
    
    for line in prefixes_file:
        if word.startswith(line.strip()):
            prefixes.append(line.strip() + '-')
            
            if (len(line.strip()) >= len(likely_prefix)):
                likely_prefix = line.strip() + '-'
    
    #if no prefix was found, move on to suffixes and return
    if likely_prefix == '': 
        find_suffix(word)
        return
    
    print('Most likely prefix: ' + likely_prefix)
    
    #if more than one prefix was found, print all 
    if (len(prefixes) > 1):
        print('Potential prefixes: ' + str(prefixes))
    
    #remove previously found prefix from original word
    word = word[len(likely_prefix)-1:]
    
    find_prefix(word)
    
def find_suffix(word):
    suffixes_file = open('suffixes.txt')
    
    if (len(word) <= 1):
        find_root(word)
        print('too short suffix')
        return
    
    global suffixes
    suffixes = []
    global likely_suffix 
    likely_suffix = ''
    
    for line in suffixes_file:
        if word.endswith(line.strip()):
            suffixes.append('-' + line.strip())
            
            if (len(line.strip()) >= len(likely_suffix)):
                likely_suffix = '-' + line.strip()
    
    #if no suffix was found, return
    if likely_suffix == '':
        find_root(word)
        return
    
    print('Most likely suffix: ' + likely_suffix)
    
    #if more than one suffix was found, print all 
    if (len(suffixes) > 1):
        print('Potential suffixes: ' + str(suffixes))
    
    #remove previously found suffix from original word
    word = word[:-len(likely_suffix)+1]
    find_suffix(word)
        
def find_root(word):
    roots_file = open('roots.txt')
     
    if (len(word) <= 1):
        return
     
    global roots
    roots = []
    global likely_root
    likely_root = ''
     
    for line in roots_file:
        if line.strip() in word:
            roots.append(line.strip())
             
            if (len(line.strip()) >= len(likely_root)):
                likely_root = line.strip()
     
    #if no root was found, return
    if likely_root == '': 
        return 
     
    #print all roots
    roots.reverse()
    print('Most likely roots: ' + str(roots))
     
    #remove previously found root from original word and check again
    word = word[len(likely_root)+1:]
    find_root(word)
    
#def glue():
 
while True:
    word = input('Please enter your word: ')
    if word == 'STOP':
        break
    find_prefix(word)

