#!/usr/bin/env python3
import sys

#make a dictionary of my favorite things
my_favs_dict = {'book' : "Ender's game", 
'song' : "Charlie Puth - Hero", 'color' : 'pale mauve'}

#add a new key and variable to my dictionary
my_favs_dict['organism'] = 'dog'

#Get the fav_thing from the command line and a new value for that key. 
fav_thing = sys.argv[1]
new_fav_thing = sys.argv[2]
my_favs_dict[fav_thing] = new_fav_thing
print(f'My new favorite {fav_thing} is {my_favs_dict[fav_thing]}')
print(my_favs_dict)

