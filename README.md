# Events Bot for Discord
A bot that allows you to easily manage and announce events for you and your friends, built right into Discord.

If you've installed the datapack, have a read through [the wiki](https://github.com/plexiondev/events-bot/wiki) for information on all available commands.

## How to install
Unfortunately at the moment I cannot provide a 24/7 web-hosted version of the bot for you to add to your server. Right now, you need to self-host the bot for your guilds.

### 1. Download the files

Obviously, the first step is to get all the files downloaded.

1. Download the [latest available .zip](https://github.com/plexiondev/events/releases/) and extract it into your Downloads folder (for example)
2. Move the files to the place you want to host the bot, a nice and safe directory for your bot to live (keep this open for later)

### 2. Create a Discord Bot

First thing first, let's get a Discord bot up and running for your server.

![image](https://user-images.githubusercontent.com/46572320/130800818-1b65d7d7-36bc-4031-a4e7-0b7f7a06673d.png)

1. Head over to the [Discord Developer Portal](https://discord.com/developers/applications) and create a **New Application**
2. Then go to the **Bot** tab and **Add** a **Bot** user ![image](https://user-images.githubusercontent.com/46572320/130800973-88cbb8a3-3837-482a-bc25-d99ec83fff14.png)
3. You can then go ahead and customise the appearance of the bot, this will show up in your server! ![image](https://user-images.githubusercontent.com/46572320/130801201-472ae176-104d-4b70-b6d7-bb5f601bdeb3.png)
4. Where it says "TOKEN", press the **Copy** button 
![image](https://user-images.githubusercontent.com/46572320/130801235-04ea1587-8c76-442f-b175-6589ef9a7c47.png)
5. Going back to your bot folder, open **token.txt** and paste in your token (you can then close the file) ![image](https://user-images.githubusercontent.com/46572320/130801438-efd115e8-6488-44ce-ae78-bf866bd851b3.png)
6. Back at the Developer Portal bot page, head over to the **OAuth2** tab and scroll down
7. At the bottom of the page, find **bot** and **applications.commands** and check both boxes
8. Then enable **Administrator** in the bottom selection (as a permission) then press the big blue **Copy** button ![image](https://user-images.githubusercontent.com/46572320/130801928-bcdf0e7b-f9ad-4512-a2ce-90929a2f4cab.png)
9. Paste this link into your browser and choose the server you want to add your bot to ![image](https://user-images.githubusercontent.com/46572320/130802033-2a31b50e-fe27-49e6-9ead-0a8650231d5f.png)
10. Your bot should now be in the server!

### 3. Finishing up

Although the bot's added, there's some final setup required before we're ready.

1. Head into your Discord settings, scroll down until you see the **Advanced** tab and click it ![image](https://user-images.githubusercontent.com/46572320/130802152-d687728a-46ef-4c11-abf6-efb39e88fe97.png)
2. Enable **Developer Mode** and exit the settings ![image](https://user-images.githubusercontent.com/46572320/130802178-c272e1dd-26a5-46ac-b374-4f90972d2764.png)
3. You can now right click on your server icon (in the sidebar) and press **Copy ID** ![image](https://user-images.githubusercontent.com/46572320/130802342-083578d8-a238-4a93-9c71-d89d5f4e0d65.png)
4. Paste this value into the **guild.txt** file in your bot's folder ![image](https://user-images.githubusercontent.com/46572320/130802396-f6c4fbe8-5d74-4fb9-8d7c-3f62fc3ada78.png)
5. Back in Discord, you then need to create (unless you have them already) channels for event announcements (an announcement channel) and one for your actual event messages (for reacting/joining) ![image](https://user-images.githubusercontent.com/46572320/130802643-d2cee862-dde4-4073-90e4-7d0cd98348c9.png)
6. Once they're created, right click your event messages channel and press **Copy ID** - paste this into **channels.txt** ![image](https://user-images.githubusercontent.com/46572320/130802842-65c01fa9-38ac-42bd-bf12-9396b850dc6d.png)
7. Then right click your announcement channel, **Copy ID** and paste this (with a comma) into **channels.txt** aswell (eg. eventid,announcementid) ![image](https://user-images.githubusercontent.com/46572320/130802774-84551b80-6ca3-4b72-b45c-83edcf202d7a.png)

### 4. Starting up

Before you can actually run your bot, two additional dependencies will need to be installed: `discord` and `discord-py-slash-command` Make sure you have Python 3+ installed before doing this step.

On Windows, this can be installed by opening a **Command Prompt** `cmd` window and typing both:

```
py -m pip install discord
```
```
py -m pip install discord-py-slash-command
```

Now everything should be ready! Simply head into your bot folder and double click **main.py** (or open `cmd` and run `main.py` - to see when an error occurs and your bot closes - up to you)

If you have any issues or questions, simply leave a Github issue in this repository. Anyways, have a good day!
