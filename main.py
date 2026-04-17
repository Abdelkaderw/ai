import discord
import requests

TOKEN = "MTQ5NDM0NjAzOTcxNTY5NjcwMA.GKAzdb.OjwWn6tfEVFb3gbZY8wDoO9OpeAzOdXepp-Uxk"
API_KEY = "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"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def ask_ai(message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        reply = ask_ai(message.content)
        await message.channel.send(reply)
    except Exception as e:
        print("Erreur :", e)
        await message.channel.send("Erreur avec l'IA 😅")

client.run(TOKEN)