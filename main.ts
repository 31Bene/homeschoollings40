let Menschen = 0
let i = 0
basic.forever(function () {
    basic.showString("" + Menschen)
    while (input.lightLevel() >= 240 && i == 0) {
        music.playMelody("C5 E D A F D G B ", 400)
        Menschen += 1
        i = 1
    }
    if (input.lightLevel() <= 200) {
        i = 0
    }
})
