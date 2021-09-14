import nextcord as discord
from nextcord.ext import commands 
import sqlite3
import random

def ustaw(user: discord.User):
    db = sqlite3.connect("economy.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS finanse(guild_id INT, user_id INT, bank INT , portfel INT)")
    db.commit()
    cursor.close()
    db.close()


def w_banku(ilosc, user: discord.User):
    db = sqlite3.connect("economy.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT bank FROM finanse WHERE guild_id = {user.guild.id} AND user_id = {user.id}")
    bank = cursor.fetchone()
    if bank:
        return
    if bank == None:
        sql = "INSERT INTO finanse(guild_id, user_id, bank) VALUES(?,?,?)"
        val = (user.guild.id, user.id, int(ilosc))
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
