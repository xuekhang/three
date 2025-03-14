from django.db import migrations

def insert_data(apps, schema_editor):
    # Get the model you want to insert data into
    GlobalCategory = apps.get_model('game', 'GlobalCategory')
    
    categories = [
        GlobalCategory(name=' A boy’s name'),
        GlobalCategory(name=' A river'),
        GlobalCategory(name=' An animal'),
        GlobalCategory(name=' Things that are cold'),
        GlobalCategory(name=' Insects'),
        GlobalCategory(name=' Television shows'),
        GlobalCategory(name=' Things that grow'),
        GlobalCategory(name=' Things that are black'),
        GlobalCategory(name=' School subjects'),
        GlobalCategory(name=' Movie titles'),
        GlobalCategory(name=' Musical Instruments'),
        GlobalCategory(name=' Authors'),
        GlobalCategory(name=' Bodies of water'),
        GlobalCategory(name='Countries'),
        GlobalCategory(name=' Cartoon characters'),
        GlobalCategory(name=' Holidays'),
        GlobalCategory(name=' Things that are square'),
        GlobalCategory(name=' Clothing'),
        GlobalCategory(name=' Games'),
        GlobalCategory(name='Athletes'),
        GlobalCategory(name=' School supplies'),
        GlobalCategory(name=' Things that are hot'),
        GlobalCategory(name=' Heroes'),
        GlobalCategory(name=' A girl’s name'),
        GlobalCategory(name=' Fears'),
        GlobalCategory(name=' Colors'),
        GlobalCategory(name=' A fish'),
        GlobalCategory(name=' Fruits'),
        GlobalCategory(name=' Provinces or States'),
        GlobalCategory(name=' Sports equipment'),
        GlobalCategory(name=' Tools'),
        GlobalCategory(name=' Breakfast foods'),
        GlobalCategory(name=' Flowers'),
        GlobalCategory(name=' Ice cream flavors'),
        GlobalCategory(name=' Toys'),
        GlobalCategory(name=' US Cities'),
        GlobalCategory(name=' Things in the kitchen'),
        GlobalCategory(name='Things in the ocean'),
        GlobalCategory(name=' Hobbies'),
        GlobalCategory(name=' Parts of the body'),
        GlobalCategory(name=' Sandwiches'),
        GlobalCategory(name=' Items in a catalog'),
        GlobalCategory(name=' World leaders/Politicians'),
        GlobalCategory(name=' Excuses for being late'),
        GlobalCategory(name=' Things that jump/bounce'),
        GlobalCategory(name=' Television stars'),
        GlobalCategory(name=' Things in a park'),
        GlobalCategory(name=' Foriegn cities'),
        GlobalCategory(name=' Stones/Gems'),
        GlobalCategory(name=' Things in the sky'),
        GlobalCategory(name=' Pizza toppings'),
        GlobalCategory(name=' Colleges/Universities'),
        GlobalCategory(name=' Things that have spots'),
        GlobalCategory(name=' Historical Figures'),
        GlobalCategory(name=' Items in your room'),
        GlobalCategory(name=' Fictional characters'),
        GlobalCategory(name=' Menu items'),
        GlobalCategory(name='Magazines'),
        GlobalCategory(name='A capital city'),
        GlobalCategory(name='Types of candy'),
        GlobalCategory(name=' Footware'),
        GlobalCategory(name=' Something you keep hidden'),
        GlobalCategory(name=' Items in a suitcase'),
        GlobalCategory(name=' Things with tails'),
        GlobalCategory(name=' Crimes'),
        GlobalCategory(name=' Things that are sticky'),
        GlobalCategory(name=' Awards/ceremonies'),
        GlobalCategory(name=' Cars'),
        GlobalCategory(name=' Spices/Herbs'),
        GlobalCategory(name=' Bad habits'),
        GlobalCategory(name=' Cosmetics/Toiletries'),
        GlobalCategory(name=' Celebrities'),
        GlobalCategory(name=' Cooking utensils'),
        GlobalCategory(name=' Reptiles/Amphibians'),
        GlobalCategory(name=' Parks'),
        GlobalCategory(name=' Leisure activities'),
        GlobalCategory(name=' Things you’re allergic to'),
        GlobalCategory(name=' Restaurants'),
        GlobalCategory(name=' Things in a medicine cabinet'),
        GlobalCategory(name=' Household chores'),
        GlobalCategory(name=' Halloween costumes'),
        GlobalCategory(name=' Weapons'),
        GlobalCategory(name=' Things that are round'),
        GlobalCategory(name=' Words associated with exercise'),
        GlobalCategory(name=' Sports'),
        GlobalCategory(name=' Song titles'),
        GlobalCategory(name=' Things you shout'),
        GlobalCategory(name=' Birds'),
        GlobalCategory(name=' Ways to get from here to there'),
        GlobalCategory(name=' Villains'),
        GlobalCategory(name=' Things you replace'),
        GlobalCategory(name=' Famous duos and trios'),
        GlobalCategory(name=' Things found in a desk'),
        GlobalCategory(name=' Vacation spots'),
        GlobalCategory(name=' Diseases'),
        GlobalCategory(name=' Words associated with money'),
        GlobalCategory(name=' Items in a vending machine'),
        GlobalCategory(name=' Things you wear'),
        GlobalCategory(name=' Things at a circus'),
        GlobalCategory(name=' Vegetables'),
        GlobalCategory(name=' Things you throw away'),
        GlobalCategory(name=' Occupations'),
        GlobalCategory(name=' Appliances'),
        GlobalCategory(name=' Types of drinks'),
        GlobalCategory(name=' Musical groups'),
        GlobalCategory(name=' Things at a football game'),
        GlobalCategory(name=' Personality traits'),
        GlobalCategory(name=' Video games'),
        GlobalCategory(name=' Electronic gadgets'),
        GlobalCategory(name=' Board games'),
        GlobalCategory(name=' Things that use a remote'),
        GlobalCategory(name=' Card games'),
        GlobalCategory(name=' Internet lingo'),
        GlobalCategory(name=' Offensive words'),
        GlobalCategory(name=' Wireless things'),
        GlobalCategory(name=' Computer parts'),
        GlobalCategory(name=' Websites'),
        GlobalCategory(name=' Game terms'),
        GlobalCategory(name=' Things in a grocery store'),
        GlobalCategory(name=' Reasons to quit your job'),
        GlobalCategory(name=' Things that have stripes'),
        GlobalCategory(name=' Tourist attractions'),
        GlobalCategory(name=' Things found in a hospital'),
        GlobalCategory(name=' Food/Drink that is green'),
        GlobalCategory(name=' Weekend Activities'),
        GlobalCategory(name=' Acronyms'),
        GlobalCategory(name=' Seafood'),
        GlobalCategory(name=' Christmas songs'),
        GlobalCategory(name=' Words ending in “-n”'),
        GlobalCategory(name=' Words with double letters'),
        GlobalCategory(name=' Children’s books'),
        GlobalCategory(name=' Things found at a bar'),
        GlobalCategory(name=' Names used in songs'),
        GlobalCategory(name=' Foods you eat raw'),
        GlobalCategory(name=' Places in Europe'),
        GlobalCategory(name=' Olympic events'),
        GlobalCategory(name=' Things you see at the zoo'),
        GlobalCategory(name=' Math terms'),
        GlobalCategory(name=' Animals in books or movies'),
        GlobalCategory(name=' Things to do at a party'),
        GlobalCategory(name='Type of soup'),
        GlobalCategory(name=' Things found in New York'),
        GlobalCategory(name=' Things you get tickets for'),
        GlobalCategory(name=' Things you do at work'),
        GlobalCategory(name=' Foreign words used in English'),
        GlobalCategory(name=' Things you shouldn’t touch'),
        GlobalCategory(name=' Spicy foods'),
        GlobalCategory(name=' Things at a carnival'),
        GlobalCategory(name=' Things you make'),
        GlobalCategory(name=' Places to hangout'),
        GlobalCategory(name=' Animal noises'),
        GlobalCategory(name=' Computer programs'),
        GlobalCategory(name=' Honeymoon spots'),
        GlobalCategory(name=' Things you buy for kids'),
        GlobalCategory(name=' Things that can kill you'),
        GlobalCategory(name=' Reasons to take out a loan'),
        GlobalCategory(name=' Words associated with winter'),
        GlobalCategory(name=' Things to do on a date'),
        GlobalCategory(name=' Historic events'),
        GlobalCategory(name=' Things you store items in'),
        GlobalCategory(name=' Things you do everyday'),
        GlobalCategory(name=' Things you get in the mail'),
        GlobalCategory(name=' Things you sit/on'),
        GlobalCategory(name=' Reasons to make a phone call'),
        GlobalCategory(name=' Types of weather'),
        GlobalCategory(name=' Titles people can have'),
        GlobalCategory(name=' Things that have buttons'),
        GlobalCategory(name=' Items you take on a road trip'),
        GlobalCategory(name=' Reasons to call 911'),
        GlobalCategory(name=' Things that make you smile'),
        GlobalCategory(name=' Ways to kill time'),
        GlobalCategory(name=' Things that can get you fired'),
        GlobalCategory(name=' Holiday Activities'),
        GlobalCategory(name='Things that are red'),
        GlobalCategory(name='Things in your car'),
        GlobalCategory(name='Word that ends with this letter'),
        GlobalCategory(name='Medical terms'),
        GlobalCategory(name='Movie title'),
        GlobalCategory(name='Dessert'),
        GlobalCategory(name='Countries in Asia'),
        GlobalCategory(name='Countries in Africa'),
        GlobalCategory(name='Country or city in South America'),
        GlobalCategory(name='Songs before 2000'),
        GlobalCategory(name='Songs after 2000'),
        GlobalCategory(name='Things made of glass'),
        GlobalCategory(name='Things that can break'),
        GlobalCategory(name='Things that are flat'),
        GlobalCategory(name='Things made of wood'),
        GlobalCategory(name='Brands'),
        GlobalCategory(name='Mammal'),
        GlobalCategory(name='Things that have wheels'),
        GlobalCategory(name='Things in a mall'),
        GlobalCategory(name='Things that use electricity'),
        GlobalCategory(name='Science terms'),
        GlobalCategory(name='Something you see in Canada'),
        GlobalCategory(name='Things at a sports game'),
        GlobalCategory(name='Things that are slow'),
        GlobalCategory(name='Things that cost more than $1000 USD'),
        GlobalCategory(name='Things at the dollar store'),
        GlobalCategory(name='Things at a picnic'),
    ]

    GlobalCategory.objects.bulk_create(categories)

def reverse_insert_data(apps, schema_editor):
    # Get the model
    GlobalCategory = apps.get_model('game', 'GlobalCategory')

    # Remove inserted data (optional)
    GlobalCategory.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20220912_2342'),
    ]


    operations = [
        migrations.RunPython(insert_data, reverse_insert_data),
    ]
