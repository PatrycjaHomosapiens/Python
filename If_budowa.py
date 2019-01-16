# taki zapis spowoduje wyprintowanie "tekst1", "tekst2", "tekst3", bo każdy if jest prawdą
if (True):
    print("tekst1")
if (True):
    print("tekst2")
if (True):
    print("tekst3")

    
# taki zapis spowoduje wyprintowanie tylko "tekst1", bo to jest prawdą i nie będzie już prawdzał dalej elif i else
if (True):
    print("tekst1")
elif (True):
    print("tekst2")
elif (True):
    print("tekst3")
