#!/usr/bin/python
import psycopg2
import sys

import queries, questions
import pprint


def display_log_analysis(query):
    conn_string = "host='localhost' dbname='news' user='postgres' password='secret'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    articles = cursor.fetchall()
    conn.close()
    return articles


def solve(question, query, suffix='views'):
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

    cursor = conn.cursor()

    # execute our Query
    cursor.execute(queries.query_1)

    # retrieve the records from the database
    records = cursor.fetchall()

    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    pprint.pprint(records)

    solve(questions.question_1, queries.query_1)
    solve(questions.question_2, queries.query_2)
    solve(questions.question_3, queries.query_3)


if __name__ == "__main__":
    main()
