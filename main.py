def direction(facing, turn):
        if (turn % 45) or (turn < -1080) or (turn > 1080):
                raise ValueError("Turn should be multiple by 45, between -1080 and 1080")
        
        directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
        if facing not in directions:
                raise ValueError(f"Facing should be some of these {directions}")

        direction_index = directions.index(facing)
        turn_index = turn // 45
        # assigning direction_index the index after turning
        direction_index = (direction_index + turn_index) % 8

        return directions[direction_index]