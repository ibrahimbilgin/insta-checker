import requests
import os
from bs4 import BeautifulSoup


class Instagram:
    def __init__(self, username):
        self.username = str(username)

    def get_request(self):
        """
        Returns page contents
        :return str:
        """
        request = requests.get('https://www.instagram.com/' + self.username)
        if request.status_code == 200:
            return request.content
        else:
            raise Exception(" This username is not used: {}".format(self.username))

    def content_parser(self):
        """
        Returns parsed page contents
        :return str:
        """
        content = self.get_request()
        source = BeautifulSoup(content, 'html.parser')
        return source

    def get_info(self):
        """
        Returns instagram infos
        :return dict:
        """
        source = self.content_parser()
        description = source.find("meta", {"property": "og:description"}).get("content")
        info_list = description.split("-")[0]
        followers = info_list[0:info_list.index("Followers")]
        info_list = info_list.replace(followers + "Followers, ", "")
        following = info_list[0:info_list.index("Following")]
        info_list = info_list.replace(following + "Following, ", "")
        posts = info_list[0:info_list.index("Posts")]
        results = {"followers": followers, "following": following, "posts": posts}
        return results

    def print_info(self):
        """
        Prints all informations
        """
        info = self.get_info()
        print("")
        print(" User Name: {}".format(self.username))
        print(" Followers: {}".format(info["followers"]))
        print(" Following: {}".format(info["following"]))
        print(" Posts: {}".format(info["posts"]))
        print("")
        print(" -" * 15)


class Helper:
    @staticmethod
    def read_file(filename):
        """
        Returns account lists
        :param filename:
        :return list:
        """
        accounts = [line.rstrip('\n') for line in open(filename, encoding="utf8")]
        return accounts

    @staticmethod
    def retry():
        """
        Decides wanna try again
        :return boolean:
        """
        q = input(" Press E to repeat operation or press H to exit the program: ")
        if q.upper() == "E":
            os.system("cls||clear")
            return True
        else:
            return False


if __name__ == "__main__":
    while True:
        accounts = Helper.read_file("accounts.txt")
        for account in accounts:
            info = Instagram(account)
            try:
                info.print_info()
            except Exception as e:
                print(e)

        retry = Helper.retry()
        if not retry:
            break
