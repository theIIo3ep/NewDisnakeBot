import disnake
from disnake.ext import commands
import os
import config

bot = commands.Bot(command_prefix=config.prefix, help_command=None, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print()
    print(" --- Бот запущен --- ")
    print(f"Имя бота: {bot.user} | Айди: {bot.user.id}")
    print(f"Версия бота: {config.version} | Пинг: {round(bot.latency * 1000)} мс")
    print(" --- Бот запущен --- ")
    print()
    print(" --- Загрузка модулей --- ")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config.token)