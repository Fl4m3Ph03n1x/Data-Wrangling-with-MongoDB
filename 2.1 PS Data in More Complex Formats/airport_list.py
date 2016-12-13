#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports' function so that it returns a list of airport
codes, excluding any combinations like "All".
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    
    with open(page, "r") as html:
        soup = BeautifulSoup(html, 'html.parser')
        airportList = soup.find(id="AirportList").find_all("option")
        
        for airport in airportList:
            data.append(airport["value"])
    
    #remove [u'All', u'AllMajors', u'AllOthers'] from the list
    del data[0]
    del data[0]
    del data[13]
    
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    test()