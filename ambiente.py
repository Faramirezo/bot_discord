import discord

def contaminacion_suelo():
    embed = discord.Embed(
        title = "1. Contaminacion en los suelos",
        description = "Averigua cuales son los objetos que destruyen el suelo",
        color = 0x00aaff
    )
    embed.add_field(
        name = "Contaminantes del suelo",
        value= "El plastico",
        inline= False
    )
    embed.add_field(
        name = "Contaminantes del suelo",
        value= "Metales pesados",
        inline= False
    )
    embed.add_field(
        name = "Contaminantes del suelo",
        value= "Sustancias quimicas",
        inline= False
    )
    embed.set_thumbnail(
        url= "https://i.postimg.cc/G3W72jrD/img-1.webp" 

    )

    return embed
def solucion_suelo():
    embed = discord.Embed(
        title = "2. Ayuda a los suelos",
        description = "Averigua como mantener tu suelo en buenas condiciones de forma cotidiana",
        color = 0x00aaff
    )
    embed.add_field(
        name = "Practicas para cuidar el suelo",
        value= "Consumir alimentos sostenibles",
        inline= False
    )
    embed.add_field(
        name = "Practicas para cuidar el suelo",
        value= "reutiliza todo lo que puedas",
        inline= False
    )
    embed.set_thumbnail(
        url= "https://i.postimg.cc/G3W72jrD/img-1.webp" 

    )

    return embed
def purificacion_suelo():
    embed = discord.Embed(
        title = "3. Purificacion en los suelos",
        description = "Mira como purificar o limpiar el suelo",
        color = 0x00aaff
    )
    embed.add_field(
        name="Practicas para cuidar el suelo",
        value="Cultivar ciertas plantas permite la purificacion de ciertas toxinas",
        inline= False
    )
    embed.add_field(
        name="Practicas para cuidar el suelo",
        value="El agua es un diluyente natural por lo cual desintegra ciertas toxinas",
        inline= False
    )
    embed.add_field(
        name="Practicas para cuidar el suelo",
        value="Sabias que el calcio (polvo de concha) en la tierra puede anular el acido de ciertas plantas",
        inline= False
    )
    embed.add_field(
        name="Practicas para cuidar el suelo",
        value="Puedes crear abono de desechos organicos ya que nutre la tierra",
        inline= False
    )

    embed.set_thumbnail(
        url= "https://i.postimg.cc/G3W72jrD/img-1.webp" 

    )

    return embed