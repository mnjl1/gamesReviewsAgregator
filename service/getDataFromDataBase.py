def get_last_reviews():
    con = db.cursor()
    top_reviews = con.execute("SELECT title, url, img_source, score FROM reviews")
    rows = list()
    for row in top_reviews:
        rows.append(row)
    return rows
