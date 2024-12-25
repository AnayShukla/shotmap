## Shotmap
Generates a shot map visualization of a player in the top 5 leagues (PL, La Liga, Serie A, Bundesliga, Ligue 1) and RFPL, all this data sourced from https://understat.com. EV projections also avaiable, sourced from https://fplreview.com.

## Tutorial
1. Download the zip file and extract its contents or run `git clone https://github.com/AnayShukla/shotmap.git` in your Terminal.
2. Set the directory to the path where you have cloned the repository (use `cd`)
3. Run `pip install -r requirements.txt` to install all the required packages.
4. Run `python shot.py`.


## Generating Output
1. Enter the name of the player whose shot map you wish to see. You can also enter discrete names such as **salah** to get it for **Mohammed Salah**, but avoid doing so for players with common names or vague spellings (basically specificity is preferred :) )
2. Enter the initial year of the season of your choice. For e.g. if you wish to see it for the 2024/25 season, enter 2024.
3. Type yes or no if you wish to see FPL Review EV for the upcoming GW.
4. Check `shotmap/results` to find the exported image.

## Example
Entering Evanilson and 2024 would yield you an image like this:


![evanilson 24](https://github.com/user-attachments/assets/7f33401f-a0a4-4a13-a044-9d2ca628b052)

## Note
Reminder that this is still a work in progress, will be making fixes with a few issues and also try to introduce new updates as well. Works perfectly for all players for the current season, however for players who played in a different league 
in any of the previous seasons will not yield accurate outputs, hoping to fix it soon!
