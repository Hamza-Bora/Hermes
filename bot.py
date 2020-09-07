#!/usr/bin/python
# -*- coding: utf-8 -*-

from instabot import Bot
import sys

timer = sys.argv[1]
bot = Bot()
bot.login(username = "yourusername", password = "yourpassword")

bot.upload_photo("/home/user/Hermes/resim"+str(timer)+".png", caption = "Katiliminiz icin tesekkur ederiz. Hamza'nin selami var..")

                    # directory of the file        |                        | Description of the photo to upload  |
