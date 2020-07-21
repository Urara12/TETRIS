import pyxel
from random import randint

TILE_SIZE = 8
WINDOW_W = 14
WINDOW_H = 25


class App:
    def __init__(self):
        pyxel.init(WINDOW_W * TILE_SIZE, WINDOW_H *
                   TILE_SIZE, caption="tetris")

        self.blocks = [
            (1, 21 * TILE_SIZE, 0),
        ]
        self.ground = 21
        self.grounds = [
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
            21 * TILE_SIZE,
        ]

        self.tiles = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ]

        # 落ちてくるプロックの種類
        self.type = 1
        self.init()

        # 音楽
        pyxel.playm(0, loop=True)
        # ゲームの起動
        pyxel.load("tetlis.pyxres")
        pyxel.run(self.update, self.draw)

    def init(self):
        self.x = 5
        self.y = 0
        # self.type = randint(1,5)
        # self.type = 1

        self.GROUND_Y = self.ground * TILE_SIZE

    def update(self):
        # 自動落下の処理
        self.y += 0.5

        if self.type == 1 or self.type == 3:
            is_ground = False
            buttoms = []
            for index in range(self.x, self.x + 4):
                for i, row in enumerate(self.tiles):
                    if row[index] != 0:
                        buttoms.append(i)
                        break
                else:
                    buttoms.append(21)

            buttom = min(buttoms)

            # 一番下にきているかたしかめる
            if self.y > buttom * TILE_SIZE:
                is_ground = True

            if is_ground:
                is_ground = False
                # self.y = int(max_ground / TILE_SIZE)
                self.y = buttom
                block = (self.x, self.y, self.type)
                self.blocks.append(block)

                row = self.tiles[self.y - 1]
                if self.type == 1:
                    row[self.x] = 1
                    row[self.x + 1] = 1
                    row[self.x + 2] = 1
                    row[self.x + 3] = 1
                if self.type == 3:
                    row[self.x] = 2
                    row[self.x + 1] = 2
                    row[self.x + 2] = 2
                    row[self.x + 3] = 2

                # for i in range(self.x - 1, self.x + 3):
                #     self.grounds[i] = max_ground - 8

                self.init()

        # else:
        #     pass

        # 消える操作
        # 揃っている列があるか確かめる
        complete_row = []
        for i, row in enumerate(self.tiles):
            for index in range(1, 13):
                if row[index] < 1:
                    break
            else:
                complete_row.append(i)
        # 剃っている列があったら
        if len(complete_row) != 0:
            for i in complete_row:
                del self.tiles[i]
                complete_row.remove(i)
                self.tiles.insert(
                    0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                )
                for index in range(0, 12):
                    self.grounds[index] += 8

        # ボタンの操作
        # 下に落とす
        if pyxel.btn(pyxel.KEY_SPACE):
            self.y += 5 * TILE_SIZE
        # 左右に動かす
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
            if self.x > 9:
                self.x = 9
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
            if self.x < 1:
                self.x = 1
        # 形をかえる
        if pyxel.btnr(pyxel.KEY_ENTER):
            if self.type == 1:
                self.type = 2
            elif self.type == 2:
                self.type -= 1

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H)
        if self.type == 1:
            pyxel.bltm(self.x * TILE_SIZE, self.y, 0,
                       12 + self.type * 4, 0, 4, 2, 7)
        if self.type == 2:
            pyxel.bltm(self.x * TILE_SIZE, self.y, 0,
                       12 + self.type * 4, 0, 4, 4, 7)

        # 落ちてきてたまったやつを表示
        # offset = (pyxel.frame_count // 2) % 160
        # for i in range(2):
        #     for x, y, t in self.blocks:
        #         pyxel.bltm(x * TILE_SIZE, y, 0, 16 + t * 4, 0, 4, 4, 7)

        # tilesの反映　落ちてきたやつをうつしてる
        for row_i, row in enumerate(self.tiles):
            for tile_i, tile in enumerate(row):
                if tile == 1:
                    pyxel.blt(
                        tile_i * TILE_SIZE, row_i * TILE_SIZE + 16, 0, 16, 0, 8, 8, 0
                    )
                if tile == 2:
                    pyxel.blt(
                        tile_i * TILE_SIZE, row_i * TILE_SIZE + 16, 0, 24, 0, 8, 8, 0
                    )

        # pyxel.rect(0, self.GROUND_Y + 16, pyxel.width, pyxel.height, 4)


App()
