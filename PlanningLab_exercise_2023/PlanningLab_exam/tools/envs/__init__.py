"""
OpenAI Gym environments designed for the AI lab course
"""

from gym.envs.registration import register
from envs.maze_env import *
from envs.lava_env import *
from envs.frozen_lake_env import *

register(
    id='SmallMaze-v0',
    entry_point='envs:SmallMazeEnv')
register(
    id='GrdMaze-v0',
    entry_point='envs:GrdMazeEnv')
register(
    id='BlockedMaze-v0',
    entry_point='envs:BlockedMazeEnv')
register(
    id='LavaFloor-v0',
    entry_point='envs:LavaFloorEnv')
register(
    id='VeryBadLavaFloor-v0',
    entry_point='envs:VeryBadLavaFloorEnv')
register(
    id='NiceLavaFloor-v0',
    entry_point='envs:NiceLavaFloorEnv')
register(
    id='BiggerLavaFloor-v0',
    entry_point='envs:BiggerLavaFloorEnv')
register(
    id='HugeLavaFloor-v0',
    entry_point='envs:HugeLavaFloorEnv')
register(
    id='LeftFrozenLakeEnv-v0',
    entry_point='envs:LeftFrozenLakeEnv')
register(
    id='BigFrozenLakeEnv-v0',
    entry_point='envs:BigFrozenLakeEnv')
register(
    id='SlipperyFrozenLakeEnv-v0',
    entry_point='envs:SlipperyFrozenLakeEnv')
register(
    id='ModifiableFrozenLakeEnv-v0',
    entry_point='envs:ModifiableFrozenLakeEnv')