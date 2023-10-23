# import requests
from bs4 import BeautifulSoup4

def get_url(position,location):
    template = "https://www.indeed.ca/jobs?q={}&l={}"
    url = template.format(position.replace(' ', '+'), location.replace(' ', '+'))
    print (url)
    return url


def main():
    position = 'Software Engineer Intern'
    location = 'Vancouver, BC'
    get_url(position, location)