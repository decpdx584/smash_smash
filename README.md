# smash_smash

This project was the brain-child of my dear wife who was attempting to help me think of something that would hold my interest beyond merely finishing this project. We love to play Super Smash Bros. together and she wondered if I could program an application that pairs up Smash Bros. characters and tells you how compatible they would be romatically. You know, Smashing Smash Bros!

I immediately loved the idea but had NO IDEA how I was to accomplish such a thing. The main goal of this project for me was (besides passing💩) to learn some new technology on my own, separate from the material that had been spoon-fed to us by our instructors. So, after talking with some of them and boucing ideas off various people I landed on a Flask-SQLAlchemy stack for the project. With Sarah King's infinite wisdom to guide me, I thought the mechanic of the application would be like some of my favorite board/card games (made by Cyanide and Happiness): A user would be able to choose from all the SSBU characters and pair any two up. Then that user (or any other user) could write arguments for why the proposed couple would be compatible or not. I LOVE arguing pointless points (as my wife can attest) and, so, this gameifying of the idea intrgued me.

Another thing I wanted to do with this project was write my own web-scraping bot in Python using Jupyter Notebook. We learned a bit about it during the last days of instruction and I was immediately hooked. So, I did it! It took at least 2 days for me to be able to clean the data I was scraping and sufficiently store it in the database I made with SQLAlchemy. It was SUPER satisfying to see it finally work, though! I still like to look back through the code of my smash_bot fondly from time to time🤗

## Tech Employed
- Flask
- SQLAlchemy
- Jupyter Notebook

## Run my app thus:
- Open a virtual environment and install the requirements.txt for the project.
- Export the environment and app from the command line thus:
```bash
export FLASK_ENV=development
export FLASK_APP=api.py
flask run
```
- Once the flask server is running, copy the port's address and paste it into your browser.

## Wrestling with SQLAlchemy
So, this project is not finished. There are a few things I've still been unable to get going in SQLAlchemy. For example, I'm still trying to be able to post new Dates and Arguments from the Flask frontend. This is the core of my game that I want to get running. I feel like I'm so close.

## Stretch Goals
Once I get the core game funtioning I have a few stretch goals I like to handle in the coming week or so:
- **move the app declaration to the api.py** After talking to Pete and doing a bunch of research online, putting the app declaration and configuration into models.py makes less and less sense to me. So, I want to put it into my api.py (my server).
- **deployment** I want this game to be available to play! I'll make it look nice(r) first but FIRST-FIRST I need the functionality.
- **write in more pseudocode** I need to practice writing pseudocode more during developement but I want to make my code easier to read by adding more into this project.

## Conclusion
I know this isn't a finished product by any real means. I have plenty of work to do on this. I do, however, feel like I've achieved the main goal of mine which was to learn some new tech on my own. I really did feel on my own with this one for most of it because even when I did reach out for help most people had little-no experience with this stack. It's forced me to do a LOT of learning on my own (with Google, of course) which I think is probably great practice for my life moving forward in this new career.
STRUGGLES AND HARD-EARNED REWARDS, HERE I COME!!!
