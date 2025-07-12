import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        await bot.tree.sync()
        print("Slash commands synced!")
    except Exception as e:
        print(f"Errore sincronizzazione comandi slash: {e}")

MEMES = {
    "asgore": "asgore.gif",
    "sans": "sans.gif",
    "papyrus": "papyrus.gif",
    "deltarune": "deltarune.png"
}

@bot.tree.command(name="listameme", description="Mostra la lista dei meme disponibili")
async def listameme(interaction: discord.Interaction):
    lista = "\n".join(f"- **{nome}**" for nome in MEMES.keys())
    embed = discord.Embed(
        title="📜 Lista Meme Disponibili",
        description=lista,
        color=discord.Color.purple()
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.command(name="asgore")
async def asgore(ctx):
    try:
        file = discord.File("asgore.gif")
        await ctx.send(file=file)
    except Exception as e:
        await ctx.send(f"Errore nell'inviare il file: {e}")

@bot.command(name="deltarune")
async def asgore(ctx):
    try:
        file = discord.File("deltarune.png")
        await ctx.send(file=file)
    except Exception as e:
        await ctx.send(f"Errore nell'inviare il file: {e}")

@bot.command(name="papyrus")
async def asgore(ctx):
    try:
        file = discord.File("papyrus.gif")
        await ctx.send(file=file)
    except Exception as e:
        await ctx.send(f"Errore nell'inviare il file: {e}")

@bot.command(name="sans")
async def asgore(ctx):
    try:
        file = discord.File("sans.gif")
        await ctx.send(file=file)
    except Exception as e:
        await ctx.send(f"Errore nell'inviare il file: {e}")

bot.run("MTM5MzQ0NjY4MTU2NzI5NzYyNw.G1gX8X.N1nKEQfGLgVbT-zkdD3o800JQmQcES0VztCnNM")
