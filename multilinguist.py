import requests
import json
import random

class Multilinguist:
  """This class represents a world traveller who knows
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'

    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    return json_response['translationText']



class MathGenius(Multilinguist):

    def __init__(self):
        pass

    def report_total(self, list = []):
        total_sum = sum(list)
        return "The total is {}".format(total_sum)


class QuoteCollector(Multilinguist):


    def __init__(self, list_of_quotes):
        self.list_of_quotes = []

    def add_quote(self, quote):
        self.list_of_quotes.append(quote)
        return self.list_of_quotes

    def pick_random_quote(self):
        random_number = random.randint(0, len(self.list_of_quotes) - 1)
        random_quote = self.list_of_quotes[random_number]
        return random_quote



quoter1 = QuoteCollector([])
quoter1.add_quote("Mind over matter")
quoter1.add_quote("Life is like a box of chocolates")
quoter1.add_quote("When life gives you lemons, make lemonade")
print(quoter1.list_of_quotes)
print(quoter1.pick_random_quote())
quoter1.travel_to("France")
msg = quoter1.pick_random_quote()
print(quoter1.say_in_local_language(msg))

# me = MathGenius()
# print(me.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
# me.travel_to("India")
# msg = me.report_total([6,3,6,68,455,4,467,57,4,534])
# print(me.say_in_local_language(msg)) # है को कुल 1604
# me.travel_to("Italy")
# msg = me.report_total([324,245,6,343647,686545])
# print(me.say_in_local_language(msg))  # È Il totale 1030767
