#!/bin/usr/env/python3

import wikipedia


def wiki_search(keyword):
    try:
        search_results = wikipedia.search(keyword)
        return search_results
    except:
        print("[Error]")
        main()


def wiki_summary(article_choice):
    summary = wikipedia.summary(article_choice)
    return summary


def write_file(summary, article_name):
    outfile = article_name + ".txt"

    try:
       f = open(outfile, 'w')
       f.write(summary)
       print("Article written to file successfully")
       print("Find your file in the application's root directory")
    except:
          print("[Error], Cannot write to file. \n")
          print("Your article is shown below:")
          print(summary)
    finally:
           f.close()


def main():
    search_word = input("Enter a word to search for an article: ")
    search_result = wiki_search(search_word)
    print("Search results:")
    print(search_result)

    article_choice = input("\n Enter your choice for article: ")
    try:
        content = wiki_summary(article_choice)
    except:
          print("Article not found")
          main()
    finally:
           write_file(content, article_choice)
           exit(0)


try:
    main()
finally:
    exit(0)
