#Partie non terminé
import pygame
from keylistener import KeyListener
from map import Map
from player import Player
from screen import Screen
from controller import Controller
from option import Option
from map import Map


class Event:
    def __init__(self, screen: Screen, player_rect: pygame.Rect, objective1_rect: pygame.Rect, font):
        self.screen = screen
        self.player_rect = player_rect
        self.objective1_rect = objective1_rect
        self.font = font
        self.objective1_reached = False




