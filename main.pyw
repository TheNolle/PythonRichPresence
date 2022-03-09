# Importing SYS
import sys
# Disable __pycache__ folder creation
sys.dont_write_bytecode = True

# Importing OS
from os import system
# Importing time function
from time import sleep

# Importing all the options
from options import *

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

# Create button, only one
button_1 = [{"label":button_1_url,"url":button_1_url}]
# Create button, two
button_2 = [{"label":button_1_url,"url":button_1_url},{"label":button_2_url,"url":button_2_url}]

# Changes all the informations to the entered ones above
if buttons_:
    if buttons_num == 1:
        rpc = RPC.update(details=first_line, state=second_line, large_image=image_1, large_text=image_1_txt, small_image=image_2, small_text=image_2_txt, start=time_, buttons=button_1)
    elif buttons_num == 2:
        rpc = RPC.update(details=first_line, state=second_line, large_image=image_1, large_text=image_1_txt, small_image=image_2, small_text=image_2_txt, start=time_, buttons=button_2)
else:
    rpc = RPC.update(details=first_line, state=second_line, large_image=image_1, large_text=image_1_txt, small_image=image_2, small_text=image_2_txt, start=time_)

# Stay alive
while True:
    print(rpc)
    sleep(15)