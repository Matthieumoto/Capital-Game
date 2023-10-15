#importtation de toutes les bibliothèques
import pygame
from pygame.locals import *
from flask import Flask, render_template
import sys
import random
import json
import time
import os


class Settings:
    """Classe qui contient tout les paramètres nécessaire à l'exécution du jeu"""
    def __init__(self):
        self.HEIGHT = 800
        self.WIDTH = 1600
        self.ACC = 1
        self.FRIC = -0.12
        self.FPS = 60
        