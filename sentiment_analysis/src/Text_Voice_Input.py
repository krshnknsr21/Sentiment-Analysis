from textblob import TextBlob


class Analyzer():
    def testAnalyze(self, input):
        analysis = TextBlob(input)

        if analysis.sentiment.polarity > 0.15:
            # print("Positive")
            return "Postive"

        elif analysis.sentiment.polarity <= 0.1:
            # print("Negative")
            return "Negative"

        else:
            # print("Neutral")
            return "Neutral"


p = Analyzer.testAnalyze('Good Morning')
print(p)
