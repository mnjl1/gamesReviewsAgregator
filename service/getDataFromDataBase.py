import json

def get_last_reviews_json(db):
    top_reviews = get_reviews_from_db(db)
    rows = list()
    for row in top_reviews:
        rows.append(row)
    first_title = rows[0]
    result = dict()
    result['title']=first_title[0]
    result['score']=first_title[3]
    result['url']=first_title[1]
    return result

def get_last_reviews_web(db):
    top_reviews = get_reviews_from_db(db)
    rows = list()
    for row in top_reviews:
        rows.append(row)
    first_title = rows[0]
    print(json.dumps(first_title))
    return rows

def get_reviews_from_db(db):
    return db.cursor().execute("SELECT title, url, img_source, score FROM reviews")
