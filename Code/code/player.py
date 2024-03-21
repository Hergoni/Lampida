import datetime

import pygame

from entity import Entity
from controller import Controller
from screen import Screen
from switch import Switch
from keylistener import KeyListener


class Player(Entity):
    def __init__(self, screen: Screen, controller: Controller, x: int, y: int, keylistener: KeyListener,
                 ingame_time: datetime.timedelta = datetime.timedelta(seconds=0)) -> None:
        super().__init__(screen, x, y)
        self.keylistener = keylistener
        self.name = "Lucas"
        self.controller = controller
        self.inventory = None
        self.ingame_time: datetime.timedelta = ingame_time


        self.menu_option: bool = False

        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None
        self.change_map: Switch | None = None

    def update(self) -> None:
        self.update_ingame_time()
        self.check_input()
        self.check_move()
        super().update()

    def check_move(self) -> None:
        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            if self.keylistener.key_pressed(self.controller.get_key("left")):
                temp_hitbox.x -= 16
                if not self.check_collisions(temp_hitbox):
                    for switch in self.check_collisions_switchs(temp_hitbox):
                        self.change_map = switch
                    self.move_left()
                else:
                    self.direction = "left"
            elif self.keylistener.key_pressed(self.controller.get_key("right")):
                temp_hitbox.x += 16
                if not self.check_collisions(temp_hitbox):
                    for switch in self.check_collisions_switchs(temp_hitbox):
                        self.change_map = switch
                    self.move_right()
                else:
                    self.direction = "right"
            elif self.keylistener.key_pressed(self.controller.get_key("up")):
                temp_hitbox.y -= 16
                if not self.check_collisions(temp_hitbox):
                    for switch in self.check_collisions_switchs(temp_hitbox):
                        self.change_map = switch
                    self.move_up()
                else:
                    self.direction = "up"
            elif self.keylistener.key_pressed(self.controller.get_key("down")):
                temp_hitbox.y += 16
                if not self.check_collisions(temp_hitbox):
                    for switch in self.check_collisions_switchs(temp_hitbox):
                        self.change_map = switch
                    self.move_down()
                else:
                    self.direction = "down"

    def add_switchs(self, switchs: list[Switch]):
        self.switchs = switchs

    def check_collisions_switchs(self, temp_hitbox):
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collision(temp_hitbox):
                    self.change_map = switch
            return[]
        return []

    def add_collisions(self, collisions):
        self.collisions = collisions

    def check_collisions(self, temp_hitbox: pygame.Rect):
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False

    def check_input(self):
        if self.keylistener.key_pressed(self.controller.get_key("quit")):
            self.menu_option = True
            self.keylistener.remove_key(self.controller.get_key("quit"))
            return

    def update_ingame_time(self):
        if self.screen.get_delta_time() > 0:
            self.ingame_time += datetime.timedelta(seconds=self.screen.get_delta_time() / 1000)
