# Remove cutscenes at boot of Rainbow Six Siege

## Explanation ##
There are two optional, skippable cutscenes that play when loading Tom Clancy's Rainbow Six: Siege. They are stored locally as bitmap files, and can be replaced with empty files to skip those cutscenes automatically. This python script will rename the two files so as to save them off in the case that they want to be added back, then creates two new empty bitmap files that will be "played" when loading the game.

The default directory for these files is in C:\Program Files (x86)\Steam\steamapps\common\Tom Clancy's Rainbow Six Siege\videos\startup where there are 2 files, "y0r6_logo_nvidia.bik" and "y0r6_logo_ubisoft.bik". These files will be renamed to "y0r6_logo_nvidia_old.bik" and "y0r6_logo_ubisoft_old.bik" respectively, then new .bik files will be made with the original names. To revert, delete the files "y0r6_logo_nvidia.bik" and "y0r6_logo_ubisoft.bik", then remove the "_old" portion from the remaining files and the cutscenes will play again on boot of the game. 

## Usage ##
Run the app.py python scipt. It will prompt you to enter 1 or 2 - one will open the file explorer to select the directory that the videos are in, 2 will allow you to paste it directly into the console window. Once the directory is selected, if the files are found in that directory, it will complete the process.

Feel free to [tip me BAT](https://brave.com/tip-with-brave/) through github if you enjoy the script and feel so inclined :)