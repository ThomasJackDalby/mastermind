import logging
import argparse, sys
from api import API

logging.basicConfig(level=logging.DEBUG)

API_URL = "http://localhost" 

class ManualClient:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("command")
        args = parser.parse_args(sys.argv[1:2])
        command_name = args.command

        if hasattr(self, command_name):
            command = getattr(self, command_name)
            command()

    def login(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("user_name")
        args = parser.parse_args(sys.argv[2:])

        user_name = args.user_name

        api = API(API_URL, user_name)

    # def propose(self):
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument("user_name")
    #     parser.add_argument("game_type_id")
    #     args = parser.parse_args(sys.argv[2:])

    #     user_name = args.user_name
    #     game_type_id = args.game_type_id

    #     api = API(API_URL, user_name)
    #     response = api.propose(game_type_id)
    #     print(response.text)

if __name__ == "__main__":
    ManualClient()