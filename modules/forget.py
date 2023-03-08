import discord
from discord import app_commands
from discord.ext import commands
from utils import json_handler

class forget(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="잊기",
        description="조랭봇에게서 단어를 잊힙니다",
    )
    async def forget_command(self, interaction: discord.Interaction, word: str, answer: str) -> None:
        try:
            list = json_handler.Read("answers.json")[word]
            list.remove(answer)
            json_handler.Update("answers.json", {word: list})
        except:
            await interaction.response.send_message(content=f"배운적 없는 단어나 대답 입니다")
            return
        await interaction.response.send_message(content=f"조랭봇은 이제 `{answer}` 라는 대답를 모릅니다!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        forget(bot)
    )