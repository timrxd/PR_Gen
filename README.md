# PR_Gen
Scrapes tournament data from Challonge.com and produces a power ranking based on the MS Trueskill algorithm.

##### Usage
Create text file with list of tournaments using end of the Challonge url (ie. http://challonge.com/gg1115 >> gg1115)<br>
File should look like:
```
gg915  
gg1015  
gg1115  
gg1215_singles
```  
Then run ./gen_pr.sh <filename>, and the PR will be printed to stdout.  Redirect how you like.

######Currently broken, need to add module for pychallonge to repo
