# import the module
import python_weather
import asyncio
import os

weather_emojis = {
    "☀️": "norm",  # Soleil
    "⛅️": "norm",  # Nuage avec soleil
    "☁️": "norm",  # Nuage
    "🌤️": "norm",  # Nuage avec soleil voilé
    "🌥️": "norm",  # Nuage avec soleil voilé
    "🌦️": "norm",  # Nuage avec pluie
    "🌧️": "rain",  # Pluie
    "⛈️": "rain",  # Orage
    "🌩️": "rain",  # Éclair
    "🌨️": "snow",  # Neige
    "❄️": "snow",  # Flocon de neige
    "🌫️": "norm",  # Brouillard
    "🌪️": "norm",  # Tornade
    "🌊": "norm",  # Vague
    "🌬️": "norm",  # Vent soufflant vers la gauche
    "💨": "norm",  # Vent soufflant vers la droite
    "🌀": "norm",  # Cyclone
    "🌈": "norm",  # Arc-en-ciel
    "☔": "rain",  # Parapluie avec gouttes de pluie
    "☂️": "rain",  # Parapluie
    "⚡": "rain",  # Éclair
    "🌁": "norm",  # Brouillard sur pont
    "🌉": "norm",  # Pont de nuit
    "🌌": "norm",  # Voie lactée
    "🌠": "norm",  # Étoile filante
    "🎇": "norm",  # Feu d'artifice
    "🔥": "norm",  # Feu
    "❌": "norm",  # Zone de danger
    "☣️": "norm",  # Symbole de danger biologique
    "☢️": "norm",  # Symbole de danger radioactif
    "🔆": "norm",  # Soleil avec rayons
    "🔅": "norm",  # Soleil avec petits rayons
    "🌍": "norm",  # Globe terrestre montrant l'Europe et l'Afrique
    "🌎": "norm",  # Globe terrestre montrant l'Amérique
    "🌏": "norm",  # Globe terrestre montrant l'Asie et l'Australie
    "🌐": "norm",  # Globe terrestre avec méridiens et parallèles
    "🌋": "norm",  # Volcan
    "🗻": "norm",  # Mont Fuji
    "🏔️": "norm",  # Montagne enneigée
    "🏕️": "norm",  # Camping
    "🏖️": "norm",  # Plage avec parasol
    "✨": "norm",
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
                    try:
                        return weather_emojis[f'{hourly.type!r}']
                    except:
                        return "norm"



if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather())