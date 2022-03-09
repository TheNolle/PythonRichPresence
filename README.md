All you need to do:  <br>
Download the release you are interested in, and get started.

---

# Get Started

## Static
To use the static version, you must first scale your image(s) to a size between 512 and 1024 minimum.  <br>
Once done you must create a new application on https://discord.com/developers/applications. Let's say you create an app called "Static".  <br>
Once done go directly to the tab "Rich Presence", now go to your folder with your image(s).  <br>
Select it/them (you can rename it/them directly when uploaded).  <br>
Now upload it/them into the Rich Presence Assets (you can choose any image as the cover for phone users).  <br>
Go into the "options.py" and place here the name of the image(s).  <br>
Now that it is done, enter a first line and second line if you want to.  <br>
Run main.pyw by either double clicking it (running in background) [to stop it run the "stop program"] or run in an IDE.

## Animated
To use the animated version, you must first scale your gif to a size between 512 and 1024 minimum, then split it (i recommend using https://ezgif.com). <br>
Once done you must create a new application on https://discord.com/developers/applications. Let's say you create an app called "Animation". <br>
Once done go directly to the tab "Rich Presence", now go to your folder with all your images split (must be in a zip if used ezgif). <br>
Select them all and rename them all at once. You can give it a prefix and a name, that's all. For example, "lol_vi-jinx" will be "lol_vi-jinx (1)" and "lol_vi-jinx (2)", etc. <br>
Now upload them all into the Rich Presence Assets (you can choose one of the frame as the cover for phone users). <br>
Go into the "options_.py" and place here the prefix (with the _ or the - if you added one), the base name, and the suffix if you added any (in the Rich Presence assets <br>
it should look something like "lol_vi-jinx_1_" so the prefix would be "lol_", the base name "vi_jinx" and suffix "_" cause "1_") Once finished, enter the amount of frames, me i have 20 frames.  <br>
Now that it is done, enter a first line and second line if you want to, and an image text. And then, enter the delay between each frames and run the "main_.pyw".  <br>
Run main_.pyw by either double clicking it (running in background) [to stop it run the "stop program"] or run in an IDE.

### WARNING:
the image name will be "{prefix}{image}_{i}{suffix}" <br>
so if prefix is "a_" image is "b" and suffix is "_" it will be "{a_}{b}_{1}{_}"
