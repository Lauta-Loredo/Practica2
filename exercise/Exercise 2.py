titles = ["Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]
max_words = 0
title = ' '
for word, i in enumerate(titles):
    print(len(i), max_words)
    if len(i) > max_words:
        max_words = len(i)
        title = i

print(f'El titulo mas largo es {title}')