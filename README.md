# Battlerships game

Ultimate Battlership is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can try to beat the computer by finding all of the computer's battlerships before the computerfinds their.<br>

Each battlership occupies one square on the board.
The game starts after the player writes his name.
<br>

Here [Link](https://buttleerships-game-41ca3ea47dae.herokuapp.com/) you can open live version of the game.
Enjoy it!

## How to play

You don't know what a game is?
Find out the basic information on [Wikipedia](<https://en.wikipedia.org/wiki/Battleship_(game)>) as soon as possible.<br>
Now you're ready to play!

First, the player needs to enter a name, which will then be displayed to show scores.<br>

After that, a board with a random arrangement of 4 ships will appear. But the location of the ships of the computer is hidden (yes, yes, because this is the point of the game).<br>

Then the player will be asked to guess the location of the enemy ship using the coordinates of the board. The guess will be marked with an X.
Hits are indicated \*.<br>

A random number is generated for the computer to guess.
After each round, a scoreboard will appear with the results. <br>

The winner is the one who managed to sink the enemy ship.

## Testing

_The following technical tools were used:_

## Featers

- ### Existing featers

  - #### Random board generation

  - #### The player cannot see the location of the computer's ships

  - #### The player sees the location of his ships, which are marked with the @ sign

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

---
