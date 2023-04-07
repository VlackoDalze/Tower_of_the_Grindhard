import pygame
import random
import scripts.setting as setting

class Music:
    def __init__(self, musics_url_list:[] = setting.background_music_list, volume: int = 1):
        self.volume = volume
        self.musics_url_list = musics_url_list

    # Método que primero verifica si hay una música reproduciéndose en caso negativo, reproducirá unas de las 2 músicas de manera aleatorias
    def play_random_background_music(self):
        if not (pygame.mixer.music.get_busy()):
            music_option_random = random.randint(0, (len(self.musics_url_list)-1))
            pygame.mixer.music.set_volume(setting.volume)

            pygame.mixer.music.load(self.musics_url_list[music_option_random])

            pygame.mixer.music.play()
