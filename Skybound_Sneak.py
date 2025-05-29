import pygame, sys
from config import *
from logic import game_loop_logic
from init import init_game
from background import *
from enemy import *
from player import *
from platforms import *
from menu import run_game

if __name__ == "__main__":
    run_game(screen)