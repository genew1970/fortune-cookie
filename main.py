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
        "You are having a bad feeling about a choice.",
        "I suggest a new strategy...let the Wookie win."
    ]

    # randomly select fortunes
    index = random.randint(0, len(fortunes) - 1)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<center><h1 style='font-size:54px; color:red; padding-top:350px;'>Star Wars Fortune Cookie</h1></center>"

        fortune = getRandomFortune()
        fortune_sentence = "Your forune: " + fortune
        fortune_paragraph = "<center><p style='font-size:36px;'>" + fortune_sentence + "<p></center>"

        lucky_number = getRandomNumbers()
        number_sentence = "Your lucky number: " + str(lucky_number)
        number_paragraph = "<center><p style='font-size:36px;'>" + number_sentence + "<p></center>"

        content = header + fortune_paragraph + number_paragraph

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
