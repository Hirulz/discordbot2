import discord
from bot_logic import gen_pass  #Para usar esta, debo tener un archivo que se llame bot_logic guardado en la misma carpeta de este archivo



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}') 

@client.event
async def on_message(message):
    if message.content.startswith('!mem'):
        with open('images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

client.run("TOKEN") # TOKEN --> No borrar