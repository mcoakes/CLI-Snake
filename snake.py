import os
import random

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_input(current):
    inp = input("> ").strip().lower()
    if inp == "":
        return current
    if inp in ("w", "s", "a", "d", "q"):
        return inp
    print("Use w=up, a=left, s=down, d=right, q=quit.")
    input("Press enter to continue")
    return current

class Game:
    def __init__(self, board_length=10, board_height=10,  snake_length=3):
        self.board = Board(board_length, board_height)
        self.snake = Snake(snake_length, self.board)
        self.score = 0

        if self.board.food in self.snake.tiles:
            r, c = self.board.food
            self.board.tiles[r][c] = 0
            self.board.food = self.board.new_apple(self.snake)
            r, c = self.board.food
            self.board.tiles[r][c] = 1

    def print(self):
        self.board.print(self.snake, self.score)
    def start(self):
        while True:
            self.print()
            direction = get_input(self.snake.direction)
            self.snake.direction = direction
            if direction == "q":
                print(f"Quitting.  Final Score: {self.score}")
                break

            new_head = self.snake.step()

            if not self.board.in_bounds(new_head) or new_head in self.snake.tiles:
                self.print()
                print("Game Over!")
                break

            self.snake.tiles.insert(0, new_head)

            if new_head == self.board.food:
                self.score += 1
                old_r, old_c = self.board.food
                self.board.tiles[old_r][old_c] = 0
                self.board.food = self.board.new_apple(self.snake.tiles)
                if not self.board.food:
                    print("Congrats!  You filled the entire board!")
                    break
                new_r, new_c = self.board.food
                self.board.tiles[new_r][new_c] = 1
            else:
                self.snake.tiles.pop()





class Board:
    def __init__(self, length=10, height=10):
        self.tiles=[[0 for i in range(length)] for j in range(height)]
        self.food = self.new_apple()
        r, c = self.food
        self.tiles[r][c] = 1


    def __repr__(self):
        height = len(self.tiles)
        length = len(self.tiles[0])
        return f"Board({length}, {height})"

    def new_apple(self, snake_tiles=[]):
        coords = [(r,c) for r in range (self.height)
                     for c in range(self.length) if (r,c) not in snake_tiles]
        return random.choice(coords) if coords else None

    def in_bounds(self,cell):
        r, c = cell
        return 0 <= r < self.height and 0 <= c < self.length


    def print(self, snake, score):
        clear_screen()
        print(f"Score: {score}")
        print(" " + "=" * self.length)
        for r in range(self.height):
            print("|", end="")
            for c in range(self.length):
                if (r,c) == snake.tiles[0]:
                   print("@", end="")
                elif (r,c) in snake.tiles:
                    print("o", end="")
                elif self.tiles[r][c] == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("|")
        print(" " + "=" * self.length)

    @property
    def length(self):
        return len(self.tiles[0])

    @property
    def height(self):
       return len(self.tiles)

class Snake:
    def __init__(self, length, board):
        self.length = length
        self.board = board
        self.tiles = []
        self.direction = random.choice(["w","s","a","d"])
        self.spawn()
    def calculate_min_and_max_pos(self):
        min_r = 0
        min_c = 0
        max_r = self.board.height - 1
        max_c = self.board.length - 1

        if self.direction == "w":
            max_r -= self.length
        elif self.direction == "s":
            min_r += self.length
        elif self.direction == "a":
            max_c -= self.length
        elif self.direction == "d":
            min_c += self.length

        return min_r, min_c, max_r, max_c

    def spawn(self):
        min_r, min_c, max_r, max_c = self.calculate_min_and_max_pos()
        r = random.randint(min_r, max_r)
        c = random.randint(min_c, max_c)
        while self.board.tiles[r][c] == 1:
            r = random.randint(min_r, max_r)
            c = random.randint(min_c, max_c)

        self.tiles.append((r,c))

        deltas = {"w": (1,0), "s": (-1,0) , "a": (0,1), "d": (0,-1) }
        for i in range(1,self.length):
            d = deltas[self.direction]
            dr = d[0] * i + self.tiles[0][0]
            dc = d[1] * i + self.tiles[0][1]
            self.tiles.append((dr,dc))

    def step(self):
        deltas = {"w": (-1,0), "s": (1,0) , "a": (0,-1), "d": (0,1) }
        dr, dc = deltas[self.direction]
        head_r, head_c = self.tiles[0]
        new_head = (head_r + dr, head_c + dc)
        return new_head

if __name__ == "__main__":
    G = Game()
    G.start()
 
