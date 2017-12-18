import discord
    import asyncio

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.content == "Hello":
            await client.send_message(message.channel, "World")

    client.run(MzkyMTY5NzEyNTU0ODY4NzU2.DRjWKA.3f2LxxH-6j0ZT-qvWmGdvc8n5DE)