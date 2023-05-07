import disnake
from disnake.ext import commands
import config

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Модуль информации был загружен")

    @commands.slash_command(name="ping", description="Проверьте скорость работы бота.")
    async def ping(self, inter):
        embed = disnake.Embed(
            title="🏓 Пинг бота",
            description=f"Пинг бота сейчас: {round(self.bot.latency * 1000)} мс",
            colour=disnake.Color.from_rgb(47, 49, 54)
        )
        embed.set_footer(text=f"Имя бота: {config.namebot} | Версия: {config.version}", icon_url=inter.author.display_avatar.url)
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Info(bot))
    