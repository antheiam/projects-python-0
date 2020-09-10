#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down, pass it around, 98 bottles of beer on the wall... ♪

#No more bottles of beer on the wall, no more bottles of beer.
#Go to the store and buy some more, 99 bottles of beer on the wall...

#Create a program that prints out every line to the song "99 bottles of beer on the wall."
#Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
#Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#Remember, when you reach 1 bottle left, the word "bottles" becomes singular.


bottles=99
bottles_init=99

while bottles>1:

    print(str(bottles) + " bottles of beer on the wall, "+str(bottles)+" bottles of beer.")
    print("Take one down, pass it around, "+str(bottles-1) + " bottles of beer on the wall...")

    bottles=bottles-1

if(bottles==1):
        print(str(bottles) + " bottle of beer on the wall, "+str(bottles)+" bottle of beer.")
        print("Take one down, pass it around, "+str(bottles-1) + " bottle of beer on the wall...")
        bottles=bottles-1

if bottles==0:
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, "+str(bottles_init)+" bottles of beer on the wall...")