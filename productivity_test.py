from collections import Counter
import  string
import time
import itertools
alphabeth=string.printable
lorem="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
myfile=file = open('enlt.txt', 'r').read()
text=myfile

def execution_time2(prog, times, *args):
    start_time = time.time()
    for _ in itertools.repeat(None, times):
        prog(*args)
    print("'{}' exec time, {} loops: {} seconds".format(prog.__name__ , times, time.time()-start_time) )
'''
def one(text):
    return Counter(text)
def two(text):
    freq={key: 0 for key in alphabeth}
    for c in text:
        freq[c]+=1
    return Counter(freq)
def three(text):
    freq={key: 0 for key in alphabeth}
    for c in alphabeth:
        freq[c] = text.count(c)
    return Counter(freq)
alphabeth={c for c in text}
print("Singles Equal: {}".format(one(text) == two(text) == three(text)))
for prog in [one,two,three,]:
    execution_time2(prog,1000,text*10)




def create_alphabeths1(text):
    alphabeth={c for c in text}
    doubles_alphabeth={text[i]+text[i+1] for i in range(len(text)-1)}
    triples_alphabeth={text[i]+text[i+1]+text[i+2] for i in range(len(text)-2)}
    quad_alphabeth={text[i]+text[i+1]+text[i+2]+text[i+3] for i in range(len(text)-3)}
def create_alphabeths2(text):
    alphabeth=set()
    doubles_alphabeth=set()
    triples_alphabeth=set()
    quad_alphabeth=set()
    for i in range(len(text)-3):
        alphabeth.add(text[i])
        doubles_alphabeth.add(text[i]+text[i+1])
        quad_alphabeth.add(text[i]+text[i+1]+text[i+2]+text[i+3])
print()
for prog in [create_alphabeths1,create_alphabeths2]:
    execution_time2(prog,text)





def doubles_three(text):
    doubles_permutations=list(itertools.permutations(alphabeth,2))
    freq={first+second: 0 for first,second in doubles_permutations}
    for double in freq.keys():
        freq[double] = text.count(double)
    return Counter(freq)
def doubles_three_with_alphabeth(text):
    freq={key: 0 for key in doubles_alphabeth}
    for double in freq.keys():
        freq[double] = text.count(double)
    return Counter(freq)
def doubles_one(text):
    return Counter({cc:text.count(cc) for cc in doubles_alphabeth})
def doubles_two(text):
    freq={key: 0 for key in doubles_alphabeth}
    for i in range(len(text)-1):
        freq[text[i]+text[i+1]]+=1
    return Counter(freq)
print()
doubles_alphabeth={text[i]+text[i+1] for i in range(len(text)-1)}
print("Doubles Equal: {}".format(doubles_two(text) == doubles_one(text) == doubles_three_with_alphabeth(text)))
for prog in [doubles_three,doubles_three_with_alphabeth,doubles_one,doubles_two]:
    execution_time2(prog,1000,text)
print()

'''

def combined1(text):
    alphabeth={c for c in text}
    doubles_alphabeth={text[i:i+2] for i in range(len(text)-1)}
    triples_alphabeth={text[i:i+3] for i in range(len(text)-2)}
    singlesfreq=Counter(text)
    doublefreq=Counter({cc:text.count(cc) for cc in doubles_alphabeth})
    triplefreq=Counter({ccc:text.count(ccc) for ccc in triples_alphabeth})
#print(singlesfreq,doublefreq)
def combined2(text):
    singlesfreq=Counter()
    doublefreq=Counter()
    triplefreq=Counter()
    quadfreq=Counter()
    quintfreq=Counter()
    quintfreq=Counter()
    sextfreq=Counter()
    septfreq=Counter()
    for i in range(len(text)-6):
        c7=text[i:i+7]
        c6=c7[:-1]
        c5=c6[:-1]
        cccc=c5[:-1]
        ccc=cccc[:-1]
        cc=ccc[:-1]
        c=cc[:-1]
        singlesfreq[c] = singlesfreq.get(c, 0) + 1
        doublefreq[cc] = doublefreq.get(cc, 0) + 1
        triplefreq[ccc] = triplefreq.get(ccc, 0) + 1
        quadfreq[cccc] = quadfreq.get(cccc, 0) + 1
        quintfreq[c5] = quintfreq.get(c5, 0) + 1
        sextfreq[c6] = sextfreq.get(c6, 0) + 1
        septfreq[c7] = sextfreq.get(c7, 0) + 1
        singlesfreq=Counter({**{c:0 for c in alphabeth}, **dict(singlesfreq)})
    print(singlesfreq, "\n"); print(doublefreq.most_common(50), "\n"); print(triplefreq.most_common(50), "\n"); print(quadfreq.most_common(50), "\n");print(quintfreq.most_common(50), "\n");print(sextfreq.most_common(50), "\n");#print(septfreq.most_common(50), "\n")

for prog in [combined1,combined2]:
    execution_time2(prog,1,text)
