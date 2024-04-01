<p align="center">
  <img src="https://i.ibb.co/j3WsQqd/chumbot-with-text-transparent.png" width="400" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">kaylinaurora/ChumBot</h1>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>A simple Discord bot developed in Python</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Discord-5865F2.svg?style=default&logo=Discord&logoColor=white" alt="Discord">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#overview)
- [ Features](#features)
- [ Repository Structure](#repository-structure)
- [ Modules](#modules)
- [ Getting Started](#getting-started)
  - [ Installation](#installation)
  - [ Usage](#usage)
- [ Project Roadmap](#project-roadmap)
</details>
<hr>

##  Overview

Hi! 👋 I'm ChumBot - just a little guy from the big blue sea that loves to see friendships thrive 🩵

---

##  Features

<img src="https://i.ibb.co/CmbF7WB/chumbot-demo.png" width="100%"><br>
- React to any *server message* with a 🤕 emoji
  - This will trigger a DM to be sent to the author, letting them know their message was hurtful
> Hello, your message received a 🤕 reaction indicating it may have been hurtful. Please be mindful of your words. <br><br>
> **Message:**
>> you are stimky <br>
>> [Link to 'View Message']
- React to any *DM from **ChumBot*** with a ❌ emoji
  - This will delete any DM received by **ChumBot**
- All server transactions are logged in `chumbot.log`
---

##  Repository Structure

```sh
└── ./
    ├── ChumBot.py
    └── requirements.txt
```

---

##  Modules

<details open><summary>Modules</summary>

| Module | Version |
| --- | --- |
| discord.py | <code>2.3.2</code> |
| python-dotenv | <code>1.0.1</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.10.10` (known working, YMMV on other versions)

###  Installation


> 1. Navigate to the repo directory:
>
> ```console
> $ cd /path/to/ChumBot
> ```
>
> 2. Install the requirements:
> ```console
> $ pip install -r requirements.txt
> ```
>
> 3. Create a .env file and add your bot token from the Discord Developer Portal:
> ```console
> $ nvim .env
> ```
> ```console
> DISCORD_BOT_TOKEN={your_token_here}

###  Usage

> Run the bot
> ```console
> $ python ChumBot.py
> ```


---

##  Project Roadmap

- [ ] `Send DM to reacting users to let them know a message was sent to the author`

---

[**Return**](#overview)

---
