# Election Analysis and Audit
---
## Overview of Project

### Purpose
Python is a programming language and tool that can be used to help Seth and Tom analyze and audit returns from a congressional election in Colorado. In this module, the goal was to identify the winner of the election as well as provide a vote count by county. To help with the analysis, the code editor Visual Studio Code was employed. Similarly, as was the case when working with VBA code, the use of conditionals and iterations (loops) made it possible to quickly sort through thousands of lines of data to determine and visualize the results.

## Results

### Election Results
The results from the election were as follows:

+ Total Votes Cast: 	369,711  

COUNTY | VOTES | PERCENT 
---|---:|---:
Denver | 306,055 | 82.8%
Jefferson | 38,855 | 10.5%
Arapahoe | 24,801 |	6.7%
TOTAL |	369,711  

+ County with most votes: Denver  

CANDIDATE | VOTES | PERCENT
---|---:|---:
Diana DeGette | 272,892 |	73.8%
Charles Casper Stockham | 85,213	| 23.0%
Raymon Anthony Doane | 11,606	| 3.1%
TOTAL | 369,711  

+ Winning Candidate: Diana DeGette  

### Python Coding Methodology
Data was uploaded using an Excel-generated CSV file where data was organized into three columns: Ballot ID, County and Candidate. After the data was integrated into the code editor for Python, total votes were determined by iterating over the entire set of rows and counting the number of Ballot IDs (as each ID should be unique and thus yield total number of votes). County and candidate votes were tallied using the same loop and dictionaries were created to index the results. Within the dictionary the name of the county (or candidate) represent the key and the votes tallied their corresponding value. 

An additional loop was run for each dictionary to access the results. The code logic is as follows:

1.	A loop is initiated to search for candidate or county name within its respective dictionary.

[![2nd-loop-iteration.png](https://i.postimg.cc/vH7L7Y3C/2nd-loop-iteration.png)](https://postimg.cc/ykdZsHqT)

2.	A new variable is created that will hold the vote count. The syntax to accomplish this is represented as: NEW_VARIABLE = VOTE_DICTIONARY[COUNTY]. This will pull the dictionary, look for the key (COUNTY), return the number of tallied votes (VALUE) and store them in the NEW_VARIABLE.

[![new-variable-vote-count.png](https://i.postimg.cc/MTyvkTMS/new-variable-vote-count.png)](https://postimg.cc/7GZx0qns)

The NEW_VARIABLE holding the votes for each (or candidate) is then used in determining the vote count. By using an if-statement in the current loop, a comparison can be done to determine which county (or candidate) had the greatest number of votes cast. The code is as follows:

1.	If NEW_VARIABLE (now holding vote count for COUNTY A) > LARGEST_COUNT (variable set to 0). In this case, the first county (COUNTY A) to test this conditional will always be greater than 0 so the statement will always be “true.”

3.	LARGEST_COUNT = NEW_VARIABLE.
Here we are changing the value of LARGEST_COUNT to be equal to the number of the votes for the first county (COUNTY A). It is important to remember that this if-statement is a part of a loop that is iterating through a dictionary of only three values. 

For example, if we had counted only the first 100 votes instead of all the votes, assume the total was:  
  
> COUNTY A: 25  
> COUNTY B: 20  
> COUNTY C: 55  

When COUNTY A runs first through the condition it is compared to LARGEST_COUNT (previously set to 0) thus LARGEST_COUNT becomes equal to 25 (25 > 0). When COUNTY B is run next through the if-statement it is less than 25 (20 < 25) so LARGEST_COUNT remains at 25. However, when COUNTY C runs its total number of votes through, because its vote total is greater than 25, LARGEST_COUNT becomes 55 (55 > 25). 

Finally, because the NEW_VARIABLE is indexed to its key in the dictionary, once the highest vote total is identified, it is then possible to also recognize the county (or candidate) with the most votes. The code for the if-statement is as follows:

[![If-statement.png](https://i.postimg.cc/fRJyz5t5/If-statement.png)](https://postimg.cc/jDYtvHhJ)

Ultimately the county with the most votes recorded is Denver with 306,055 votes.

### Summary
