import nextcord as discord
from nextcord.ext import commands 
import sqlite3
import random

def ustaw():
    db = sqlite3.connect("economy.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS finanse(guild_id STR, user_id INT, bank INT , portfel INT)")
    db.commit()
    cursor.close()
    db.close()


def na_start(ilosc, ilosc2, user: discord.User):
    
    db = sqlite3.connect("economy.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM finanse WHERE guild_id = {user.guild.id} AND user_id = {user.id}")
    bank = cursor.fetchone()
    if bank:
        return
    if bank == None:
        sql = "INSERT INTO finanse(guild_id, user_id, bank, portfel) VALUES(?,?,?,?)"
        val = (user.guild.id, user.id, int(ilosc), int(ilosc2))
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()

