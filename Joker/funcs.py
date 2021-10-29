import asyncio
import discord
import requests
from discord_components import DiscordComponents, Button, ButtonStyle
import json


def getframe(img,frame,file,file2):
  data = f"{img} {frame} {file} {file2}"
  response = requests.request("GET",url=f"https://japi.eris9.repl.co/api/getframe?data={data}")
  return response.text



async def conf(bot,ctx,msg="Confirmed Successfully",title="Sucessfull!",one="✔️",two="❌"):
    embed = discord.Embed(title=title,description=msg,color=ctx.author.color)
    await ctx.send("Buttons!", components=[Button(label=one, custom_id="t",style=ButtonStyle.green),Button(label=two, custom_id="f",style=ButtonStyle.red)])
    try:
        interaction = await bot.wait_for(
            "button_click", check=lambda inter: inter.custom_id in ["t","f"],
            timeout = 10.0
        )
        if interaction.component.id == "t":
            await ctx.message.edit(embed=embed)
            return True
        if interaction.component.id == "f":
            return False
    except asyncio.TimeoutError:
        await ctx.send("You didn't respond in time.")
        return "."


def getcard():
  with open("data/card.json") as f:
    e = json.load(f)
  return e

def addcard(ctx,id,q,pby):
  e = getcard()
  x = "."
  while x in e["used"]:
    y = string.ascii_letters
    x = f"{random.choice(y)}{random.choice(y)}{random.choice(y)}{random.choice(y)}{random.choice(y)}{random.choice(y)}"
  e[x] = {}
  e[x]["malid"] = id
  e[x]["q"] = q
  e[x]["dby"] = ctx.author.id
  e[x]["pby"] = pby
  e[x]["effort"] = random.randint(1,40)*q
  e["used"].append(x)
  with open("data/card.json","w") as x:
    json.dump(e,x)

def getpub():
    with open("data/public.json","r") as f:
        e = json.load(f)
    return e

def getcdt():
    with open("data/dt.json","r") as f:
        e = json.load(f)
    return e

def opencdt(lix):
  dt = getcdt()
  malid = str(lix[0])
  if malid not in dt:
    dt[malid] = {}
  if str(lix[1]) not in dt[malid]:
    li = str(lix[1])
    dt[malid][li] = {}
    dt[malid][li]["img"] = lix[2]
    dt[malid][li]['wishlisted'] = 0
    dt[malid][li]["claimed"] = 0
    dt[malid][li]["burnt"] = 0
    dt[malid][li]["circ"] = 0
    dt[malid][li]["cr"] = 0
    dt[malid][li]["tcr"] = 0
    dt[malid][li]["ttcr"] = 0
    dt[malid][li]["4"] = 0
    dt[malid][li]["3"] = 0
    dt[malid][li]["2"] = 0
    dt[malid][li]["1"] = 0
    dt[malid][li]["0"] = 0
  with open("data/dt.json","w") as f:
    json.dump(dt,f)

def writepub(e):
    with open("data/public.json","w") as f:
        json.dump(e,f)

def openpub(user):
    pub = getpub()
    pub["users"][str(user.id)] = {}
    pub["users"][str(user.id)]["avatar"] = user.avatar_url
    pub["users"][str(user.id)]["name"] = user.name
    pub["users"][str(user.id)]["description"] = "no description."
    pub["users"][str(user.id)]["clans"] = []
    pub["users"][str(user.id)]["featured"] = {}
    pub["users"][str(user.id)]["featured"]["1"] = "."
    pub["users"][str(user.id)]["featured"]["2"] = "."
    pub["users"][str(user.id)]["featured"]["3"] = "."
    pub["users"][str(user.id)]["featured"]["4"] = "."
    pub["users"][str(user.id)]["featured"]["5"] = "."
    writepub(pub)

async def get_main(ctx,editer,pages):
    if editer != None:
        main = editer
        await main.edit(content=None,embed=pages[0])
    else:
	    main = await ctx.send(embed=pages[0])
    return main
async def paginate(ctx,pages,bot,editer=None):
    main = await get_main(ctx,editer,pages)
    await main.add_reaction('⏮')
    await main.add_reaction('⏪')
    await main.add_reaction('⏹')
    await main.add_reaction('⏩')
    await main.add_reaction('⏭')
    current_page = 0
    for i in range(50):
    	def check(reaction, user):
    		return user == ctx.author
    	try:
    		reaction, user = await bot.wait_for('reaction_add', check = check, timeout = 10)
    		await main.remove_reaction(reaction, user)
    		if str(reaction) == '⏮':
    			await main.edit(embed=pages[0])
    		elif str(reaction) == '⏭':
    			await main.edit(embed=pages[len(pages)-1])
    			current_page = len(pages)-1
    		elif str(reaction) == '⏩':
    			page = current_page+1
    			current_page = page
    			try:
    				await main.edit(embed=pages[page])
    			except:
    				pass
    		elif str(reaction) == '⏪':
    			page = current_page-1
    			current_page = page
    			try:
    				await main.edit(embed=pages[page])
    			except:
    				pass
    		elif str(reaction) == '⏹':
    			current_page = 0
    			await main.clear_reactions()


    	except asyncio.TimeoutError:
    		await main.clear_reactions()

def openimg(iz):
  lmfao = True
  cdt = getcdt()
  if str(iz) not in cdt:
    while lmfao == True:
      try:
        amtx = 1
        url = f"https://api.jikan.moe/v3/character/{iz}/pictures"
        print(url)


        pics = requests.request("GET",url=url)
        pics = pics.json()
        print(pics)
        if pics["pictures"] != []:


          for picture in pics["pictures"]:

            opencdt([iz,amtx,picture["image_url"]])
            lmfao=False
            amtx += 1
        if pics["pictures"] == []:
          lmfao=False
      except KeyError:
        ok = "ok"
      
