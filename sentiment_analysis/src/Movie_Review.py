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
        for i in output:
            # print(i[0]+"\n\n")
            analysis = TextBlob(i[0])
            if analysis.sentiment.polarity > 0.15:
                pos += 1
                #print("\n", i[0])

            if analysis.sentiment.polarity <= 0.1:
                neg += 1
                #print("\n", i[0])

            if analysis.sentiment.polarity > 0.1 and analysis.sentiment.polarity <= 0.15:
                nu += 1
                #print("\n", i[0])

        if neg < pos and pos >= nu and (pos-neg) > 4:
            print("Excellent")

        elif neg > pos and neg >= nu and (neg-pos) > 4:
            print("Poor")

        else:
            if pos == neg:
                print("Theres 50% Chance You Will Like this Movie")

            elif (pos+nu) > neg:
                print("Good")

            elif (neg+nu) > pos:
                print("Bad, But Watchable")

            else:
                print("Theres 50% Chance You Will Like this Movie")

        x = "Movie : " + str(n) + str(pos) + str(neg) + str(nu)
        print(x)
        return x
        #print(pos, neg, nu,)
        # To close the connection
        conn.close()


#x = MovieReviewAnalyzer.reviewAnalyzer('The Shawshank Redemption')
