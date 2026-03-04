torch_lit = True
if torch_lit:
    outcome = '''Flicker: "You wake to the feeling of cold stone against your face. It is too dark to see. You fumble 
    around for your light, and manage to find it. Bright light stretches across the pallid walls, and you find yourself 
    in a narrow, stone corridor. On one end there lies a long staircase. You cannot see the other end. The light does 
    not reach. You decide to ascend the stairs."'''
else:
    outcome = '''Doom: "You wake to the feeling of cold stone against your face. It is too dark to see. You fumble 
    around for your light, and manage to find it. You press the power button, but it does not turn on. You walk slowly 
    in the dark, feeling for anything, but find no exit. You are stuck."'''
print(outcome)