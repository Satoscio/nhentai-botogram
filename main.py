from nhentai import Nhentai
import requests
import botogram

bot = botogram.create("TOKEN")

@bot.command("search")
def search_command(chat, message, args):
    if not args:
        chat.send("Command usage: `/search <ID>`")
    else:
        try:
            if Nhentai().book_info(int(args[0]))["title"]:
                chat.send("https://nhentai.net/g/" + str(args[0]))
        except KeyError:
            chat.send("404 Not Found")
        except ValueError:
            chat.send("Invalid data")

@bot.command("latest")
def latest_command(chat, message, args):
    chat.send("https://nhentai.net/g/" + str(Nhentai().latest_id()))

@bot.command("random")
def random_command(chat, message, args):
    r = requests.get("https://nhentai.net/random/", allow_redirects=False)
    random_nhid = r.headers['Location']
    chat.send("https://nhentai.net" + str(random_nhid))

@bot.command("info")
def info_command(chat, message, args):
    if not args:
        chat.send("Command usage: `/info <ID>`")
    else:
        try:
            if Nhentai().book_info(int(args[0]))["title"]:
                dictx = Nhentai().book_info(int(args[0]))
                chat.send_photo(url=Nhentai().book_cover(int(args[0])), caption=
                                    "*Short title*: " + str(dictx["title"]["pretty"]) +
                                    "\n*English title*: " + str(Nhentai().book_title(int(args[0]))) + 
                                    "\n*Japanese title*: " + str(Nhentai().book_title_jp(int(args[0]))) +
                                    "\n*Author(s)*: " + str(Nhentai().book_artists(int(args[0]), return_string=True)) +
                                    "\n*Language*: " + str(Nhentai().book_language(int(args[0]), return_string = True)) +
                                    "\n*Pages*: " + str(Nhentai().book_pagenum(int(args[0]))) + 
                                    "\n*Category*: " + str(Nhentai().book_category(int(args[0]))) + 
                                    "\n\n*Tags*: " + str(Nhentai().book_tags(int(args[0]), return_string = True)) + 
                                    "\n\n*Fucking jerk off to it here*: https://nhentai.net/g/" + str(int(args[0])), syntax="markdown")
        except KeyError:
            chat.send("404 Not Found")
        except ValueError:
            chat.send("Invalid data")

@bot.command("start")
def start_command(chat, message, args):
    """Hello"""
    chat.send("Welcome to this fucking bot.")

@bot.command("source")
def source_command(chat, message, args):
    """Bot source code on GitHub"""
    chat.send("Bot Source: https://github.com/Satoscio/nhentai-botogram")

if __name__ == "__main__":
    bot.run()