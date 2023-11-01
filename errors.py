class pathfinder_error(Exception):
    "Pathfinder could not find a continous path"

    def __init__(self, message="Pathfinder could not find a continous path"):
        self.message = message
        super().__init__(self.message)