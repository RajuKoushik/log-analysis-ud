#!/usr/bin/python
import psycopg2

import queries
import questions


def display_log_analysis(query):
    """
    :param query: The individual query
    :return: returns the result after the query is executed
    """
    # Define our connection string
    conn_string = "host='localhost' dbname='news' user='postgres' password='secret'"

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()

    # execute our Query
    cursor.execute(query)
    articles = cursor.fetchall()
    conn.close()
    return articles


def solve(question, query, suffix='views'):
    """
    This function is to printout the individual question and the result of it's query sequentially.
    :param question: The question parameter to get the question printed
    :param query: The quesry parameter to get the individual query
    :param suffix:
    """
    query = query.replace('\n', ' ')
    result = display_log_analysis(query)
    print question
    for i in range(len(result)):
        print '\t', i + 1, '.', result[i][0], '--', result[i][1], suffix
    print ''


def main():
    # Define our connection string
    conn_string = "host='localhost' dbname='news' user='postgres' password='secret'"

    # print the connection string we will use to connect
    print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"

    solve(questions.question_1, queries.query_1)
    solve(questions.question_2, queries.query_2)
    solve(questions.question_3, queries.query_3)

    # closing the connection

    conn.close()


if __name__ == "__main__":
    main()
