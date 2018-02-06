import string
from collections import OrderedDict

alphabeth=string.printable

def analyse(text):
    frequency={}
    for c in alphabeth:
        frequency[c]=0
    bigram={}
    trigram={}
    quadgram={}
    quintgram={}

    gap_bigram={}
    gap_trigram={}
    gap_quadgram={}

    dgap_bigram={}
    for i in range(len(text)-4):
        t1,t2,t3,t4,t5=text[i],text[i+1],text[i+2],text[i+3],text[i+4]
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

        quint=quad+text[i+4]
        if quint in quintgram.keys():
            quintgram[quint]+=1
        else:
            quintgram[quint]=1
     
        gbi=t1+'_'+t3
        if gbi in gap_bigram.keys():
            gap_bigram[gbi]+=1
        else:
            gap_bigram[gbi]=1

        dgbi=t1+'__'+t4
        if dgbi in dgap_bigram.keys():
            dgap_bigram[dgbi]+=1
        else:
            dgap_bigram[dgbi]=1

        for gtri in [t1+'_'+t3+t4, t1+t2+'_'+t4]:
            if gtri in gap_trigram.keys():
                gap_trigram[gtri]+=1
            else:
                gap_trigram[gtri]=1

        for gquad in [t1+'_'+t3+t4+t5, t1+t2+'_'+t4+t5, t1+t2+t3+'_'+t5]:
            if gquad in gap_quadgram.keys():
                gap_quadgram[gquad]+=1
            else:
                gap_quadgram[gquad]=1

    for key, value in trigram.items():
        trigram[key]=value*2
    for key, value in quadgram.items():
        quadgram[key]=value*3
    for key, value in quintgram.items():
        quintgram[key]=value*4


    for key, value in gap_trigram.items():
        gap_trigram[key]=value*2
    for key, value in gap_quadgram.items():
        gap_quadgram[key]=value*3
    
    ngram={}
    ngram.update(quintgram)
    ngram.update(quadgram)
    ngram.update(trigram)
    ngram.update(bigram)

    ngram.update(gap_quadgram)
    ngram.update(gap_trigram)
    ngram.update(gap_bigram)

    bigram.update(gap_bigram)
    bigram.update(dgap_bigram)
    
    print( sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    print( sorted(bigram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )
#   print( sorted(trigram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )
#   print( sorted(quadgram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )
#   print( sorted(quintgram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )
    
#   print( sorted(gap_bigram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )
#   print( sorted(gap_trigram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )
#print( sorted(gap_quadgram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )
#    print()
    #print( sorted(ngram.items(), key=lambda x: x[1], reverse=True)[:len(frequency)] )

eng_text="Seoul (CNN)North and South Korean athletes will march together at the Winter Olympics opening ceremony under a unified flag, the South said Wednesday, in a diplomatic breakthrough following days of talks between the two countries.The nations have also agreed to form a joint North and South Korean women's ice hockey team for the Games in Pyeongchang, which begin early next month, South Korea's unification ministry said.The unification ministry announced a range of joint activities between the countries for the Games, following talks Wednesday at the demilitarized zone (DMZ).North and South Korean skiers will train together at a resort in North Korea before the Olympics start, and performers from the two countries will also hold a joint cultural event there.North Korea will also send around 230 supporters to cheer on its athletes. A smaller delegation of North Korean athletes and supporters will attend the Paralympics, the ministry said.South Korean supporters wave unified flags at the World Student Games in August 2003 in Daegu, South Korea.South Korean supporters wave unified flags at the World Student Games in August 2003 in Daegu, South Korea.The Korean Unification Flag features a blue silhouette of the peninsula and outlying islands. The two countries have marched under the flag before, in rare shows of unity, first at the 1991 World Table Tennis Championships, and at a number of sporting events since. It was most recently used at the 2006 Winter Games in Turin, Italy.The International Olympics Committee (IOC) would need to approve the countries' agreements, and those that affect competition, such as the joint hockey team, could be more complicated than the ceremonial proposals.The committee said Wednesday it had received a number of interesting proposals that it would discuss with delegates from both countries in Switzerland on Saturday.We are sure that the two Korean delegations will present their ideas and proposals at the meeting on Saturday in Lausanne. This will then enable the IOC to carefully evaluate the consequences and the potential impact on the Olympic Games and the Olympic competitions, it said in a statement."

lorem_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ac arcu ac tellus faucibus ultricies. Duis vestibulum erat ac elit tempor, id facilisis leo consectetur. Nunc consectetur vestibulum aliquet. Sed vitae volutpat eros. Nulla lorem lectus, rutrum id dignissim in, rutrum id nisi. Vestibulum erat ante, egestas id velit et, facilisis facilisis nulla. Phasellus vel vestibulum turpis. Phasellus quis pulvinar nunc, quis scelerisque urna. Cras feugiat sem id est dignissim, elementum suscipit eros pharetra. Maecenas pharetra mi et pharetra fringilla. Donec egestas condimentum enim eget condimentum. Duis interdum, elit sit amet placerat ultrices, lectus mauris mattis purus, vitae finibus nisl lorem sed orci. Etiam et eros at arcu sagittis euismod ut eget purus.Donec et dui sed metus egestas semper eu in mi. Aenean nec diam laoreet, consequat massa pharetra, tincidunt tortor. Pellentesque ut molestie magna. Aenean et metus scelerisque, imperdiet elit eget, consectetur metus. Pellentesque diam mauris, cursus eget fermentum eget, dapibus condimentum dui. Proin in lacus ante. Donec non hendrerit erat, eget tincidunt sapien. Etiam egestas orci eu arcu imperdiet, convallis luctus dolor cursus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus quis lorem nec ante malesuada viverra. Aliquam in tortor vitae dolor ultrices tincidunt. Nam eu nisl est. Integer ornare feugiat ante et mattis. Nulla facilisi.Nam fringilla odio eu viverra lacinia. In ornare nisi eu porttitor fermentum. Proin eget turpis feugiat, molestie metus eget, accumsan metus. Nunc facilisis sem orci, et varius ipsum lacinia eu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sodales risus id velit rutrum, nec fringilla erat ullamcorper. Maecenas enim risus, condimentum vel nulla eu, aliquet lobortis justo. Morbi efficitur nunc ipsum, posuere aliquet risus ullamcorper quis.Etiam non erat interdum, accumsan orci vitae, gravida eros. Cras tristique dui vitae nisl varius gravida. Duis pharetra aliquet metus nec hendrerit. Etiam vitae enim nec magna ullamcorper facilisis. Sed bibendum quis diam sit amet congue. Cras facilisis, orci ac egestas fermentum, leo orci venenatis odio, ac lacinia diam urna et lacus. Phasellus gravida leo elit, sit amet convallis quam fringilla non. Fusce consectetur dolor est, at aliquam felis condimentum vel. Nulla vitae condimentum neque. Vivamus tristique turpis nunc, nec pretium dui dictum a. Praesent lorem sem, posuere vel tellus eget, suscipit tincidunt magna. Etiam egestas vitae tellus quis ullamcorper. Nam pretium, tellus pretium lobortis finibus, arcu est dignissim enim, tincidunt pellentesque orci diam non ante. Nullam at dignissim libero.Vivamus mi enim, tristique eu arcu quis, mollis luctus purus. Morbi eget libero ac mi egestas dapibus. Phasellus scelerisque sapien nec lorem tincidunt facilisis. Etiam ultricies viverra posuere. Nulla pharetra auctor rutrum. Sed mattis velit ac rutrum posuere. Phasellus a nibh ornare, malesuada est a, congue lectus. Phasellus tincidunt imperdiet augue a ullamcorper. Mauris accumsan felis leo, ac posuere leo cursus ac. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque facilisis sodales venenatis."

analyse(lorem_text+eng_text)
