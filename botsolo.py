import discord
import os
import random
from discord.ext import commands 
#sm
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="$",intents=intents)
@bot.command()
async def reciclaje(ctx):
    rec= random.choice(os.listdir("imagenes"))
    with open(f'imagenes/{rec}', 'rb') as f:
        # ¡Vaacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    picture = discord.File(f)

@bot.command()
async def formas(ctx):
    lista =["Trata de comprar productos que utilicen menos envoltorios",
    "Reutilizar todos los productos que puedas",
    "Medir los desechos que se generan en un hogar",
    "Hacer composta",
    "Elegir productos duraderos",
    "Evitar usar productos desechables",
    "Usar la tecnología para leer en línea",
    ]
    sobre= random.choice(lista)
    await ctx.send(sobre)




