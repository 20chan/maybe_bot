from maybe_bot import Bot

bot = Bot()


@bot.Got()
def got_message(msg):
    print('Got {}'.format(msg))


@bot.Tagged('philly')
def tag_philly(msg):
    print('you tagged philly!')


@bot.Contained('damn')
def contain_bad(msg):
    print('that\'s bad word.')

bot.input('hi')
bot.input('hey phillly')
bot.input('heeeey @philly')
bot.input('damn!')