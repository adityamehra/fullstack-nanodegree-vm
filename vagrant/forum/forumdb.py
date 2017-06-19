# "Database code" for the DB Forum.

import psycopg2, bleach

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  cur = db.cursor()
  cur.execute("select content, time from posts order by time desc")
  posts = cur.fetchall()
  db.close()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  cur = db.cursor()
  cur.execute("insert into posts values (%s)", (bleach.clean(content),))
  db.commit()
  db.close()
