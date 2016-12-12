
import sopel
import random
@sopel.module.commands('meme') 
def meme(bot, trigger):
    """Gives a random Meme | Usage .meme"""
    messages = [ "http://i.imgur.com/udeyF4n.jpg", "http://i.imgur.com/T8TDgBS.jpg", "http://i.imgur.com/12sjpB9.jpg ", 
"http://i.imgur.com/NXqr5vR.png ", "http://i.imgur.com/mlg9N5y.jpg", "http://i.imgur.com/JTEo0Ia.jpg", 
"http://i.imgur.com/BydxXup.jpg ", "http://i.imgur.com/T4kwnc5.jpg ", "http://i.imgur.com/0mdgLye.jpg ", 
"http://i.imgur.com/l8TD0el.png", "http://i.imgur.com/CS0rX6f.jpg", "http://i.imgur.com/D9vPjr4.jpg ", 
"http://i.imgur.com/FxFBWUf.jpg", "http://i.imgur.com/NEQHkLN.jpg ", "http://i.imgur.com/1Rh79jv.jpg " ]
    answer = random.randint(0,len(messages) - 1)
    bot.say(messages[answer]);
