#Week 1: Rule Based Chatbot

#Overview

A simple rule based chatbot built in Python. It takes user input, matches it against a set of predefined responses, and replies accordingly. If no match is found, it returns a default fallback message.

How it works


Takes continuous input from the user in a loop.
Normalizes input by converting to lowercase and stripping whitespace.
Looks up the input in a dictionary of predefined question and response pairs.
Returns a default "I dont Understand" message if no match is found.
Exits the loop when the user types "exit".
