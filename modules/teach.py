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
            json_handler.Update("answers.json", {word: list})
        except:
            json_handler.Update("answers.json", {
                word: [answer]
            })
        await interaction.response.send_message(content=f"`{word}`라고 말하면 `{answer}`라고 대답하게 학습했습니다.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        teach(bot)
    )