import os
import hikari
import lightbulb
import miru
import dotenv


dotenv.load_dotenv()
bot = lightbulb.BotApp(
    os.getenv("token"),
    intents=hikari.Intents.ALL,
    help_slash_command=True,
)


def run() -> None:
    if os.name != "nt":
        import uvloop

        uvloop.install()
    bot.load_extensions("commands.PrefixCommands", "commands.SlashCommands")
    miru.install(bot)
    bot.run()
