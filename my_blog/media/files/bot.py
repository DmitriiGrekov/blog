import discord
import os
from discord.ext import commands
from discord.utils import get
import wget
import requests
from bs4 import BeautifulSoup


client = commands.Bot(command_prefix = '.')


@client.event

async def on_ready():
    print("Bot connected")




@client.command(pass_context = True)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}, I am a Bot for discord')

#connect

token =  'Njk5NjkyOTMyODMxMjQ4Mzg0.Xplt_A.VX8QHWi7v09RRo1Mi_RcxtMbr6A'




@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients,guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоединился к каналу:{channel}')




@client.command()
async def leave(ctx):
    
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients,guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот оключился от канала:{channel}')









def get_html(url):
    r = requests.get(url)
    return r.text



def get_link(html):
    b=BeautifulSoup(html,'html.parser')
    item = b.findAll('div',{'class':'actions'})[0]
    link = item.find('li',{'class':'play'}).get('data-url')
    return link
    

def downloads(s):
    filename = wget.download(s,bar = None)
    os.rename(filename, 'song.mp3')

@client.command()
async def play(ctx,*,song):
    song_there = os.path.isfile('song.mp3')

    try:
        if song_there:
            os.remove('song.mp3')
            print('Старый файл удалён')

    except PermissionError:
        print('не удалось удалить файл')
    await ctx.send('Пожалуйста ожидайте')
    voice = get(client.voice_clients,guild = ctx.guild)
    print(song)
    arr = song.split(' ')
    string = "%20".join(arr)
    url = 'https://muzofond.fm/search/'+string
    html = get_html(url)
    downloads(get_link(html))
    voice.play(discord.FFmpegPCMAudio('song.mp3'),after = lambda e:print({song},'закончила своё проигрывание'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    await ctx.send(f'Сейчас пригрывается музыка: {song}')






client.run(token)
