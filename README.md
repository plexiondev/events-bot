# Events Bot for Discord
A bot that allows you to easily manage and announce events for you and your friends, built right into Discord.

## How to install
Unfortunately at the moment I cannot provide a 24/7 web-hosted version of the bot for you to add to your server. Right now, you need to self-host the bot for your guilds.

### 1. Download the files

Obviously, the first step is to get all the files downloaded.

1. Click the latest release on the sidebar of the Github page: [Releases](https://github.com/plexiondev/events/releases/)
2. Download the available .zip file and extract it into your Downloads folder (for example)
3. Move the files to the place you want to host the bot, a nice and safe directory for your bot to live
4. Keep this folder open for the later steps

### 2. Create a Discord Bot

First thing first, let's get a Discord bot up and running for your server.

1. Head over to the [Discord Developer Portal](https://discord.com/developers/applications) and create a **New Application**
2. Then go to the **Bot** tab and **Add** a **Bot** user
3. You can then go ahead and customise the appearance of the bot, this will show up in your server!
4. Where it says "TOKEN", press the **Copy** button
5. Going back to your bot folder, open **token.txt** and paste in your token (you can then close the file)
6. Back at the Developer Portal bot page, head over to the **OAuth2** tab and scroll down
7. At the bottom of the page, find **bot** and **applications.commands** and check both boxes
8. Then enable **Administrator** in the bottom selection (as a permission) then press the big blue **Copy** button
9. Paste this link into your browser and choose the server you want to add your bot to
10. Your bot should now be in the server!

### 3. Finishing up

Now your bot's in the server, there's a few more setup you need to do before you can run your bot.

1. Head into your Discord settings, scroll down until you see the **Advanced** tab and click it
2. Enable **Developer Mode** and exit the settings
3. You can now right click on your server icon (in the sidebar) and press **Copy ID**
4. Paste this value into the **guild.txt** file in your bot's folder
5. Back in Discord, you then need to create (unless you have them already) channels for event announcements (an announcement channel) and one for your actual event messages (for reacting/joining)
6. Once they're created, right click your event messages channel and press **Copy ID** - paste this into **channels.txt**
7. Then right click your announcement channel, **Copy ID** and paste this (with a comma) into **channels.txt** aswell (eg. eventid,announcementid)

### 4. Starting up

Now everything should be ready! Simply head into your bot folder and double click **main.py** (or open cmd and run main.py - to see when an error occurs and your bot closes - up to you)

If you have any issues or questions, simply leave a Github issue in this repository. Anyways, have a good day!
