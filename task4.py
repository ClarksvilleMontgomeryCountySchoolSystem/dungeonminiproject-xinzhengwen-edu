drawbridge_raised = False
if not drawbridge_raised:
    outcome = '''Thunder: "You meet another door. Past it lies an great chasm and another immense wall. You cannot
    see where they end. As you walk along the edge, you spot a narrow drawbridge, leading to a small doorway, spanning
    the gap. Fortunately, it is lowered, and you cross the bridge."'''
else:
    outcome = '''Doom: "You meet another door. Past it lies an great chasm and another immense wall. You cannot
    see where they end. As you walk along the edge, you spot a narrow drawbridge, leading to a small doorway, spanning
    the gap. It is raised, so you continue walking. You walk for days. You cannot find another bridge."'''
print(outcome)