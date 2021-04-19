from textblob import TextBlob

line = """There's some very clever humour in this film, which is both a parody of and a tribute to actors. However, after a while it just seems an exercise in style (notwithstanding great gags such as Balasko continuing the part of Dussolier, and very good acting by all involved) and I 
was wondering why Blier made this film. All is revealed in the ending, when Blier, directing Claude Brasseur, gets a phone call from his dad (Bernard Blier) - from heaven, and gets the chance to say how much he misses him. An effective emotional capper and obviously heartfelt. 
But there isnt really sufficient dramatic tension or emotional involvement to keep the rest of the film interesting throughout its entire running time. Some really nice scenes and sequences, however, and anyone who likes these mosntres sacrés of the French cinema should get a fair amount of enjoyment out of this film."""
analysis = TextBlob(line)


if analysis.sentiment.polarity > 0.3:
    print("Positive")

elif analysis.sentiment.polarity <= 0:
    print("Negative")
else:
    print("Neutral")
