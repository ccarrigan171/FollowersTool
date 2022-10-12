from http import client
import random
from sre_constants import SUCCESS
from instagrapi import Client

print("LOGIN:") #get login info (not stored externally)
username = input("type username then press enter: ")
password = input("type password then press enter: ")
client = Client() #store client object
client.login(username, password) #input login info
print("GOOD LOGIN")
myID = client.user_id #store personal ID
following = client.user_following(myID) #store following
print("FOLLOWING STORED")
followers = client.user_followers(myID) #store followers
print("FOLLOWERS STORED")

def unfollowers(): #returns list of unfollowers
    missingFollowers = set(following).difference(followers) #get unfollowers (by user_id)
    print("number of unfollowers: " + str(len(missingFollowers))) 
    unfollowers = [] #initialize unfollowers list (will contain names)
    for user_id in missingFollowers: #iterate each userID in unfollowers
        x = client.username_from_user_id(int(user_id)) #get username from userID
        unfollowers.append(x) #add username to unfollowers list
    print("missing followers: ", unfollowers)
    return unfollowers

def unfollowAction():
    while True: 
        unfollow = input("Do you want to unfollow any of these users? (y/n)") 
        if unfollow == "y":
            for name in unfollowers:
                unfollowUser = input("Unfollow: " + name + " ?? (y/n)")
                if unfollowUser == "y":
                    unfollowID = client.user_id_from_username(name)
                    client.user_unfollow(unfollowID)
                    print("action successful")
                elif unfollowUser == "n":
                    continue
                else:
                    print("Enter (y/n)!!")
        elif unfollow == "n":
            print("finished")
            return
        else:
            print("Enter (y/n)!!")


unfollowers()
unfollowAction()


