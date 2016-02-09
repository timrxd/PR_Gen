import challonge

def find_player(list, id):
    for p in list:
        if p['id'] == id:
            return p
                               
def main():

    user = 'Greyhound_Smash'
    key = 'WVcRiQ7UCjMd5JxyGpzXKk7M36KNot2cALXitGSj'
    mid = 'gg1115'
    
    challonge.set_credentials(user, key)
    
    tournament = challonge.tournaments.show(mid)

    # Represented as dicts
    print(tournament["id"]) # 3272
    print(tournament["name"]) # My Awesome Tournament
    print(tournament["started-at"]) # None

    # Retrieve the participants for a given tournament.
    p = challonge.participants.index(tournament["id"])
    print(len(p)) 

    # Get matches
    matches = challonge.matches.index(tournament['id'])

    for m in matches:
        print(find_player(p, m['winner-id'])['name'] + ' <def.> ' +
              find_player(p, m['loser-id'])['name'])

    print("\nend")

# end main

main()
