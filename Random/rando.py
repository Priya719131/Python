import random
value= random.random()# between 0 and 1
print(value)

v1 = random.uniform(1,10)#between 1 and 10
print(v1)

v2= random.randint(1,6)#give random number between 1 and 6 and not float
print(v2)

Greeting = ['Hello','Hi','Hey','Howdy']
v3= random.choice(Greeting)#choose one from the list
print(v3)

colors = ['Red','Black','Green']
result= random.choices(colors,weights=[18,18,2],k=10)#choose 10 colors from the list with weights
print(result)

deck = list(range(1,53))
random.shuffle(deck)
print(deck)

hand = random.sample(deck,k=5)#chose unique 5 cards from the deck each time
print(hand)