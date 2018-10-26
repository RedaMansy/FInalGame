from items import *

room_reception = {
    "name": "The Reception",

    "description":
    """You have just entered the Reception. The interior is very modern,\nwith sleek furnishings and glass walls.\nOver By The Window You See A Receptionist Who Seems To Be Daydreaming""",

    "exits": {"east": "The Shopping Centre", "west": "The Lab", "south": "The Library", "north":"Home"},

    "items": []
}

room_lab = {
    "name": "The Lab",

    "description":
    """You enter the lab. It isn't too crowded. A few people are around, working and seeing that stresses you 
    out becuase you feel that you should be working too. You look around, not knowing who you're looking for.\nYou Look Onwards, Trying To Find Someone Who Will Help""",

    "exits":  {"west": "The Library", "east": "The Cafeteria", "north": "The Reception"},

    "items": [item_github, item_thebae]
}

room_library = {
    "name": "The Library",

    "description":
    """You are standing in the library, Everyone is working or reading quietly.
    As everyone is focusing on their own work, nobody notice that there is a notepad on the floor.
    """,

    "exits": {"east": "The Lab"},

    "items": [item_notes, item_voucher, item_profoak]
}

room_cinema = {
    "name": "The Cinema",

    "description":
    """You wander around the city aimlessly and you find a cinema that you've never noticed before.
    It is oddly empty, apart from one man and you are perplexed as you've been in this area many times in the past and have never noticed it.
    The only movie you find playing is David Fincher's The Social Network.""",

    "exits": {"north": "The Shopping Centre"},

    "items": []
}

room_cafeteria = {
    "name": "The Cafeteria",

    "description":
    """You walk in the cafeteria and immediately notice the lingering waft of coffee in the air. 
    You look at the black board by the cashier and notice that they're serving hotdogs and tiramisu. Realising You Are A Broke Student,\nYou Resort To The 99p Section\n(Foodstuffs Replenish Your Energy)""",

    "exits": {"west": "The Lab", "north": "The Reception"},

    "items": [item_food, item_water, item_bluebear]
}

room_shoppingcentre = {
    "name": "The Shopping Centre",

    "description":
    """You Enter The Bustling Shopping Centre,\nRows Upn Rows Of People Are Cramming Into Shops\nBut You Notice A 40 or So Year Old Man Playing Metal Gear 5\nCalling It His Creation And A Waste Of Time\nYou Soon Realise That This Is Hideo Kojima, One Of The Creators Of The Konami Code""",

    "exits": {"west": "The Reception", "north": "The Bar","south":"The Cinema","east":"The Petshop"},

    "items": [item_laptop, item_hideokojima]
}

room_home = {
    "name": "Home",

    "description":
    """You look around your home, it truly is a tip as you wander around.\nYou see a bowl with something green that you think was originally brown sitting\nin a bowl""",

    "exits": {"west": "The Reception", "south": "The Shopping Centre"},

    "items": []
}

room_bar = {
    "name": "The Bar",

    "description":
    """You Walk Into The Bar called "The Closet",\nSeemingly Empty Apart From Two Men Sharing A Strawberry Daquiri\nOnly one More Man Remains,\nA Seemingly Grouchy Old Man, Who You Scarce To Believe That Is Alan Turing\nYou Giggle To Yourself As You Realise He's "In The Closet" And Hasn't Come Out Yet""",

    "exits": {"west": "The Cafeteria", "north": "Home", "south": "The Shopping Centre"},

    "items": [item_NICoffee]
}

room_petshop = {
    "name": "The Petshop",

    "description":
    """You Find A Petshop\nWith What Looks To Be A Man Watching A Rabbit Attack A Snake,\nWhen You Come Over He Seems To Shout\n'Go On Python! You Cant Beat Anything!'\nHe Chuckles And Explains That He Named The Rabbit Python After Monty Python""",

    "exits": {"west": "The Shopping Centre"},

    "items": [item_food, item_pythonguy]
}

rooms = {
    "The Reception": room_reception,
    "The Lab": room_lab,
    "The Library": room_library,
    "The Cinema": room_cinema,
    "The Cafeteria": room_cafeteria,

    "The Shopping Centre": room_shoppingcentre,
    "The Bar": room_bar,
    "Home": room_home,
    "The Petshop": room_petshop,

}
