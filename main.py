import discord
from discord.ext import commands
from utils import json_handler


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="$",
            intents= discord.Intents.all()
        )


    async def setup_hook(self) -> None:
        for command_name in json_handler.Read("config.json")["modules"]:
            await self.load_extension(f"modules.{command_name}")
        await bot.tree.sync()

    async def on_ready(self):
        print(f"{self.user.name} has connected to discord!")

    async def on_message(self, message: discord.Message) -> None:
        content = message.content
        if content.startswith("조랭봇 "):
            try:
                answer = json_handler.Read("answer.json")[content[4:]]
            except:
                answer = "아직 모르는 단어예요!\n`/가르치기` 명령어를 써서 가르쳐 주세요!"

            await message.channel.send(answer)


bot = Bot()
bot.run(json_handler.Read("config.json")["token"])