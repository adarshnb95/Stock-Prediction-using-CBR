"""

Author: Aaditya Arigela
Description: First version of code - Creating cases from trending News articles.

"""

import csv, re, pprint, os
from datetime import datetime as dt

try:
    import cPickle as pickle
except ImportError:
    import pickle


def parse_csv(filename):
    with open(filename, "rt") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        next(reader, None)  # skip the headers
        return parse_item(reader)


def parse_cases(filename):
    with open(filename, "r") as fp:
        return parse_item([i.split(None, 1) for i in fp])


def parse_items(lines):
    items = []

    for line in lines:
        if not line:
            continue
        else:
            items.append(parse_item(line))

    return items


def parse_item(lines):

    items = []
    interval = {};

    #Case will be created with the weekly stock data
    count = 0;

    opening_price = 0;
    closing_price = 0;
    company_name = "apple";
    data_directory = "data/"

    for line in lines:

        item = {}
        try:
            if count == 0:
                if dt.strptime(line[0], '%Y-%m-%d').date().weekday() < 5:
                    opening_price = float(line[1])
                    count += 1

            elif count < 5:
                count += 1

            elif count == 5:
                closing_price = float(line[4])
                if closing_price > opening_price:
                    stock_diff = closing_price - opening_price
                    item['StockPercentageChange'] = (stock_diff / opening_price) * 100
                else:
                    stock_diff = opening_price - closing_price
                    item['StockPercentageChange'] = (stock_diff / closing_price) * 100

                d = dt.strptime(line[0], '%Y-%m-%d').date()

                scores = readSentiment(data_directory, company_name + "_" + str(d.year) + str(d.month) + str(d.day) + ".txt")

                #Length will be 2 - positive and negative sentiment score
                if scores and len(scores) > 1:
                    item["NewsPosSentiment"] = scores[0]
                    item["NewsNegSentiment"] = scores[1]

                if item['StockPercentageChange'] > 5:
                    item['StockDifference'] = stock_diff
                    items.append(item)

                    # Reset count.
                    count = 0;

        except ValueError:
            continue

    return items

'''
    Read sentiment scores from input file
'''
def readSentiment(data_directory, filename):
    if os.path.exists(data_directory + filename):
        with open(data_directory + filename, "rt") as news_sentiment:
            for line in news_sentiment:
                scores = line.split(' ');

            return scores


if __name__ == "__main__":

    import sys

    #from place import Place
    if len(sys.argv) < 2:
        print("Usage: %s <filename>." % sys.argv[0])
        sys.exit(1)
    else:
        filename = sys.argv[1]

    if filename.endswith(".csv"):
        items = parse_csv(filename)
    else:
        items = parse_cases(filename)
    print("Parsed %d items" % len(items))

    filename = "cases.pickle"
    if os.path.exists(filename):
        print("Case storage file %s exists. Not creating cases." % filename)
    else:
        print("\nCreating and storing Case objects in %s:" % filename)
        from case import Case
        cases = []
        for i,item in enumerate(items):
            cases.append(Case(item))
            if (i+1)%100 == 0:
                print("  %d cases created..." % (i+1))
        print("  Storing cases...")
        with open(filename, "wb") as fp:
            pickle.dump((item,cases), fp, -1)
            print("\n  Done.")
    '''
    except RuntimeError:
        sys.stderr.write("Fatal error occurred!")
        sys.exit(1)
    '''
