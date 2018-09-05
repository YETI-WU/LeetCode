# 458. Poor Pig 
"""
There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. 
They all look the same. If a pig drinks that poison it will die within 15 minutes. 
What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
Answer this question, and write an algorithm for the follow-up general case.
Follow-up:
If there are n buckets and a pig drinking poison will die within m minutes, 
how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.
"""
"""
Use Character A B C D .... to label Pig, O label NONE
Use Number 0 1 2 3 4 ..... to label order of try.

1 Pig  ->  1 char
15min(1)	
O	A	
0	1								2 total
30min(2)
O	A	A
0	1	2							3 total
45min(3)
O	A	A	A
0	1	2	3						4 total
60min(4)
O	A	A	A	A
0	1	2	3	4					5 total	( #try + 1 )^1

2 Pig  ->  2 char
15min(1)			
OO	AO	OB	AB		
00	10	01	11						4 total	
30min(2)
OO	AO	OB	AB	OB	AO	AB	AB	AB		
00	10	01	11	02	20	12	21	22	9 total	( #try + 1 )^2

3 Pig  ->  3 char
15min(1)
OOO	AOO	OBO	OOC	ABO	AOC	OBC	ABC
000	100	010	001	110	101	011	111		8 total	( #try + 1 )^3

Conclusion >>>>>  ( #try + 1 )^#Pig
"""

def poorPigs(self, buckets, minutesToDie, minutesToTest):
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

