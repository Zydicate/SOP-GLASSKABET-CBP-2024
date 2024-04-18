import sys
import pygame

class CutScene:
    def __init__(self, name, text, backgrounds):
        self.name = name
        self.text = text
        self.backgrounds = backgrounds
        self.step = 0
        self.text_counter = 0
        self.space_pressed = False
        self.cut_scene_running = True

    def update(self):
        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]
        if space and not self.space_pressed:
            self.space_pressed = True
            if self.step < len(self.text) - 1:
                self.step += 1
                self.text_counter = 0
            else:
                self.cut_scene_running = False
        elif not space:
            self.space_pressed = False

        if int(self.text_counter) < len(self.text[self.step]):
            self.text_counter += 0.4

        return self.cut_scene_running

    def draw(self, screen):
        Glasskabet.draw_text(screen, self.text[self.step][0:int(self.text_counter)],
                             40, (255, 255, 255), 40, 40)

    def get_current_background(self):
        return self.backgrounds[self.step]

class CutSceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.cut_scenes = {
            'intro': CutScene('intro',
                              ["Mr. Seyfert, en kold og egoistisk forretningsmand, er nu blevet enkemand...", #1
                               "Ægteskabskontrakten nævner at så snart Ms.Seyfert er 'BEGRAVET'",#2
                               "skal formuen gå til hendes familie...", #3
                               "Men Mr.Seyfert har fundet en vej rundt om dette..",#4
                               "Ved ikke at lade Ms.Seyfert 'BEGRAVE' igennem Glasskabet...", #5
                              "en række af spekulationer har i de seneste år ledt ham til store tab...",#6
                               "han er nu NØD til at tilvejebringe en sum a 40.000 pund ellers...", #7
                               "vil han møde konsekvenserne af sine handlinger...", #8
                               "GLASSKABET AF B.S. INGEMANN (UNFINISHED)" #9



                                  ,],

                              ["img/DALLE COVER GLASSKABET.jpg", #1
                               "img/DALLE COVER GLASSKABET.jpg", #2
                               "img/DALLE COVER GLASSKABET.jpg",#3
                               "img/CLOSEUPMRSEYFERT.jpg", #4
                               "img/CLOSEUPMRSEYFERT.jpg", #5
                               "img/DALLESEYFERTSEARCH.jpg", #6
                               "img/DALLESEYFERTSEARCH.jpg", #7
                               "img/DALLEMRSEYFERTCHAINED.jpg", #8
                               "img/DALLEMRSEYFERTSIND.jpg" #9

                               ]),
        }
        self.current_cutscene = None
        self.cut_scene_running = False

    def start_cut_scene(self, scene_name):
        if scene_name in self.cut_scenes:
            self.current_cutscene = self.cut_scenes[scene_name]
            self.cut_scene_running = True

    def update(self):
        if self.cut_scene_running:
            self.cut_scene_running = self.current_cutscene.update()

    def draw(self):
        if self.cut_scene_running:
            self.current_cutscene.draw(self.screen)

class Glasskabet:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.cutscene_manager = CutSceneManager(self.display)
        self.cutscene_manager.start_cut_scene('intro')


    def draw_text(screen, text, size, color, x, y):
        font = pygame.font.SysFont("bodoni", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.cutscene_manager.cut_scene_running:
                background_path = self.cutscene_manager.current_cutscene.get_current_background()
                intro_background = pygame.image.load(background_path)
                intro_background = pygame.transform.scale(intro_background, (self.width, self.height))
                self.display.blit(intro_background, (0, 0))

            self.cutscene_manager.update()
            self.cutscene_manager.draw()
            pygame.display.update()

def main():
    game = Glasskabet(1280, 720)
    game.run()

if __name__ == '__main__':
    main()
