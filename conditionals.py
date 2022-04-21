res = input('First time at Best Buy?')
res = answer.lower()
if res == 'yes':
    print('35% discount. Promo code NEW-CUSTOMER')
else:
    print('15% discount on cakes. Promo code RETURNING')
# 
# 
# 
allergic = input('Have an allergy:')
allergy = input('Allergic to:')
allergic = allergic.lower()
allergy = allergy.lower()
is_allergic = allergic == 'yes' or allergic == 'have'
suggestion = allergy != 'milk' and allergy != 'gluten'
print('Allergies:', is_allergic)
print('Offer cheesecakes:', suggestion)
# 
# 
# 
age = int(input('Enter your age:'))
if age < 18:
   print("You're a minor")
else:
   print("You're not a minor anymore")
print('Have Fun!')
# 
# 
# 
 
wish = input('What do you want?')
if wish == 'money':
    print('Here is 1 million dollars')
if wish == 'happiness':
    print('Sorry, no happiness here')
if wish != 'money'  and wish != 'happiness':
    print('get a life')
# 
# 
# 
weight = int(input('Enter weight in KG:'))
taste = input('Enter food:')
if weight <= 150:
   price = 3000
else:
   price = 5000
if taste == 'fruit':
   price = price + 1000
else:
   price =  price + 500
print('Approximate cake price:', price)