async def draw_human(head_level, body_level, arms_level, legs_level):
    return (
        f"  o   (head: {head_level:.2f})\n"
        f"  /|\\  (arms: {arms_level:.2f})\n"
        f"   |   (body: {body_level:.2f})\n"
        f"  / \\  (legs: {legs_level:.2f})"
    )
