import challonge, sys
from clean_names import clean

def find_player(list, id):
    for p in list:
        if p['id'] == id:
            return p

def main():

    if len(sys.argv) < 2:
        print("\n\tUsage:\tpython load_tourney tourney1 tourney2 ...")
        return
    
    user = 'Greyhound_Smash'
    key = 'WVcRiQ7UCjMd5JxyGpzXKk7M36KNot2cALXitGSj'
    challonge.set_credentials(user, key)

    for t in sys.argv[1:]:
        p = challonge.participants.index(t)
        matches = challonge.matches.index(t)
        for m in matches:
            print(clean(find_player(p, m['winner-id'])['name']) + '\t<def>\t' +
                  clean(find_player(p, m['loser-id'])['name']))
                      
#end

main()
