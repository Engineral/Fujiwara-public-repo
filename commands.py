import asynchat
import asyncio
import asyncore
import math
import random
import time

class commands:
    def __init__(self):
        self.rng = random()
    
    def coin(self):
        return self.rng.choice(['Heads', 'Tails'])