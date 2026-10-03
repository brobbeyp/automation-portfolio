# Practice example: flag actions that need approval.
# Keyword matching is only a learning exercise.
def assess_action(action):
    risky_words = ["delete", "send", "buy", "pay"]
    action = action.lower().replace(",", " ").replace("!", " ").strip()
    if action == "":
        return "invalid"
    elif any(word in action.split() for word in risky_words):
        return "approval required"
    else:
        return "safe to plan"
