from DailyCheckBot import *


bot = DailyCheckBot()
bot.login()
try:
    bot.fakeoptions()
    print('Daily check complete')
except:
    print('Daily check has been completed already')
