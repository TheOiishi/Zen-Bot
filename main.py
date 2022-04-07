import json
import random
import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
status = cycle(['Being Built', 'Testing new stuff.'])

client = commands.Bot(command_prefix='"')



        


@client.command()
async def changeprefix(ctx, prefix):
    await ctx.send(f'This is used to change the prefix of the bot.')
    
    
    
@client.event
async def on_member_remove(member, ctx=None):
    await ctx.send(f'(member) has left the server')

@client.command()
async def ping(ctx):

  embed = discord.Embed(title='Pong!',description=f'{(client.latency * 1000)}ms')

  await ctx.send("Pong!", embed=embed)

@client.command(aliases=['8ball'])
async def Eightball(ctx, *, question):
    responses = ['It is certain',
                 'Without a doubht',
                 'Yes',
                 'No',
                 'Probably',
                 "Don't have High Hopes cuz that isn't gonna happen",
                 'Best not to ask',
                 'Yes for sure',
                 'Ask again later',
                 'It is Decided, Yes',
                 'Signs point to yes!!!',
                 'Most likely',
                 'Yes definitely.',
                 'My sources say a no',
                 'My sources say a yes',
                 'Sent a Detective to the question and the Detective came back with a Yes',
                 'Maybe',
                 'Very doubtful',
                 'Cannot predict now',]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['hg','Hg'])
async def howgay(ctx, *, questions):


    r = random.randint(0, 100)

    embed2 = discord.Embed(title='Gay Machine ', description=f'{questions} is {r}% Gay :rainbow_flag:')

    await ctx.send(embed=embed2)

@client.command(aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount+1)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for reason')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator, = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return





@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command sent')



@clear.error
async def clear_error(ctx, error):
    """Command which is used to Delete messages"""
    await ctx.send("Please provide a specific amount of messages that needs to be deleted.")
    if isinstance(error, commands.MissingRequiredArguement):
        await ctx.send('Please specify an amount of messages that needs to be deleted.')






@client.command()
async def info(ctx, *, member: discord.Member):
    """Tells you some info about the member."""
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))



@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')


def is_it_me(ctx):
    return ctx.author.id == 906909174984740914


@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi im {ctx.author}')    




























client.run('OTQzNjg4MzcxODgzMDg1ODI0.Yg2sSA.esoetHwHkAhvhnQjWFup46fdaaI')


