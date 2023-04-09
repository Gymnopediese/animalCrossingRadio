# import the module
import python_weather
import asyncio
import os

weather_emojis = {
    "☀️": "NORMAL",  # Soleil
    "⛅️": "NORMAL",  # Nuage avec soleil
    "☁️": "NORMAL",  # Nuage
    "🌤️": "NORMAL",  # Nuage avec soleil voilé
    "🌥️": "NORMAL",  # Nuage avec soleil voilé
    "🌦️": "NORMAL",  # Nuage avec pluie
    "🌧️": "RAINY",  # Pluie
    "⛈️": "RAINY",  # Orage
    "🌩️": "RAINY",  # Éclair
    "🌨️": "SNOWY",  # Neige
    "❄️": "SNOWY",  # Flocon de neige
    "🌫️": "NORMAL",  # Brouillard
    "🌪️": "NORMAL",  # Tornade
    "🌊": "NORMAL",  # Vague
    "🌬️": "NORMAL",  # Vent soufflant vers la gauche
    "💨": "NORMAL",  # Vent soufflant vers la droite
    "🌀": "NORMAL",  # Cyclone
    "🌈": "NORMAL",  # Arc-en-ciel
    "☔": "RAINY",  # Parapluie avec gouttes de pluie
    "☂️": "RAINY",  # Parapluie
    "⚡": "RAINY",  # Éclair
    "🌁": "NORMAL",  # Brouillard sur pont
    "🌉": "NORMAL",  # Pont de nuit
    "🌌": "NORMAL",  # Voie lactée
    "🌠": "NORMAL",  # Étoile filante
    "🎇": "NORMAL",  # Feu d'artifice
    "🔥": "NORMAL",  # Feu
    "❌": "NORMAL",  # Zone de danger
    "☣️": "NORMAL",  # Symbole de danger biologique
    "☢️": "NORMAL",  # Symbole de danger radioactif
    "🔆": "NORMAL",  # Soleil avec rayons
    "🔅": "NORMAL",  # Soleil avec petits rayons
    "🌍": "NORMAL",  # Globe terrestre montrant l'Europe et l'Afrique
    "🌎": "NORMAL",  # Globe terrestre montrant l'Amérique
    "🌏": "NORMAL",  # Globe terrestre montrant l'Asie et l'Australie
    "🌐": "NORMAL",  # Globe terrestre avec méridiens et parallèles
    "🌋": "NORMAL",  # Volcan
    "🗻": "NORMAL",  # Mont Fuji
    "🏔️": "NORMAL",  # Montagne enneigée
    "🏕️": "NORMAL",  # Camping
    "🏖️": "NORMAL",  # Plage avec parasol
    "✨": "NORMAL",
}
async def getweather(time = 18):
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(format=python_weather.METRIC) as client:

        # fetch a weather forecast from a city
        weather = await client.get("Geneve")

        for forecast in weather.forecasts:
            for hourly in forecast.hourly:
                if hourly.time.hour >= time:
                    print(weather_emojis[f'{hourly.type!r}'])
                    return weather_emojis[f'{hourly.type!r}']



if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather())