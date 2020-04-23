# -*- coding: utf-8 -*-
import pyxel

WINDOW_H = 120
WINDOW_W = 150

class App:
    def __init__(self):
        self.IMG_ID0 = 0 #クレーン
        self.IMG_ID1 = 1 #下の白ネコ
        self.IMG_ID1 = 1 #下の黒ネコ
        #windowの設定(幅、高さ、名前)
        pyxel.init(WINDOW_W, WINDOW_H, caption="RetroGame2", fps=3)
        #pyxeleditorのRetroRPGgame.pyxresを挿入
        #pyxeleditorで作った画像はimage(0)になる
        pyxel.load("RetroRPGgame.pyxres")
        pyxel.image(1).load(0, 0, "cat_w.png")
        pyxel.image(2).load(0, 0, "cat_m.gif")
        #Falseにするとマウス非表示
        pyxel.mouse(False)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(3)
        pyxel.text(40, 51, "UFO catcher Game!", pyxel.frame_count % 16)

        pyxel.line(0, 2, 150, 2, 5)

        #0-0:close #32-0:open
        pyxel.blt(pyxel.frame_count % pyxel.width, 3, 0, 32*(pyxel.frame_count % 2), 0, 32, 32, 0)

        pyxel.blt(-15, 77, 1, 0, 0, 32, 32, 0)
        pyxel.blt(15, 77, 2, 0, 0, 32, 32, 0)
        pyxel.blt(47, 77, 1, 0, 0, 32, 32, 0)
        pyxel.blt(79, 77, 2, 0, 0, 32, 32, 0)
        pyxel.blt(110, 77, 1, 0, 0, 32, 32, 0)
        pyxel.blt(140, 77, 2, 0, 0, 32, 32, 0)

        pyxel.blt(0, 96, 1, 0, 0, 32, 32, 0)
        pyxel.blt(32, 96, 2, 0, 0, 32, 32, 0)
        pyxel.blt(64, 96, 1, 0, 0, 32, 32, 0)
        pyxel.blt(96, 96, 2, 0, 0, 32, 32, 0)
        pyxel.blt(128, 96, 1, 0, 0, 32, 32, 0)

App()
