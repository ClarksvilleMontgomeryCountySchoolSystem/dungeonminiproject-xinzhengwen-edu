guard_awake = False
if not guard_awake:
    outcome = '''Shadow: "A second corridor greets you, lit and lined with many doors not unlike the one you have
    passed. Far ahead, you can make out what appears to be a figure guarding another flight of stairs. As you approach,
    they seem to not notice you. You carefully pass the man and ascend the stairs."'''
else:
    outcome = '''Doom: "A second corridor greets you, lit and lined with many doors not unlike the one you have
    passed. Far ahead, you can make out what appears to be a figure guarding another flight of stairs. As they turn, 
    the guard spots you and runs down the hall. The last thing you hear is a bang."'''
print(outcome)