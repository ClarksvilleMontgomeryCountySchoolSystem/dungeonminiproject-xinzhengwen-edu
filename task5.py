escaped = True
if escaped:
    outcome = '''Legend: "The doorway leads to another flight of stairs. You make the brutal ascent once more, and
    eventually meet a rusted steel door. With great difficulty, you manage to open it. Outside lies a field. When you 
    look behind you, there is no trace of the door. You walk until you find civilation."'''
else:
    outcome = '''Doom: "The doorway leads to another flight of stairs. You make the brutal ascent once more, and
    eventually meet a rusted steel door. With great difficulty, you manage to open it. Behind it lies the same narrow
    corridor you woke in. You turn around but see you are back where you started. Your light dies before you find 
    the exit. You are stuck."'''
print(outcome)