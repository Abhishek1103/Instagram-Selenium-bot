from Bot import InstaBot
from Const import USERNAME
from time import sleep

bot = InstaBot("Chrome")
bot.login()
sleep(20)
bot.notif_popup()
bot.open_user(USERNAME)
src_set = bot.view_pics()
try:
    for s in src_set:
        f = open('file', 'a')
        f.write(s+"\n")

except:
    f.close()
    pass
f.close()
# bot.download_pics(src_set)
