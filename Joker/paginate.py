import discord, asyncio
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from funcs import get_main

async def paginate(bot,ctx,paginationList,editer=None):
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
										check = lambda i: i.component.id in ["back", "front"] and i.author.id == ctx.author.id, #You can add more
										timeout = 20.0 #10 seconds of inactivity
								)
								#Getting the right list index
								if interaction.component.id == "back":
										current -= 1
								elif interaction.component.id == "front":
										current += 1
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
																label = "➡️",
																id = "front",
																style = ButtonStyle.red,
																disabled = True
														)
												]
										]
								)
								break
