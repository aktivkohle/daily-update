import config
from emailResult import sendresult
import pandas as pd 
import datetime
import sys

def scrape_send():

    started = datetime.datetime.now()

    print ("\n", "Using Python Version: \n",sys.version, '\n')
    print ('Started', str(started), '\n')

    q = pd.read_html(config.TARGET_WEBSITE)
    q3 = q[2]

    SearchFor = config.SEARCH_TERMS
    searchfor = [e.lower() for e in SearchFor]

    # return rows which include terms from relevant columns
    relevantRecords = q3[q3[config.COLUMN_HEADING_1].str.lower(
    	).str.contains('|'.join(searchfor), na=False) | q3[config.COLUMN_HEADING_2].str.lower(
    	).str.contains('|'.join(searchfor), na=False)]

    asText = relevantRecords.to_csv(sep=' ', index=False, header=False, line_terminator='\n\n') 
    howmany = '\n' + str(len(relevantRecords)) + ' matching results found today :' + '\n\n'
    print (howmany + asText)

    finished = datetime.datetime.now()

    sendresult(howmany + asText)

    print ('Finished', str(finished), '\n')
