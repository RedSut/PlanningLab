from envs.obsgrid_env import ObsGrid

class LeftFrozenLakeEnv(ObsGrid):
    """
    Frozen lake involves going from Start(S) to Goal(G) without falling into any Holes(H) by walking over the Frozen(F) lake. 
    The agent's actions are fully deterministic.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "F", "F", "F", "F", "F"],
                ["F", "W", "W", "W", "W", "F"],
                ["F", "W", "G", "F", "F", "F"],
                ["F", "W", "F", "F", "F", "W"],
                ["F", "W", "F", "W", "F", "F"],
                ["F", "W", "F", "F", "F", "F"],
                ["F", "F", "F", "F", "W", "F"],
            ]
        rewards = {"S": 0.0, "F": 0.0, "G": 1}
        actdyn = {0: {0: 1.0}, 1: {1: 1.0}, 2: {2: 1.0}, 3: {3: 1.0}}
        super().__init__(actions, grid, actdyn, rewards)

        
class BigFrozenLakeEnv(ObsGrid):
    """
    Frozen lake involves going from Start(S) to Goal(G) avoiding walls(W) by walking over the Frozen(F) lake. 
    The agent's actions are fully deterministic.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [["S", "W", "F", "F", "F", "F", "W", "F"],
                ["F", "W", "F", "W", "F", "F", "F", "F"],
                ["F", "F", "W", "W", "F", "F", "F", "F"],
                ["W", "F", "F", "F", "F", "W", "F", "F"],
                ["F", "F", "F", "W", "F", "F", "F", "W"],
                ["F", "W", "W", "F", "W", "F", "W", "F"],
                ["F", "W", "F", "F", "W", "F", "W", "F"],
                ["F", "F", "F", "W", "F", "F", "F", "G"]
            ]
        rewards = {"S": 0.0, "F": 0.0, "G": 1}
        actdyn = {0: {0: 1.0}, 1: {1: 1.0}, 2: {2: 1.0}, 3: {3: 1.0}}
        super().__init__(actions, grid, actdyn, rewards)
        
        
class SlipperyFrozenLakeEnv(ObsGrid):
    """
    Frozen lake involves going from Start(S) to Goal(G) without falling into any Holes(H) by walking over the Frozen(F) lake. 
    The agent may not always move in the intended direction due to the slippery nature of the frozen lake.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "F", "F", "F"],
                ["F", "H", "F", "H"],
                ["F", "F", "F", "H"],
                ["H", "F", "F", "G"]
            ]
        rewards = {"S": -0.04, "F": -0.04, "H": -0.2, "G": 1}
        actdyn = {0: {0: 0.5, 2: 0.25, 3: 0.25, 1: 0.0}, 1: {1: 0.5, 2: 0.25, 3: 0.25, 0: 0.0}, 2: {2: 0.5, 1: 0.25, 0: 0.25,
                  3: 0.0}, 3: {3: 0.5, 0: 0.25, 1: 0.25, 2: 0.0}}
        super().__init__(actions, grid, actdyn, rewards)
        
        
class ModifiableFrozenLakeEnv(ObsGrid):
    """
    Frozen lake involves going from Start(S) to Goal(G) without falling into any Holes(H) by walking over the Frozen(F) lake. 
    The agent may not always move in the intended direction due to the slippery nature of the frozen lake.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["S", "F", "F", "F"],
                ["F", "H", "F", "H"],
                ["F", "F", "F", "H"],
                ["H", "F", "F", "G"]
            ]
        rewards = {"S": -0.04, "F": -0.04, "H": -0.2, "G": 1}
        actdyn = {0: {0: 0.5, 2: 0.25, 3: 0.25, 1: 0.0}, 1: {1: 0.5, 2: 0.25, 3: 0.25, 0: 0.0}, 2: {2: 0.5, 1: 0.25, 0: 0.25,
                  3: 0.0}, 3: {3: 0.5, 0: 0.25, 1: 0.25, 2: 0.0}}
        super().__init__(actions, grid, actdyn, rewards)