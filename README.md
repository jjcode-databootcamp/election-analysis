# Election Results Analysis

## Overview
The goal of this analysis is to determine voter turnout statstics by county and candidate results for a local congretional elections in Colorado. This was done with a python script reading data from a csv file. Each row in the csv is a vote cast by a voter and their associated voter info. Tha analysis outlines:  

- Count of total votes cast in election 
- Count of total votes cast by county
- County voting percentage representation out of total votes cast
- Count of total votes for each candidate
- Overall percentage of votes garner by each candidate 
- County with the largest voter turnout
- Winner of election 

## Election-Audit Results: 

1. Total votes were cast in this congressional election were 369,711

2. A breakdown of the number of votes and the percentage of total votes for each counties were:
- - Jefferson: 10.5% (38,855)
- - Denver: 82.8% (306,055)
- -  Arapahoe: 6.7% (24,801)

3. It appaears Denver had the largest number of registered voters 


4. A breakdown of the number of votes and the percentage of total votes for each counties were:
- - Charles Casper Stockham: 23.0% (85,213)
- - Diana DeGette: 73.8% (272,892)
- - Raymon Anthony Doane: 3.1% (11,606)


5. Diana DeGette won this election with a count of 272,892 votes receviced which accounts for 73.8% of total votes cast. 

## Election-Audit Summary:
The script used written for this analysis has a lot of business value such as:
- It is flexible and dynamic. It can be used for other elections by simply changing the csv source file if the file had the same column structure. 
- It can be modify to accommodate other voter info such as gender, age, demographics and etc.
- It is extremely fast to run.  