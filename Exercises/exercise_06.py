"""
exercise_06  Scraping and Saving

In this class you will write a class that scrapes and saves URLs. If the item to be scraped has been saved, it will
be opened from the save and returned without making a new web request.

This class will be named "Scrape_Saver" and has 3 definitions:

 1) an __init__ function that accepts a base_url to scrape and a save_location, both are strings
    * The base URL should be of the format "http://www.uniprot.org/uniprot/{}.fasta" where each item to be scraped
       will replace the {} in the base url ( this is done with base_url.format(item) )
    * The save location is the folder path where the text scraped will be saved

 2) a "retrieve" function that accepts a single argument, the name to be scraped. EX: 'P69892'
    * The retrieve definition should first check if the item to be scraped has already been scraped and saved
       to the save_location.
    * If it exists, then this function should read the file and return the contents without
       making a new web requests.
    * If the save does not exist, then the url should be scraped and saved as a string in a plain text file.

 3) a __str__ function that returns a list of files in the save_location


"""
import os
import urllib.request as ur

class Scrape_Saver:

    def __init__(self, base_url, save_location):
        self.base_url = base_url
        self.save_location = save_location
        return

    def retrieve(self, item):
        if item in os.listdir(self.save_location):
            with open(self.save_location + item,'r') as infile:
                return infile.read()
        else:
            string = ur.urlopen(self.base_url.format(item)).read().decode()
            with open(self.save_location+item,'w') as outfile:
                outfile.write(string)
        return string

    def __str__(self):
        return os.listdir(self.save_location)


if __name__ == '__main__':
    """
    Here is where the Scrape_Saver class is tested.
    """

    url = "http://www.uniprot.org/uniprot/{}.fasta"
    item = 'P69892'

    x = Scrape_Saver(url, 'saves/')
    print(x.retrieve(item))