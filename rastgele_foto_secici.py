import os, random, subprocess

folder = r"Folder_Path"

Extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

phot_list = [f for f in os.listdir(folder) if f.lower().endswith(Extensions)]

if photo_list:
    selected = random.choice(photo_list)
    path = os.path.join(folder, selected)
    print(f"Selected photo:{path}")
    subprocess.run(["start", "", path], shell=True)
else:
    print("Error: Not Found Photo!")
