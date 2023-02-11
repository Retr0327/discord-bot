# **discord-bot**

This project builds a simple Discord bot which was designed to make our Discord life easier and cooler.

## **Features**

- `/echo [message]`: Echo the same message content to the user
- `/ban [user]`: Ban user
- `/kick [user]`: Kick user
- `/brodcast [channel] [message] [minutes]`: Send the scheduled message to a channel
- `/unbrodcast [channel]`: Remove the scheduled message from a channel
- `/clear [channel]`: Clear the chat history of a channel
- `/create [channel]`: Create a channel
- `/delete [channel]`: Delete a channel
- `/send_to [channel] [message]`: Send the message to a specific channel


## **Setup**
### 1. Installation
- Installation
- Clone repository
  ```bash
  git clone git@github.com:Retr0327/discord-bot.git
  ```
- Install Requirement
  ```
  cd discord-bot && pip install -r requirements.txt
  ```

### 2. Start the bot
There are two main ways to run the bot: 

- in Python
- 
  First make sure you are in the `discord-bot` folder, and then simply run:

  ```bash 
  python ./bot/bot.py
  ```
  or 
  ```bash 
  python -u "./bot/bot.py"
  ```

- run in Docker
- 
  Install Docker, and use the following command to run:

  ```bash
  docker compose up
  ```

## Contact Me
If you have any suggestion or question, please do not hesitate to email me at lixing.dev@gmail.com
