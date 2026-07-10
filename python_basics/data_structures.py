def list_demo(tasks=None):
    if tasks is not None and not isinstance(tasks, list):
        raise TypeError("tasks must be a list or None")
    tasks = tasks or ["wake up", "eat", "sleep", "repeat"]
    tasks.append("code")
    tasks.extend(["debug", "deploy"])
    tasks.insert(0, "first task")
    return tasks

def tuple_demo(coords=None):
    if coords is not None and not (isinstance(coords, tuple) and len(coords) == 2 and all(isinstance(c, (int, float)) for c in coords)):
        raise TypeError("coords must be a tuple of two numbers or None")
    coords = coords or (40.7128, -74.0060)
    return {
        "original": coords, "x": coords[0], "y": coords[1],
        "concat": coords + ("Extra Data",),
        "count_20": (10, 20, 30, 20).count(20),
        "nested": (coords, (1, 2, 3))
    }

def set_demo(user_ids=None):
    if user_ids is not None and not (isinstance(user_ids, list) and all(isinstance(u, int) for u in user_ids)):
        raise TypeError("user_ids must be a list of integers or None")
    s = set(user_ids or [101, 102, 103, 101])
    initial = s.copy()
    s.update([104, 105, 106])
    s.discard(102)
    return {"initial": initial, "final": s, "has_101": 101 in s, "union": s | {999, 1000}}

def dict_demo(username="coder99", score=500):
    if not isinstance(username, str):
        raise TypeError("username must be a string")
    if not isinstance(score, int):
        raise TypeError("score must be an integer")
    user = {"username": username, "score": score, "is_premium": False}
    user["score"] += 100
    user["level"] = 5
    user["role"] = user.get("role", "standard_user")
    user.pop("is_premium", None)
    return user

if __name__ == "__main__":
    print(f"List: {list_demo()}")
    print(f"Tuple: {tuple_demo()}")
    print(f"Set: {set_demo()}")
    print(f"Dict: {dict_demo()}")
