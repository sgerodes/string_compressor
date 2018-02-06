#Challenge: String compression
#https://www.sololearn.com/Discuss/1009655/challenge-compression
#https://www.sololearn.com/Discuss/1017933/string-challenge/

# The efficiency is 25-35%. With zlib the efficiency is even 57-62%!
# If you do not want to use zlib just set "use_zlib=False"
from math import floor
from itertools import permutations
import string
use_zlib=False
if use_zlib:
    import zlib

alphabeth=string.printable

replacing=[]
replacer=[]
replacer2=list(permutations([chr(x) for x in range(17,27)],2))

common_map={}
special_map={}

def create_tailormade_ngrams(text):
    frequency={}
    for c in alphabeth:
        frequency[c]=0
    bigram={}
    trigram={}
    quadgram={}
    for i in range(len(text)-3):
        
        freq=text[i]
        if freq in frequency.keys():
            frequency[freq]+=1
        else:
            frequency[freq]=1
        
        bi=freq+text[i+1]
        if bi in bigram.keys():
            bigram[bi]+=1
        else:
            bigram[bi]=1
        
        tri=bi+text[i+2]
        if tri in trigram.keys():
            trigram[tri]+=1
        else:
            trigram[tri]=1
        
        quad=tri+text[i+3]
        if quad in quadgram.keys():
            quadgram[quad]+=1
        else:
            quadgram[quad]=1

gap_bigrams={}
    for i in range(len(text)-3):
        gbi=text[i]+ "_" +text[i+2]
        if gbi in gap_bigrams.keys():
            continue
        for i in range(len(text)-3):
            if text[i] == gbi[0] and text[i+2] == gbi[2]:
                if gbi in gap_bigrams.keys():
                    gap_bigrams[gbi]+=1
                else:
                    gap_bigrams[gbi]=1

print([" '"+x[0]+"' :"+str(x[1]) for x in sorted(gap_bigrams.items(), key = lambda x:x[1], reverse = True)])

for key, value in bigram.items():
    bigram[key]=value*1
    for key, value in trigram.items():
        trigram[key]=value*2
for key, value in quadgram.items():
    quadgram[key]=value*3
    
    ngram={}
    ngram.update(quadgram)
    ngram.update(trigram)
    ngram.update(bigram)
    
    replacer=[x[0] for x in sorted(frequency.items(), key = lambda x:x[1], reverse = False) [:floor(len(frequency)/1.78)] ]
    ngram = [x[0] for x in sorted(ngram.items(), key = lambda x:x[1], reverse = True) [:len(replacer)] ]
    
    return (replacer,ngram)

def compress(text):
    
    replacer,replacing=create_tailormade_ngrams(text)
    if len(replacing) > len(replacer):
        print("Need more replacers. Replacers=" + str(len(replacer)) + " replacing=" + str(len(replacing)))
        return
    
    compressed=text
    for seq in replacing:
        repl=replacer.pop()
        common_map[seq]=repl
        special=replacer2.pop()
        special_map[repl]=special[0]+special[1]
    
    skeys=special_map.keys()
    for key in skeys:
        compressed=compressed.replace(key, special_map[key])
    keys=common_map.keys()
    for key in keys:
        compressed=compressed.replace(key, common_map[key])
    
    #additional zlib compression :)
    if use_zlib:
        compressed=zlib.compress(compressed.encode())
    
    return compressed

def decompress(text):
    decompressed=text
    if use_zlib:
        decompressed=zlib.decompress(decompressed).decode()
    
    inverted_special_map = dict([[v,k] for k,v in special_map.items()])
    inverted_common_map = dict([[v,k] for k,v in common_map.items()])
    
    skeys=inverted_special_map.keys()
    keys=inverted_common_map.keys()
    for key in keys:
        decompressed=decompressed.replace(key, inverted_common_map[key])
    for key in skeys:
        decompressed=decompressed.replace(key, inverted_special_map[key])
    return decompressed

eng_text="Seoul (CNN)North and South Korean athletes will march together at the Winter Olympics opening ceremony under a unified flag, the South said Wednesday, in a diplomatic breakthrough following days of talks between the two countries.The nations have also agreed to form a joint North and South Korean women's ice hockey team for the Games in Pyeongchang, which begin early next month, South Korea's unification ministry said.The unification ministry announced a range of joint activities between the countries for the Games, following talks Wednesday at the demilitarized zone (DMZ).North and South Korean skiers will train together at a resort in North Korea before the Olympics start, and performers from the two countries will also hold a joint cultural event there.North Korea will also send around 230 supporters to cheer on its athletes. A smaller delegation of North Korean athletes and supporters will attend the Paralympics, the ministry said.South Korean supporters wave unified flags at the World Student Games in August 2003 in Daegu, South Korea.South Korean supporters wave unified flags at the World Student Games in August 2003 in Daegu, South Korea.The Korean Unification Flag features a blue silhouette of the peninsula and outlying islands. The two countries have marched under the flag before, in rare shows of unity, first at the 1991 World Table Tennis Championships, and at a number of sporting events since. It was most recently used at the 2006 Winter Games in Turin, Italy.The International Olympics Committee (IOC) would need to approve the countries' agreements, and those that affect competition, such as the joint hockey team, could be more complicated than the ceremonial proposals.The committee said Wednesday it had received a number of interesting proposals that it would discuss with delegates from both countries in Switzerland on Saturday.We are sure that the two Korean delegations will present their ideas and proposals at the meeting on Saturday in Lausanne. This will then enable the IOC to carefully evaluate the consequences and the potential impact on the Olympic Games and the Olympic competitions, it said in a statement."

eng_text2="Technology has certainly changed. Here's where you would typically see a comparison saying that if you punched the 743 billion words one to a card and stacked them up, then assuming 100 cards per inch, the stack would be 100,000 miles high; nearly halfway to the moon. But that's silly, because the stack would topple over long before then. If I had 743 billion cards, what I would do is stack them up in a big building, like, say, the Vehicle Assembly Building (VAB) at Kennedy Space Center, which has a capacity of 3.6 million cubic meters. The cards work out to only 2.9 million cubic meters; easy peasy; room to spare. And an IBM model 84 card sorter could blast through these at a rate of 2000 cards per minute, which means it would only take 700 years per pass (but you'd need multiple passes to get the whole job done).I culled a corpus of 20,000 words from a variety of sources, e.g., newspapers, magazines, books, etc. For each source selected, a starting place was chosen at random. In proceeding forward from this point, all three, four, five, six, and seven-letter words were recorded until a total of 200 words had been selected. This procedure was duplicated 100 times, each time with a different source, thus yielding a grand total of 20,000 words. This sample broke down as follows: three-letter words, 6,807 tokens, 187 types; four-letter words, 5,456 tokens, 641 types; five-letter words, 3,422 tokens, 856 types; six-letter words, 2,264 tokens, 868 types; seven-letter words, 2,051 tokens, 924 types. I then proceeded to construct tables that showed the frequency counts for three, four, five, six, and seven-letter words, but most importantly, broken down by word length and letter position, which had never been done before to my knowledge.Certain letters are more common in written English than others, for example I is used far more often than W. By analyzing a large piece of known text we can find which letters are used most often. These sequences will vary depending on the text analyzed, but typical sequences areJust as letters have expected frequencies in language, so do groups of letters; tables of frequencies of digraphs (pairs of letters) and trigraphs (sets of three letters) exist to assist the cryptoanalyst. The thirty most common digraphs in the English language are, in order of occurrence:"

lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ac arcu ac tellus faucibus ultricies. Duis vestibulum erat ac elit tempor, id facilisis leo consectetur. Nunc consectetur vestibulum aliquet. Sed vitae volutpat eros. Nulla lorem lectus, rutrum id dignissim in, rutrum id nisi. Vestibulum erat ante, egestas id velit et, facilisis facilisis nulla. Phasellus vel vestibulum turpis. Phasellus quis pulvinar nunc, quis scelerisque urna. Cras feugiat sem id est dignissim, elementum suscipit eros pharetra. Maecenas pharetra mi et pharetra fringilla. Donec egestas condimentum enim eget condimentum. Duis interdum, elit sit amet placerat ultrices, lectus mauris mattis purus, vitae finibus nisl lorem sed orci. Etiam et eros at arcu sagittis euismod ut eget purus.Donec et dui sed metus egestas semper eu in mi. Aenean nec diam laoreet, consequat massa pharetra, tincidunt tortor. Pellentesque ut molestie magna. Aenean et metus scelerisque, imperdiet elit eget, consectetur metus. Pellentesque diam mauris, cursus eget fermentum eget, dapibus condimentum dui. Proin in lacus ante. Donec non hendrerit erat, eget tincidunt sapien. Etiam egestas orci eu arcu imperdiet, convallis luctus dolor cursus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus quis lorem nec ante malesuada viverra. Aliquam in tortor vitae dolor ultrices tincidunt. Nam eu nisl est. Integer ornare feugiat ante et mattis. Nulla facilisi.Nam fringilla odio eu viverra lacinia. In ornare nisi eu porttitor fermentum. Proin eget turpis feugiat, molestie metus eget, accumsan metus. Nunc facilisis sem orci, et varius ipsum lacinia eu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sodales risus id velit rutrum, nec fringilla erat ullamcorper. Maecenas enim risus, condimentum vel nulla eu, aliquet lobortis justo. Morbi efficitur nunc ipsum, posuere aliquet risus ullamcorper quis.Etiam non erat interdum, accumsan orci vitae, gravida eros. Cras tristique dui vitae nisl varius gravida. Duis pharetra aliquet metus nec hendrerit. Etiam vitae enim nec magna ullamcorper facilisis. Sed bibendum quis diam sit amet congue. Cras facilisis, orci ac egestas fermentum, leo orci venenatis odio, ac lacinia diam urna et lacus. Phasellus gravida leo elit, sit amet convallis quam fringilla non. Fusce consectetur dolor est, at aliquam felis condimentum vel. Nulla vitae condimentum neque. Vivamus tristique turpis nunc, nec pretium dui dictum a. Praesent lorem sem, posuere vel tellus eget, suscipit tincidunt magna. Etiam egestas vitae tellus quis ullamcorper. Nam pretium, tellus pretium lobortis finibus, arcu est dignissim enim, tincidunt pellentesque orci diam non ante. Nullam at dignissim libero.Vivamus mi enim, tristique eu arcu quis, mollis luctus purus. Morbi eget libero ac mi egestas dapibus. Phasellus scelerisque sapien nec lorem tincidunt facilisis. Etiam ultricies viverra posuere. Nulla pharetra auctor rutrum. Sed mattis velit ac rutrum posuere. Phasellus a nibh ornare, malesuada est a, congue lectus. Phasellus tincidunt imperdiet augue a ullamcorper. Mauris accumsan felis leo, ac posuere leo cursus ac. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque facilisis sodales venenatis."

some_text="Sorting strings in alphabetical order is very common, however using sorted might not sort the keys/values of our dict in the proper alphabetical order, i.e. ignoring the case. To ignore the case we can again utilize the key argument and the str.lower (or str.upper) method so that all strings are the same case when comparing them:This contains only string keys and values, so there'd be no way to put the months in the correct order without additional context. To do so we can simply create another dictionary to map the strings to their numerical values and use that dictionary's __getitem__ method to compare the values in our month dictionary:Likewise we could list the odd class sizes first, and perform many other algorithms to get our sort exactly how we want. There are many other intricate sorting methods and tricks you could use with dictionaries (or any iterable object), but for now hopefully these examples have provided a good starting point."

from random import choice
random_string=''.join(choice(string.ascii_lowercase + string.digits) for _ in range(100000))


#feel free to choose your text

text=lorem_text#+some_text+eng_text+eng_text2+random_string
#text=random_string
compressed=compress(text)
print("Text         length= " + str(len(text)))
print("Compressed   length= " + str(len(compressed)))
print("Efficiency         = " + str((1-len(compressed)/len(text))*100))
decompressed=decompress(compressed)
print("Decompressed length= " + str(len(decompressed)))

