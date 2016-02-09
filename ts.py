from trueskill import Rating, quality_1vs1, rate_1vs1
import sys

pr = {}

#f = open(sys.argv[1])
for line in sys.stdin:
    line = line[:-1]
    winner = line.split('\t')[0]
    if winner not in pr:
        pr[winner] = Rating(100)
    loser = line.split('\t')[2]
    if loser not in pr:
        pr[loser] = Rating(100)
    pr[winner], pr[loser] = rate_1vs1(pr[winner], pr[loser])
    #print("Winner: " + winner + ", Loser: " + loser)
    
for p in pr:
    print(str(pr[p].mu) + "\t" + p)

    
