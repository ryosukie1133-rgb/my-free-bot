import discord
from discord.ext import commands

# --- [ ตั้งค่าส่วนตัว ] ---
TOKEN = 'MTQ2NDg4NTAyNDMwNTMxNTkzMA.GI-mZq.WCYD1n1TYB8rCMm_W3a2GxnWH8G9c1DK8omusI'
ROLE_ID = 1466804755312541839  # ID ยศที่จะเสกให้ (Yot Share - SISI)
MY_ID = 1411888296270893251   # ID ของตัวคุณ (DELETX)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ บอท {bot.user} ออนไลน์พร้อมใช้งาน!')

# --- 1. ระบบเสกยศ (พิมพ์ !give @ชื่อคน) ---
@bot.command()
@commands.has_permissions(manage_roles=True)
async def give(ctx, member: discord.Member):
    role = ctx.guild.get_role(ROLE_ID)
    if role:
        await member.add_roles(role)
        await ctx.send(f"🪄 เสกยศ **{role.name}** ✅ ให้กับ {member.mention} เรียบร้อย!")
    else:
        await ctx.send("❌ หา ID ยศไม่เจอ ตรวจสอบเลข ROLE_ID ในโค้ดอีกทีครับ")

# --- 2. ระบบตอบแทนเมื่อโดนแท็ก (พร้อมปุ่มลิงก์) ---
@bot.event
async def on_message(message):
    if message.author == bot.user: return

    # เช็คว่ามีคนแท็ก ID ของคุณหรือไม่
    if f'<@{MY_ID}>' in message.content or f'<@!{MY_ID}>' in message.content:
        # สร้าง Embed
        embed = discord.Embed(
            description=f"🪴 สวัสดีครับ {message.author.mention}\n\n🌙 ขณะนี้เจ้าของไม่อยู่\n📩 สามารถทิ้งข้อความไว้หรือกดปุ่มติดต่อด้านล่างครับ",
            color=0x2f3136
        )
        embed.set_footer(text="Auto Response • Owner Offline")

        # สร้างปุ่มลิงก์ไปโปรไฟล์คุณ
        view = discord.ui.View()
        my_link = f"https://discord.com/users/1411888296270893251"
        button = discord.ui.Button(label="📩 ติดต่อเจ้าของเซิร์ฟเวอร์", url=my_link)
        view.add_item(button)

        await message.reply(embed=embed, view=view)

    # สำคัญมาก: ต้องมีบรรทัดนี้เพื่อให้คำสั่ง ! พิมพ์งานได้
    await bot.process_commands(message)

bot.run(TOKEN)
