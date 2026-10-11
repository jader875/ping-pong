from pygame import *



class gameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(gameSprite):
    def update(self):
        var = key.get_pressed()
        if var[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if var[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

    def update2(self):
        var = key.get_pressed()
        if var[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if var[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
        

window = display.set_mode((700,500))
window.fill((47, 158, 154))
clock = time.Clock()
FPS = 60

platform = Player('палка.png',20,200,50,150,6)
platform2 = Player('палка.png',620,200,50,150,6)
ball = gameSprite('мячик.png',200,200,30,30,4)



game = True
finish = False 
xball = 3
yball = 3
font.init()
foont = font.SysFont('Arial',40)
text1 = foont.render('Player 1 lost!',True,(74, 65, 42))
text2 = foont.render('Player 2 lost!',True,(74, 65, 42))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    
    if finish != True:
        window.fill((47, 158, 154))
        platform.update()
        platform2.update2()
        ball.rect.x += xball
        ball.rect.y += yball
        if ball.rect.y < 0 or ball.rect.y > 470:
            yball *= -1
        if sprite.collide_rect(platform,ball):
            xball *= -1
            if xball < 0:
                xball -= 0.2
            if xball > 0:
                xball += 0.2
        if sprite.collide_rect(platform2,ball):
            xball *= -1
            if xball < 0:
                xball -= 0.2
            if xball > 0:
                xball += 0.2
        if ball.rect.x <= 0:
            window.blit(text1,(250,250))
        if ball.rect.x >= 700:
            window.blit(text2,(250,250))
        
        platform.reset()
        platform2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
    
    

