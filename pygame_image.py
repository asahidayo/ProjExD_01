import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ProjeExD2023/ex01/fig/pg_bg.jpg")
    img_tori=pg.image.load("ProjeExD2023/ex01/fig/3.png")
    img_tori=pg.transform.flip(img_tori,True,False)
    img_utori=pg.transform.rotozoom(img_tori,10,1.0)
    img_uutori=pg.transform.rotozoom(img_utori,5,1.0)
    bg_bimg=pg.transform.flip(bg_img,True,False)
    tmr = 0
    tori=[img_tori,img_uutori,img_utori]
    #bg=[bg_bimg,bg_img]
    x=0
    count=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        #screen.blit(bg_img,[1600-x,0])
        
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_bimg,[1600-x,0])
        screen.blit(tori[tmr%3],[300,200])
        
        
        
        pg.display.update()
        
        tmr += 1 
        
        x+=5
        #if x==1600:
           # count+=1
           # x-=800
        #if x==1599:
            #screen.blit(bg_bimg,[-x,0])
            #screen.blit(bg_bimg,[1600-x,0])
       
        
        
        

        clock.tick(50)
        #move_ip


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()