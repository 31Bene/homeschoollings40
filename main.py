Menschen = 0
i = 0
def on_forever():
    global Menschen
    global i
    basic.show_string("" + str((Menschen)))
    while input.light_level() >= 240 and i == 0:
        music.play_melody("C5 E D A F D G B ", 400)
        Menschen += 1
        i = 1
    if input.light_level() <= 200:
        i = 0
basic.forever(on_forever)