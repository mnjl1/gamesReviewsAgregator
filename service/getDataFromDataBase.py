import json

def get_last_reviews_json(db):
    con = db.cursor()
    top_reviews = con.execute("SELECT title, url, img_source, score FROM reviews")
    rows = list()
    for row in top_reviews:
        rows.append(row)
    return json.dumps(rows)

def get_last_reviews_web(db):
    con = db.cursor()
    top_reviews = con.execute("SELECT title, url, img_source, score FROM reviews")
    rows = list()
    for row in top_reviews:
        rows.append(row)
    return rows
