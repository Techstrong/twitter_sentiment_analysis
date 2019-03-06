import Twitter

#Welcome Screen
print("Twitter Analytics App")

#Take in User Inputs
selection = input("Type#1 to analyze the most used words",
                  "Type#2 to analyze twitter sentiment",
                  "Type#3 to analyze twitter stream"
                  )

if selection == 1:
    print("proceed to analyze most used words")
    u = input("Search Account: ")
    num = int(input("How many tweets? "))
if selection == 2:
    print("proceed to analyze twitter sentiment")

if selection == 3:
    print("Proceed to analyze twitter stream")
    hash_tag = input("Please enter the hashtag")




Twitter.user_tweets(u, num)
Twitter.polarity()#Not quite sure what to do here.
Twitter.stream_tweets(hash_tag)
