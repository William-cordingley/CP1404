import wikipedia


def summary():
    print("What Page would you like to summarize: ")
    page = input(">>> ")
    while page != "":
        print("Title: " + wikipedia.page(page).title)
        print("Summary: " + wikipedia.summary(str(page)))
        print("URL: " + wikipedia.page(page).url)
        print("What Page would you like to summarize: ")
        page = input(">>> ")
    print("Thank You")


summary()
