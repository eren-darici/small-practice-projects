import discord
import random
from discord.ext import commands
import pandas as pd

class HP():
    def __init__(self, base_hp = 100):
        self.base_hp = base_hp

    def hit(self, hit_point):
        self.hit_point =  hit_point
        if self.base_hp == 0:
            return
        else:
            self.base_hp -= self.hit_point
        return self.base_hp

    def heal(self, heal_point):
        self.heal_point = heal_point
        if self.base_hp == 100:
            return "hp is full."
        elif self.base_hp == 0:
            return "cannot heal."
        else:
            self.base_hp += self.heal_point
        return self.base_hp

    def show_hp(self):
        return self.base_hp

class Inventory():
    def __init__(self, inventory = [], new_Inventory = []):
        self.inventory = inventory
        self.new_Inventory = new_Inventory


    # Adding to inventory
    def add_Inventory(self, item_Name):
        self.item_Name = item_Name
        self.inventory.append(self.item_Name)

    # Deleting from inventory
    def delete_Inventory(self, item_Index):
        self.item_Index = item_Index
        self.inventory.pop(self.item_Index)

    # Show inventory
    def show_Inventory(self):

        item_dataframe = pd.DataFrame({
            "item_list": self.inventory
        })

        # Checking if inventory is empty - 1
        isempty = item_dataframe.empty

        # Checking if inventory is empty - 2
        if isempty == True:
            return "inventory is empty"
        else:
            return item_dataframe

hp = HP()
inv = Inventory()

client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Bot başlatıldı. {0.user}'.format(client))

help = '''
        Komutlar \n
        Zar Atmak\n
        **************\n
        !zar6 \n
        !zar8 \n
        !zar10 \n
        !zar12 \n
        !zar20 \n

        Can İşlemleri\n
        **************\n
        !heal deger \n
        !hit deger \n
        !show_hp
        '''

#yeni_uye_Channel = client.get_channel(new member channel here)

newUserMessage = """" Selamlar, {member}! """
@client.event
async def on_member_join(member):
    await yeni_uye_Channel.send(member, " ,hoşgeldin!")



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!selam'):
        await message.channel.send('Selamlar, {0.author}!'.format(message))
    if message.content.startswith('!help'):
        await message.channel.send(help)


    # Dices
    if message.content.startswith('!zar6'):
        await message.channel.send(random.randint(1, 6))
    if message.content.startswith('!zar10'):
        await message.channel.send(random.randint(1, 10))
    if message.content.startswith('!zar8'):
        await message.channel.send(random.randint(1, 8))
    if message.content.startswith('!zar12'):
        await message.channel.send(random.randint(1, 12))
    if message.content.startswith('!zar20'):
        await message.channel.send(random.randint(1, 20))

    # Health Actions
    if message.content.startswith('!heal'):
        userInput_heal = int(message.content[6:])
        await message.channel.send(hp.heal(userInput_heal))

    if message.content.startswith('!hit'):
        userInput_hit = int(message.content[5:])
        await message.channel.send(hp.hit(userInput_hit))
        if hp.show_hp() == 0:
            await message.channel.send('you died.')

    if message.content.startswith('!show_hp'):
        await message.channel.send(hp.show_hp())

    # Inventory Actions
    if message.content.startswith('!show_inv'):
        await message.channel.send(inv.show_Inventory())
    if message.content.startswith('!inv_add'):
        try:
            userInput_addinv = str(message.content[9:])
            await message.channel.send(inv.add_Inventory(userInput_addinv))
        except:
            pass
    if message.content.startswith("!inv_del"):
        try:
            userInput_delinv = int(message.content[9:])
            await message.channel.send(inv.delete_Inventory(userInput_delinv))
        except:
            pass
    if message.content.startswith('!foto'):
        directory = message.content[6:]
        await message.channel.send(file = discord.File(directory))




# client.run(inset your token here)
