import pymysql
from textblob import TextBlob


class MovieReviewAnalyzer():
    def reviewAnalyzer(name):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="",
            db='python_miniproject',
        )
        movieID = {'Joker': 1, 'The Shawshank Redemption': 2, 'The Dark Knight': 3, 'Avengers Endgame': 4, 'Avengers Infinity War': 5,
                   'Tenet': 6, 'Parasite': 7, 'Inception': 8, 'The Lord of the Rings: The Return of the King': 9, 'Spider-Man: Far from Home': 10}
        n = movieID[name]
        cur = conn.cursor()
        cur.execute("select review from reviews where movieID = {}".format(n))
        output = cur.fetchall()
        pos = 0
        neg = 0
        nu = 0
        x = [{},""]
        for i in output:
            analysis = TextBlob(i[0])
            if analysis.sentiment.polarity > 0.15:
                pos += 1

            if analysis.sentiment.polarity <= 0.1:
                neg += 1

            if analysis.sentiment.polarity > 0.1 and analysis.sentiment.polarity <= 0.15:
                nu += 1

        if neg < pos and pos >= nu and (pos-neg) > 4:
            print("Excellent")
            x[1] = "Excellent"
        elif neg > pos and neg >= nu and (neg-pos) > 4:
            print("Poor")
            x[1] = "Poor"

        else:
            if pos == neg:
                print("Theres 50% Chance You Will Like this Movie")
                x[1] = "Theres 50% Chance You Will Like this Movie"

            elif (pos+nu) > neg:
                print("Good")
                x[1] = "Good"

            elif (neg+nu) > pos:
                print("Bad, But Watchable")
                x[1] = "Bad, But Watchable"

            else:
                print("Theres 50% Chance You Will Like this Movie")
                x[1] = "Theres 50% Chance You Will Like this Movie"

        x[0] = {"Positive Reviews":pos,
                "Negative Reviews":neg,
                "Neutral Reviews":nu
               }
        print(x)
        return x

        # To close the connection
        conn.close()
