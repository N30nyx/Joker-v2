import discord, asyncio
import requests
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from funcs import get_main, getcdt, openimg

#v.pagin
async def vpaginate(bot,dictx,ctx,paginationList,editer=None):
  #Sets a default embed
  current = 0
  #Sending first message
  #I used ctx.reply, you can use simply send as

  mainMessage = await editer.edit(None,
      embed = paginationList[current],
      components = [ #Use any button style you wish to :)
          [
              Button(
                  label = "⬅️",
                  id = "back",
                  style = ButtonStyle.red
              ),
              Button(
                  label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                  id = "cur",
                  style = ButtonStyle.grey,
                  disabled = True
              ),
              Button(
                  label = "🔍",
                  id = "view",
                  style = ButtonStyle.grey,
              ),
              Button(
                  label = "➡️",
                  id = "front",
                  style = ButtonStyle.red
              )
          ]
      ]
  )
  #Infinite loop
  while True:
      #Try and except blocks to catch timeout and break
    try:
      interaction = await bot.wait_for(
        "button_click",
        check = lambda i: i.component.id in ["back", "front","view"] and i.author.id == ctx.author.id, #You can add more
        timeout = 20 #10 seconds of inactivity
        )
      def is_correct(m):
        print(m.author)
        return m.author == ctx.author



        #Getting the right list index
      if interaction.component.id == "back":
          current -= 1
      elif interaction.component.id == "front":
          current += 1
      elif interaction.component.id == "view":
        await editer.edit(embed = dictx[str(current)],
          components = [ 
              [
                  Button(
                      label = "⬅️",
                      id = "gback",
                      style = ButtonStyle.red
                  )
                  
              ]
          ]
        )
        interaction = await bot.wait_for(
        "button_click",
        check = lambda i: i.component.id in ["gback"] and i.author.id == ctx.author.id, #You can add more
        timeout = 20 #10 seconds of inactivity
        )
        if interaction.component.id == "gback":
          await editer.edit(
          embed = paginationList[current],
          components = [ #Use any button style you wish to :)
              [
                  Button(
                      label = "⬅️",
                      id = "back",
                      style = ButtonStyle.red
                  ),
                  Button(
                      label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                      id = "cur",
                      style = ButtonStyle.grey,
                      disabled = True
                  ),
                  Button(
                      label = "🔍",
                      id = "view",
                      style = ButtonStyle.grey,
                  ),
                  Button(
                      label = "➡️",
                      id = "front",
                      style = ButtonStyle.red
                  )
              ]
          ]
      )
          
          
      #If its out of index, go back to start / end
      if current == len(paginationList):
          current = 0
      elif current < 0:
          current = len(paginationList) - 1

        #Edit to new page + the center counter changes
      await editer.edit(
          embed = paginationList[current],
          components = [ #Use any button style you wish to :)
              [
                  Button(
                      label = "⬅️",
                      id = "back",
                      style = ButtonStyle.red
                  ),
                  Button(
                      label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                      id = "cur",
                      style = ButtonStyle.grey,
                      disabled = True
                  ),
                  Button(
                      label = "🔍",
                      id = "view",
                      style = ButtonStyle.grey,
                  ),
                  Button(
                      label = "➡️",
                      id = "front",
                      style = ButtonStyle.red
                  )
              ]
          ]
      )
    except asyncio.TimeoutError:
        #Disable and get outta here
        await editer.edit(
            components = [
                [
                    Button(
                        label = "⬅️",
                        id = "back",
                        style = ButtonStyle.red,
                        disabled = True
                    ),
                    Button(
                        label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                        id = "cur",
                        style = ButtonStyle.grey,
                        disabled = True
                    ),
                    Button(
                        label = "🔍",
                        id = "view",
                        style = ButtonStyle.grey,
                        disabled = True
                    ),
                    Button(
                        label = "➡️",
                        id = "front",
                        style = ButtonStyle.red,
                        disabled = True
                    )
                ]
            ]
        )
        break


#s.pagin
async def paginate(bot,dictx,ctx,paginationList,editer=None):
  #Sets a default embed
  current = 0
  #Sending first message
  #I used ctx.reply, you can use simply send as

  mainMessage = await editer.edit(None,
      embed = paginationList[current],
      components = [ #Use any button style you wish to :)
          [
              Button(
                  label = "⬅️",
                  id = "back",
                  style = ButtonStyle.red
              ),
              Button(
                  label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                  id = "cur",
                  style = ButtonStyle.grey,
                  disabled = True
              ),
              Button(
                  label = "🗨️",
                  id = "chat",
                  style = ButtonStyle.grey,
              ),
              Button(
                  label = "➡️",
                  id = "front",
                  style = ButtonStyle.red
              )
          ]
      ]
  )
  #Infinite loop
  while True:
      #Try and except blocks to catch timeout and break
    try:
      interaction = await bot.wait_for(
        "button_click",
        check = lambda i: i.component.id in ["back", "front","chat"] and i.author.id == ctx.author.id, #You can add more
        timeout = 20 #10 seconds of inactivity
        )
      def is_correct(m):
        print(m.author)
        return m.author == ctx.author



        #Getting the right list index
      if interaction.component.id == "back":
          current -= 1
      elif interaction.component.id == "front":
          current += 1
      elif interaction.component.id == "chat":
        keyr = await bot.wait_for("message", check = lambda msg: msg.author.id == ctx.author.id, timeout = 20)
        if str(keyr.content) in dictx:
          dz = 0
          listfp = []
          dictfp = {}
          iz = dictx[str(keyr.content)]
          await asyncio.sleep(4)
          response = requests.request("GET",f"https://api.jikan.moe/v3/character/{iz}")
          az = response.json()
          

          iz = str(iz)
          openimg(iz)
          cdt = getcdt()
          for item in cdt[iz]:
            name = az["name"]
            series = az["animeography"][0]["name"]
            aliases = len(az["nicknames"])
            wishlisted = cdt[iz][item]["wishlisted"]
            burnt = cdt[iz][item]["burnt"]
            circ = cdt[iz][item]["circ"]
            tcr = cdt[iz][item]["tcr"]
            cr = cdt[iz][item]["cr"]
            s = cdt[iz][item]["0"]
            ss = cdt[iz][item]["1"]
            sss = cdt[iz][item]["2"]
            ssss = cdt[iz][item]["3"]
            sssss = cdt[iz][item]["4"]
            desc = f"""

            Character · **{name}**
            Series · **{series}**
            Wishlisted · **{wishlisted}**
            Aliases · **{aliases}**

            Total generated · **{circ}**
            Total claimed · **{tcr}**
            Total burned · **{burnt}**
            Total in circulation · **{circ}**
            Claim rate · **{cr}%**

            Circulation (★★★★) · **{sssss}**
            Circulation (★★★☆) · **{ssss}**
            Circulation (★★☆☆) · **{sss}**
            Circulation (★☆☆☆) · **{ss}**
            Circulation (☆☆☆☆) · **{s}**
            """
            embed = discord.Embed(title="Character lookup",description=desc,color=ctx.author.color)
            embed.set_thumbnail(url=cdt[iz][item]["img"])
            listfp.append(embed)
            embedw = discord.Embed(title="Character lookup",desc=f"{series} · **{name}**",color=ctx.author.color)
            embedw.set_image(url=cdt[iz][item]["img"])
            dictfp[str(dz)] = embedw
            dz += 1
          
          msg = await ctx.send("loaded!")

          await vpaginate(bot,dictfp,ctx,listfp,msg)
          
      #If its out of index, go back to start / end
      if current == len(paginationList):
          current = 0
      elif current < 0:
          current = len(paginationList) - 1

        #Edit to new page + the center counter changes
      await editer.edit(
          embed = paginationList[current],
          components = [ #Use any button style you wish to :)
              [
                  Button(
                      label = "⬅️",
                      id = "back",
                      style = ButtonStyle.red
                  ),
                  Button(
                      label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                      id = "cur",
                      style = ButtonStyle.grey,
                      disabled = True
                  ),
                  Button(
                      label = "🗨️",
                      id = "chat",
                      style = ButtonStyle.grey,
                  ),
                  Button(
                      label = "➡️",
                      id = "front",
                      style = ButtonStyle.red
                  )
              ]
          ]
      )
    except asyncio.TimeoutError:
        #Disable and get outta here
        await editer.edit(
            components = [
                [
                    Button(
                        label = "⬅️",
                        id = "back",
                        style = ButtonStyle.red,
                        disabled = True
                    ),
                    Button(
                        label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                        id = "cur",
                        style = ButtonStyle.grey,
                        disabled = True
                    ),
                    Button(
                        label = "🗨️",
                        id = "chat",
                        style = ButtonStyle.grey,
                        disabled = True
                    ),
                    Button(
                        label = "➡️",
                        id = "front",
                        style = ButtonStyle.red,
                        disabled = True
                    )
                ]
            ]
        )
        break
