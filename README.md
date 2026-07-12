# MonoKey-Mania
### A retro-themed single-key web arcade. (Inspired for onekey HackClub)
### You can only use a SINGLE KEY
---
### Initial Plan:
To make a card highlight  menu themed website that has option of morse and cubesat(postponed) programs
That I would only use a single key for menu control and launch

### Ended Up:
The design chaged to a bit more on the keycaps ends.
Becoming a circus mania of different programs. I intent to further work on this maybe as a personal site or for another ysws

---
## Features:
* Basically you initially bind your key when a pop-up appears in the start
* You can choose **ANY KEY** of your liking thats a cool feature right
* I am Using a terminal style Idk I just like it thought of makinga a gaint key but didn't
* Then you have locked the key and you cannot change it unless you refresh the page
* Then there are some **menu rules:**
  1. Click the key to move through all those program keys in the menu
  2. Pause for 1.5s to launch that 
  3. Press for 5s to reset selection
  4. Once reaching the last key and unclicked wait a few seconds to navigate again
  5. ****In Game****: if in game press the key for 10s to go back to the menu
---
* **Morse**
* Uses time based threshold along with the dictionary for morse
  1. Tap for dot (.)
  2. Hold for dash (-)
  3. Space is auto implemented, so its challenging to level up your morse game
* **Dice**
* Uses randomizing processm and displays random numbers (1-6) on head then picks one between and stops at the result
  1. Tap to roooolll. Very Simple
* **WikiTap**
* Uses Wikipedia's free api to fetch articles
  1. Press the key to land into Wiki-Verse
  2. Rnadom Articles from wikipedia
  ~I had fun implementing api and learning it for this first api related project (Did use AI for help)
* **TypingMongo**
* Uses Press down adn up like others just change the image on screen and add a text for slam count variable
* Plus the appends revel text variable to display the hidden text
  1. Click your key and slam that key cap
  2. Reveals a secret message for the King of ONE-KEY
---
**Some other features**
* Animated keys press for the title MONOKEY MANIA
* Ignoring repeat keys, the glitch of morse when you lift up
* Implemented a keyclick sound effect
* Uses window listeners to read key (I learned this new thing along with the document, as I was doing brython)
* What I understand document allows you to access the web front from within a .py file, and its basically html and css if you look at it
---
### Structure:
It's a bit scattered like I just made a source folder 'src' and just dumped every python file and image there so I dont have to define an absolute path while importing

---
