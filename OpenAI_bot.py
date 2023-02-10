import openai
import discord

openai.api_key = "YOUR_API_KEY"

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!generate"):
        prompt = message.content[9:]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        generated_text = response["choices"][0]["text"]
        await message.channel.send(generated_text)

client.run("YOUR_DISCORD_BOT_TOKEN")
