import json
import os
from datetime import datetime, timedelta, date
from functions_4 import normalize_case


class Feed:
    def __init__(self, text, type_of_news='News'):
        self.publish_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type_of_news = type_of_news
        self.text = text

    def write_to_file(self):
        with open("volha_newsfeed.txt", "a") as f:
            f.write(f"\n\n{self.type_of_news}" + ('-' * (30 - len(self.type_of_news))) + '\n')
            f.write(self.text)
            f.write(f"\n{self.publish_date}\n")
            f.write('-' * 30 + '\n')


class Ads(Feed):
    def __init__(self, text, days_to_last):
        super().__init__(text)
        self.days_to_last = int(days_to_last)
        self.type_of_news = "Ads"

    def calculate_expiration_date(self):
        expiration_date = date.today() + timedelta(days=self.days_to_last)
        return expiration_date

    def calculate_days_left(self):
        return (self.calculate_expiration_date() - date.today()).days

    def write_to_file(self):
        with open("volha_newsfeed.txt", "a") as f:
            f.write(f"\n{self.type_of_news}------------------------\n")
            f.write(self.text)
            f.write(f"\nActual till: {self.calculate_expiration_date()}. {self.calculate_days_left()} days left.\n")


class News(Feed):
    def __init__(self, text, city: str):
        super().__init__(text)
        self.city = city

    def write_to_file(self):
        with open("volha_newsfeed.txt", "a") as f:
            f.write(f"\n{self.type_of_news}------------------------\n")
            f.write(self.text)
            f.write(f"\n{self.city} {self.publish_date}\n")


class AutoFeed:
    def __init__(self, number_of_records=1,
                 path=r"C:\Users\Volha_Bykhautsova\PycharmProjects\python-for-dqe\feed.txt"):
        self.number_of_records = number_of_records
        self.path = path

    def read_file(self):
        with open(self.path, 'r') as file:
            lines = [line.rstrip() for line in file]
        lines_capitalized = []
        for item in lines:
            new_item = normalize_case(item)
            lines_capitalized.append(new_item)

        if len(lines) > 0:
            os.remove(self.path)

        return lines_capitalized

    def write_to_feed(self):
        lines_capitalized = self.read_file()
        for i in range(int(self.number_of_records)):
            if lines_capitalized[0] == "1":
                user_city = (lines_capitalized[2])
                user_text = lines_capitalized[1]
                news_feed_item = News(user_text, user_city)
                lines_capitalized = lines_capitalized[3:]
            elif lines_capitalized[0] == "2":
                user_expiration_time = (lines_capitalized[2])
                user_text = lines_capitalized[1]
                news_feed_item = Ads(user_text, user_expiration_time)
                lines_capitalized = lines_capitalized[3:]
            elif lines_capitalized[0] == "3":
                user_text = lines_capitalized[1]
                news_feed_item = Feed(user_text, "Weather")
                lines_capitalized = lines_capitalized[2:]
            news_feed_item.write_to_file()


class JsonAutoFeed:
    def __init__(self, number_of_records=1,
                 path=r"C:\Users\Volha_Bykhautsova\PycharmProjects\python-for-dqe\feed.json"):
        self.number_of_records = number_of_records
        self.path = path

    def read_file(self):
        with open(self.path) as json_file:
            fields = json.load(json_file)

        if fields["type"] == "Ads":
            return Ads(fields["text"], fields["days_to_last"])
        if fields["type"] == "News":
            return News(fields["text"], fields["city"])
        return Feed(fields["text"])

    def write_to_feed(self):
        self.read_file().write_to_file()


while input("Do you want to add something?\nPrint Y for yes, N for no ").upper() == "Y":
    user_input = input("Add feed manually - 1, add feed from txt - 2, add feed from json - 3. \nPlease, enter your choice: ")
    if  user_input == "1":
        user_choice = input("News - 1, Ads - 2, Weather - 3.\nPlease, enter your choice: ")
        user_text = input("Please, enter your text: ")
        if user_choice == "1":
            user_city = input("Please, enter your city: ")
            news_feed_item = News(user_text, user_city)
        elif user_choice == "2":
            user_expiration_time = input("Please, enter number of days for your add to last: ")
            news_feed_item = Ads(user_text, user_expiration_time)
        elif user_choice == "3":
            news_feed_item = Feed(user_text, "Weather")
        news_feed_item.write_to_file()
    elif user_input == "3":
        JsonAutoFeed().write_to_feed()
    else:
        number_of_records = input("Please, enter number of records. Hit enter to skip. ")
        path = input("Please, provide path to your file. Hit enter to skip. ")
        if number_of_records == '' and path == '':
            user_file = AutoFeed()
        elif number_of_records == '' and path != '':
            user_file = AutoFeed(path=path)
        elif number_of_records != '' and path == '':
            user_file = AutoFeed(int(number_of_records))
        else:
            user_file = AutoFeed(int(number_of_records), path)
        user_file.write_to_feed()
