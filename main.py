#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomNumbers():
    # randomly picks number
    lucky_num = random.randint(1,100)
    return lucky_num

def getColor():
    colors = ["red", "blue", "green", "purple", "yellow"]
    rand_color = random.randint(0, len(colors) - 1)
    return colors[rand_color]

def getRandomFortune():

    # list of possible fortunes
    fortunes = [
        "These aren't the droids you're looking for.",
        "I find your lack of faith disturbing",
        "Fear is a path to the dark side of the force.",
        "It's a trap!",
        "Stay on target!",
        "Obi-wan is your only hope.",
        "Obey your boss.  They know force choke.",
        "A little padawan is in your future.",
        "Release your anger.",
        "The force is with you...but you are not a Jedi yet.",
        "You are beaten.  It is useless to resist.",
        "You are having a bad feeling about this.",
        "I suggest a new strategy...let the Wookie win."
    ]

    # randomly select fortunes
    index = random.randint(0, len(fortunes) - 1)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        body = "<body background='http://paulbourke.net/miscellaneous/starfield/8192x4096.png'></body>"
        logo = "<center><image src='http://www.pngmart.com/files/3/Star-Wars-Logo-PNG-File.png' style='height:300; width: 600; margin-top: 50px;'></center>"
        header = "<center><h1 style='font-size:54px; color:" + getColor() + "; text-shadow: " + getColor() + " 3px 3px 5px; padding-top:50px;'>Fortune Cookie</h1></center>"

        fortune = getRandomFortune()
        fortune_sentence = "<p style='color:red; font-size:36px;'>Your fortune: <fortune style='color:yellow;'>" + fortune + "</fortune></p>"
        fortune_paragraph = "<center>" + fortune_sentence + "<p></center>"

        lucky_number = getRandomNumbers()
        number_sentence = "<p style='font-size:36px; color: red;'>Your lucky number: <lucky style='color:yellow;'>" + str(lucky_number) + "</lucky></p>"
        number_paragraph = "<center>" + number_sentence + "</center>"

        content = body + logo + header + fortune_paragraph + number_paragraph

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
