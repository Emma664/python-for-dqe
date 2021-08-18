from datetime import datetime, timedelta, date


class NewsFeed:
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


class Ads(NewsFeed):
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


class News(NewsFeed):
    def __init__(self, text, city: object):
        super().__init__(text)
        self.city = city

    def write_to_file(self):
        with open("volha_newsfeed.txt", "a") as f:
            f.write(f"\n{self.type_of_news}------------------------\n")
            f.write(self.text)
            f.write(f"\n{self.city} {self.publish_date}\n")


while input("Do you want to add something?\nPrint Y for yes, N for no ").upper() == "Y":
    user_choice = input("News - 1, Ads - 2, Weather - 3.\nPlease, enter your choice: ")
    user_text = input("Please, enter your text: ")
    if user_choice == "1":
        user_city = input("Please, enter your city: ")
        news_feed_item = News(user_text, user_city)
    elif user_choice == "2":
        user_expiration_time = input("Please, enter number of days for your add to last: ")
        news_feed_item = Ads(user_text, user_expiration_time)
    elif user_choice == "3":
        news_feed_item = NewsFeed(user_text, "Weather")
    news_feed_item.write_to_file()

