# Importing SYS
import sys
# Disable __pycache__ folder creation
sys.dont_write_bytecode = True

# Importing OS
from os import system
# Importing time function
from time import sleep

# Importing all the options
from options_ import *

try:
    # Importing Python Rich Presence
    import pypresence
# If doesn't exist
except ImportError:
    # Warn Message
    print("Trying to Install required module: pypresence\n")
    # Installs pypresence if doesn't exist
    system("python -m pip install pypresence")

# Import Presence from pypresence
from pypresence import Presence

# Sets the Rich Presence to your client id
RPC = Presence(client_id=client_id)

# Starts the Rich Presence
RPC.connect()

"""
INFORMATIONS:
To use the animation, you must first scale your gif to a size between 512 and 1024 minimum, then split it (i recommend using ezgif.com).
Once done you must create a new application on https://discord.com/developers/applications. Let's say you create an app called "Animation".
Once done go directly to the tab "Rich Presence", now go to your folder with all your images split (must be in a zip if used ezgif).
Select them all and rename them all at once. You can give it a prefix and a name, that's all. For example, "lol_vi-jinx" will be "lol_vi-jinx (1)" and "lol_vi-jinx (2)", etc.
Now upload them all into the Rich Presence Assets (you can choose one of the frame as the cover for phone users).
Go into the "options_.py" and place here the prefix (with the _ or the - if you added one), the base name, and the suffix if you added any (in the Rich Presence assets
it should look something like "lol_vi-jinx_1_" so the prefix would be "lol_", the base name "vi_jinx" and suffix "_" cause "1_") Once finished, enter the amount of frames, me i have 20 frames. 
Now that it is done, enter a first line and second line if you want to, and an image text. And then, enter the delay between each frames and run the "main_.pyw".

WARNING:
the image name will be "{prefix}{image}_{i}{suffix}"
so if prefix is "a_" image is "b" and suffix is "_" it will be "{a_}{b}_{1}{_}"
"""

# Stay alive
while True:
    if i == frames:
        i = 1
    rpc = RPC.update(details=first_line, state=second_line, large_image=prefix+image+'_'+str(i)+suffix, large_text=image_txt)
    i += 1
    print(rpc)
    sleep(delay)