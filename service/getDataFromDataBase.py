import json

def get_last_reviews_json(db):
    con = db.cursor()
    top_reviews = con.execute("SELECT title, url, img_source, score FROM reviews")
    rows = list()
    for row in top_reviews:
        rows.append(row)
    first_title = rows[0]
    print(json.dumps(first_title))
    return json.dumps(first_title)

def get_last_reviews_web(db):
    con = db.cursor()
    top_reviews = con.execute("SELECT title, url, img_source, score FROM reviews")
    rows = list()
    for row in top_reviews:
        rows.append(row)
    first_title = rows[0]
    print(json.dumps(first_title))
    return rows
