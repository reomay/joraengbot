import discord
from discord import app_commands
from discord.ext import commands
from utils import json_handler

class teach(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="가르치기",
        description="조랭봇에게 단어를 가르칩니다.",
    )
    async def teach_command(self, interaction: discord.Interaction, word: str, answer: str) -> None:
        try:
            list = json_handler.Read("answers.json")[word]
            list.append(answer)
        except:
            json_handler.Update("answers.json", {
                word: [answer]
            })


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        teach(bot)
    )