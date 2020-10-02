import argparse
import logging

import pandas as pd

from article import Article
from database import Base, Session, engine


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    filename = args.filename

    articles = pd.read_csv(filename, delimiter=';')

    Base.metadata.create_all(engine)
    postgress_session = Session()

    # uid;body;title;url;newspaper_uid;host;n_token_title;n_token_body
    for index, row in articles.iterrows():
        article = Article(
            row['uid'],
            row['body'],
            row['host'],
            row['title'],
            row['newspaper_uid'],
            row['n_token_body'],
            row['n_token_title'],
            row['url']
        )
        postgress_session.add(article)

    postgress_session.commit()
    postgress_session.close()


main()
