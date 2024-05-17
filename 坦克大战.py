import turtle
import random
import math
import time

# 设置屏幕
wn = turtle.Screen()
wn.title("坦克大战")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# 创建玩家坦克
player = turtle.Turtle()
player.shape("square")
player.color("green")
player.shapesize(stretch_wid=2, stretch_len=2)  # 使坦克为正方形
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)  # 坦克面朝上方

# 创建玩家子弹
player_bullet = turtle.Turtle()
player_bullet.color("red")
player_bullet.shape("circle")
player_bullet.penup()
player_bullet.speed(0)
player_bullet.shapesize(0.5, 0.5)
player_bullet.hideturtle()

# 玩家子弹状态
player_bullet_state = "ready"

# 创建敌人坦克
enemy = turtle.Turtle()
enemy.color("blue")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.shapesize(stretch_wid=2, stretch_len=2)  # 使坦克为正方形
enemy.goto(0, 250)
enemy.setheading(270)  # 敌人坦克面朝下方

# 创建敌人子弹
enemy_bullet = turtle.Turtle()
enemy_bullet.color("yellow")
enemy_bullet.shape("circle")
enemy_bullet.penup()
enemy_bullet.speed(0)
enemy_bullet.shapesize(0.5, 0.5)
enemy_bullet.hideturtle()

# 敌人子弹状态
enemy_bullet_state = "ready"

# 移动玩家坦克
def move_forward():
    player.forward(20)

def move_backward():
    player.backward(20)

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

# 发射玩家子弹
def fire_player_bullet():
    global player_bullet_state
    if player_bullet_state == "ready":
        player_bullet_state = "fire"
        x, y = player.position()
        player_bullet.setposition(x, y)
        player_bullet.setheading(player.heading())
        player_bullet.showturtle()

# 移动玩家子弹
def move_player_bullet():
    global player_bullet_state
    if player_bullet_state == "fire":
        player_bullet.forward(20)
    
    if player_bullet.ycor() > 275 or player_bullet.ycor() < -275 or player_bullet.xcor() > 275 or player_bullet.xcor() < -275:
        player_bullet.hideturtle()
        player_bullet_state = "ready"

# 敌人自动开火
def auto_fire_enemy_bullet():
    global enemy_bullet_state
    if enemy_bullet_state == "ready":
        enemy_bullet_state = "fire"
        x, y = enemy.position()
        enemy_bullet.setposition(x, y)
        enemy_bullet.setheading(enemy.heading())
        enemy_bullet.showturtle()

# 移动敌人子弹
def move_enemy_bullet():
    global enemy_bullet_state
    if enemy_bullet_state == "fire":
        enemy_bullet.forward(20)
    
    if enemy_bullet.ycor() > 275 or enemy_bullet.ycor() < -275 or enemy_bullet.xcor() > 275 or enemy_bullet.xcor() < -275:
        enemy_bullet.hideturtle()
        enemy_bullet_state = "ready"

# 敌人自动瞄准玩家
def auto_aim():
    dx = player.xcor() - enemy.xcor()
    dy = player.ycor() - enemy.ycor()
    angle = math.atan2(dy, dx)
    angle = math.degrees(angle)
    enemy.setheading(angle + 90)

# 键盘绑定
wn.listen()
wn.onkeypress(move_forward, "Up")
wn.onkeypress(move_backward, "Down")
wn.onkeypress(turn_left, "Left")
wn.onkeypress(turn_right, "Right")
wn.onkeypress(fire_player_bullet, "space")

# 主游戏循环
while True:
    wn.update()
    move_player_bullet()
    move_enemy_bullet()
    auto_aim()
    if random.randint(1, 20) == 1:  # 随机决定是否开火
        auto_fire_enemy_bullet()
    time.sleep(0.1)  # 控制游戏更新速度