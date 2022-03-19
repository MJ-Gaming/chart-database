import os
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='MJ!')

testServerID = 734066960672751706

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type = nextcord.ActivityType.watching, name='PTFS Charts'))
    print('Ready for use!')
    print('---------------------------')

@client.slash_command(name = "ping", description = "Responds with 'pong'")
async def ping(interaction: Interaction):
    await interaction.response.send_message("🏓 Pong!")

@client.slash_command(name = "join", description = "Join the MJ's Charts Discord Server")
async def join(interaction: Interaction):
    embed = nextcord.Embed(title="Click here to join!", url="https://discord.gg/J4pXHwyDr5", colour=0x003B64)
    embed.set_author(name="MJ's Charts PTFS", icon_url="https://media.discordapp.net/attachments/927991956901089320/953323777188581476/Still_Logo_Transparent.png?width=699&height=700")
    await interaction.response.send_message(embed=embed)

@client.slash_command(name = "invite", description = "Invite this bot to to other servers")
async def invite(interaction: Interaction):
    embed = nextcord.Embed(title="Click here to invite!", url="https://discord.com/api/oauth2/authorize?client_id=932381557891686443&permissions=137439333440&scope=bot%20applications.commands", colour=0x003B64)
    embed.set_author(name="MJ's Charts Bot", icon_url="https://media.discordapp.net/attachments/927991956901089320/953323777188581476/Still_Logo_Transparent.png?width=699&height=700")
    await interaction.response.send_message(embed=embed)

@client.slash_command(name = "charts", description = "Access the chart database")
async def chart(
    interaction: Interaction,
    chart: str = SlashOption(name="options", description="Pick your chart option", choices={"airspace":"1", "checklist":"2","rockford":"3","perth":"4","tokyo":"5","izolirani":"6","larnaca":"7"})
):
    if chart == "1":
        embed = nextcord.Embed(title="Airspace Charts", description="Here's all the airspace related charts we have:",
                               colour=0x003B64)
        embed.add_field(name="〉Official Enroute Chart ~ Sander",
                        value="Sander's map of waypoints in PTFS.\n[Link](https://cdn.discordapp.com/attachments/929341507985637376/938176204245180497/Enroute_Chart_PTFS.png)",
                        inline=False)
        embed.add_field(name="〉PTFS_OCEAN_CROSSING_TRACKS ~ Gabe",
                        value="Gabe's map of ocean crossing tracks in PTFS.\n[Link](https://cdn.discordapp.com/attachments/929341507985637376/937524003818582066/PTFS_OCEAN_CROSSING_TRACKS.pdf)",
                        inline=False)
        embed.set_footer(text="MJ's Charts PTFS | Chart System",
                         icon_url="https://media.discordapp.net/attachments/927991956901089320/930572683605856286/White.png")
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/927991956901089320/953329782215565353/plane_5.gif")
        await interaction.response.send_message(embed=embed)

    elif chart == "2":
        embed = nextcord.Embed(title="Aircraft Checklists", description="Here's all the aircraft checklists we have: ",
                               colour=0x003B64)
        embed.add_field(name="〉A320/A319 ~ MBlox",
                        value="MBlox's A320/A319 checklist.\n[Link](https://cdn.discordapp.com/attachments/929341507985637376/933128648045756526/AIRBUSA319A320.CHECKLIST.pdf)",
                        inline=False)
        embed.add_field(name="〉B767-300ER ~ MBlox",
                        value="MBlox's B767-300ER checklist.\n[Link](https://cdn.discordapp.com/attachments/929341507985637376/933835162276466688/BOEING767-300ERCHECKLIST_1_20_2022.pdf)",
                        inline=False)
        embed.add_field(name="〉B777-300ER ~ Gabe",
                        value="Gabe's B777-300ER checklist.\n[Link](https://cdn.discordapp.com/attachments/879472733531029544/936039778644799558/B777-300ER_STANDARD_CHECKLIST.pdf)",
                        inline=False)
        embed.add_field(name="〉Cessna 172 ~ Gabe",
                        value="Gabe's Cessna 172 checklist.\n[Link](https://cdn.discordapp.com/attachments/901153105226375179/936405781262262312/CESSNA_172_STANDED_OPERATION_CHECKLIST.pdf)",
                        inline=False)
        embed.set_footer(text="MJ's Charts PTFS | Chart System",
                         icon_url="https://media.discordapp.net/attachments/927991956901089320/930572683605856286/White.png")
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/927991956901089320/953329782215565353/plane_5.gif")
        await interaction.response.send_message(embed=embed)

    elif chart == "3":
        embed = nextcord.Embed(title="Greater Rockford Charts", description="Here's all the charts we have for rockford: ",
                               colour=0x003B64)
        embed.add_field(name="〉Airport Chart ~ PTC",
                        value="Official in-game airport chart.\n[Link](https://ptfs.xyz/charts/light/IRFD%20Ground%20Chart.png)",
                        inline=False)
        embed.add_field(name="〉Offical Charts ~ PTC",
                        value="Official charts, github link.\n[Link](https://github.com/Treelon/ptfs-charts/tree/main/Rockford)",
                        inline=False)
        embed.add_field(name="〉ICAO Aerodrome Chart ~ Rish",
                        value="Rish's aerodrome chart for rockford.\n[Link](https://media.discordapp.net/attachments/836992980916371526/906887602735562762/unknown.png?width=1044&height=700)",
                        inline=False)
        embed.add_field(name="〉Control Zone Chart ~ Sander",
                        value="Sander's control zone chart for rockford.\n[Link](https://media.discordapp.net/attachments/878266040465891358/906876684702220338/IRFD_CTR-CTA_-_ENTRY-EXIT_AND_VRPs.png?width=495&height=700)",
                        inline=False)
        embed.add_field(name="〉IRFD_CHARTS ~ Sander",
                        value="Sander's document of charts for rockford. \n[Link](https://drive.google.com/file/d/1I-oucFK61M6QdSFdEPYWQ3P9dRZ8D7Jl/view?usp=sharing)",
                        inline=False)
        embed.add_field(name="〉KRFD CHARTS ~ Schad_Y",
                        value="Schad's document of charts for rockford.\n[Link](https://docs.google.com/presentation/d/1Mpo5ke2clIRRgLjx7jWZR6MJyRBrCJ40yDSaASSsbz8)",
                        inline=False)
        embed.add_field(name="〉ROPPESEN 20-11 KRFD SID/STAR ~ Nikita39",
                        value="Nikita's document of charts for rockford.\n[Link](https://docs.google.com/document/d/1N0wP0CkaUdsgWWoQA3Zw9p7WQEMxoDur-DY9g_zCrrk/edit)",
                        inline=False)
        embed.add_field(name="〉IRFD SID Chart ~ Maki",
                        value="Maki's document of charts for rockford.\n[Link](https://docs.google.com/document/d/1pOfIhQ9z6HSgFNjIMryd_FWwF_FgkAPvhK5xerOBex4/edit?usp=sharing)",
                        inline=False)
        embed.set_footer(text="MJ's Charts PTFS | Chart System",
                         icon_url="https://media.discordapp.net/attachments/927991956901089320/930572683605856286/White.png")
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/927991956901089320/953329782215565353/plane_5.gif")
        await interaction.response.send_message(embed=embed)

    elif chart == "4":
        embed = nextcord.Embed(title="Perth Charts", description="Here's all the charts we have for perth: ",
                               colour=0x003B64)
        embed.add_field(name="〉Airport Chart ~ PTC",
                        value="Official in-game airport chart.\n[Link](https://ptfs.xyz/charts/light/IPPH%20Ground%20Chart.png)",
                        inline=False)
        embed.add_field(name="〉Offical Charts ~ PTC",
                        value="Official charts, github link.\n[Link](https://github.com/Treelon/ptfs-charts/tree/main/Perth/Perth)",
                        inline=False)
        embed.add_field(name="〉YPPH CHARTS ~ Schad_Y",
                        value="Schad's document of charts for perth.\n[Link](https://docs.google.com/presentation/d/1hHIKTWivg3EB9XsTa1clcH7cgts-zE7sD8PZmk9eGlg)",
                        inline=False)
        embed.set_footer(text="MJ's Charts PTFS | Chart System",
                         icon_url="https://media.discordapp.net/attachments/927991956901089320/930572683605856286/White.png")
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/927991956901089320/953329782215565353/plane_5.gif")
        await interaction.response.send_message(embed=embed)

    elif chart == "5":
        embed = nextcord.Embed(title="Tokyo Charts", description="Here's all the charts we have for tokyo: ",
                               colour=0x003B64)
        embed.add_field(name="〉Airport Chart ~ PTC",
                        value="Official in-game airport chart.\n[Link](https://ptfs.xyz/charts/light/ITKO%20Ground%20Chart.png)",
                        inline=False)
        embed.add_field(name="〉Offical Charts ~ PTC",
                        value="Official charts, github link.\n[Link](https://github.com/Treelon/ptfs-charts/tree/main/Orenji/Tokyo)",
                        inline=False)
        embed.add_field(name="〉Visual Approach Chart ~ Sander",
                        value="Sander's visual approach chart for tokyo.\n[Link](https://cdn.discordapp.com/attachments/919656910007976017/939263726878609428/ITKO_Visual_Approach_Chart_-_ICAO.png)",
                        inline=False)
        embed.add_field(name="〉TMA Chart ~ Sander",
                        value="Sander's TMA chart for tokyo.\n[Link](https://cdn.discordapp.com/attachments/929341507985637376/939486782804869140/ITKO_TMA-TIA_CHART_TOKYO_TMA.png)",
                        inline=False)
        embed.add_field(name="〉Tokyo UK AIP ~ SQD_Yeet and Sander",
                        value="Sander's and SQD's document of charts for tokyo.\n[Link](https://docs.google.com/presentation/d/1PPpJoNXSOLL5DUMBSexPGDbDskA2nMkrPglJ35szKF4/edit?usp=sharing)",
                        inline=False)
        embed.add_field(name="〉ITKO Charts ~ Gabe",
                        value="Gabe's document of charts for tokyo.\n[Link](https://docs.google.com/document/d/1NjssUTQnlHVQiZciry656h5ZBu2xW7lJu2Q2L5G90CU/edit?usp=sharing)",
                        inline=False)
        embed.add_field(name="〉ITKO CHARTS ~ Nikita39",
                        value="Nikita's document of charts for tokyo.\n[Link](https://docs.google.com/document/d/1VZPegMnzg2cmiysxUPK3TeWvPqzk4RysnvHYmJJ47pM/edit?usp=sharing)",
                        inline=False)
        embed.set_footer(text="MJ's Charts PTFS | Chart System",
                         icon_url="https://media.discordapp.net/attachments/927991956901089320/930572683605856286/White.png")
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/927991956901089320/953329782215565353/plane_5.gif")
        await interaction.response.send_message(embed=embed)

    elif chart == "6":
        embed = nextcord.Embed(title="Izolirani Charts", description="Here's all the charts we have for izolirani: ",
                               colour=0x003B64)
        embed.add_field(name="〉Airport Chart ~ PTC",
                        value="Official in-game airport chart.\n[Link](https://ptfs.xyz/charts/light/IZOL%20Ground%20Chart.png)",
                        inline=False)
        embed.add_field(name="〉Offical Charts ~ PTC",
                        value="Official charts, github link.\n[Link](https://github.com/Treelon/ptfs-charts/tree/main/Izolirani/Izolirani)",
                        inline=False)
        embed.add_field(name="〉IZOL_CHARTS ~ Sander",
                        value="Sander's document of charts for izolirani.\n[Link](https://cdn.discordapp.com/attachments/876914987715686440/906579978722902046/IZOL_CHARTS.pdf)",
                        inline=False)
        embed.add_field(name="〉IZOL Charts ~ Nerdyisfat",
                        value="Nerdy's document of charts for izolirani.\n[Link](https://docs.google.com/document/d/199o7-Z5jhEWdgPbZGxuSKiBQUvNUmLU52koi_tuxPbs/edit?usp=sharing)",
                        inline=False)
        embed.set_footer(text="MJ's Charts PTFS | Chart System",
                         icon_url="https://media.discordapp.net/attachments/927991956901089320/930572683605856286/White.png")
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/927991956901089320/953329782215565353/plane_5.gif")
        await interaction.response.send_message(embed=embed)

    elif chart == "7":
        embed = nextcord.Embed(title="Larnaca Charts", description="Here's all the charts we have for larnaca: ",
                               colour=0x003B64)
        embed.add_field(name="〉Airport Chart ~ PTC",
                        value="Official in-game airport chart.\n[Link](https://ptfs.xyz/charts/light/ILAR%20Ground%20Chart.png)",
                        inline=False)
        embed.add_field(name="〉Offical Charts ~ PTC",
                        value="Official charts, github link.\n[Link](https://github.com/Treelon/ptfs-charts/tree/main/Cyprus/Larnaca)",
                        inline=False)
        embed.add_field(name="〉Larnaca Information Charts ~ Poptarsh",
                        value="Poptarsh's document of charts for larnaca.\n[Link](https://docs.google.com/presentation/d/10ZjuKVhReUspycpjkqtxftcgCs7dmS2mi7H0_UWhbOo/edit)",
                        inline=False)
        embed.add_field(name="〉ILAR CHARTS ~ Aloha",
                        value="Aloha's docuemnt of charts for larnaca.\n[Link](https://docs.google.com/document/d/1hbVXnIfK2KMrX_j1ie8l7y1fPe-yptfxWPgajC753Zw/edit?usp=sharing)",
                        inline=False)
        embed.add_field(name="〉ILAR Charts ~ Maki",
                        value="Maki's docuemnt of charts for larnaca.\n[Link](https://docs.google.com/document/d/11Wvou24H_RgUIn5VwJoQ5w4tnE5JZbtYTTbkuRDvtHk/edit)",
                        inline=False)
        embed.set_footer(text="MJ's Charts PTFS | Chart System",
                         icon_url="https://media.discordapp.net/attachments/927991956901089320/930572683605856286/White.png")
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/927991956901089320/953329782215565353/plane_5.gif")
        await interaction.response.send_message(embed=embed)

client.run(os.environ("SECRET_TOKEN"))