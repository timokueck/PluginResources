# **Resources for Tech's Spigot Plugins**

> A repository holding translations and permissions for [Tech's Spigot Plugins].

- [Discord][Discord]
- [Spigot][Tech's Spigot Plugins]

---

## **Contribute translations**

You are speaking a different language? That's great because we need you to help us translating our work into other languages.

#### Instructions
- check for untranslated phrases in [these files][translations]
- replace the english phrases with the according translations
  - make sure to keep the same format
  - highlight the same words with ``** **``
  - don't use color codes
- uncomment all phrases you translated
- create a [pull request]


## **Contribute permissions**

Our plugin Ultra Permissions simplifies searching for permissions by suggesting them based on installed plugins. The permission suggestions will be retrieved from [this file][permissions].

#### Instructions
- pick a plugin that hasn't been added yet
- add all its permissions line by line
  - make sure to keep the format which is shown below
  - for easier editing use the tool shown below
- create a [pull request]
  - provide a link to the plugin page
  - provide a link to the plugin permissions
  - only add one plugin per pull request
  - when adding permissions for a premium plugin, please provide the plugin.yml
    - the plugin.yml can be found inside the jar file
    - use WinZip or other programs to open it
    - DON'T SHARE THE WHOLE JAR OF A PREMIUM PLUGIN

#### Format
Permissions:<br>
``Plugin + Permission + Description + / optional Command``

Permission commands:<br>
``/ Command <required argument> [optional argument]``

#### Examples
Permission without a command:<br>
``Essentials+essentials.fly+Allows the player to fly.``

Permission with a command:<br>
``Essentials+essentials.fly+Allows the player to fly.+/fly``

Permission with multiple commands:<br>
``Essentials+essentials.fly+Allows the player to fly.+/fly,/playerfly``

Permission with a placeholder:<br>
``Essentials+essentials.fly.[world]+Allows the player to fly in a specific world.``

Permission with command and required argument:<br>
``Essentials+essentials.fly+Give someone fly mode.+/fly <player>``

Permission with command and required argument to choose:<br>
``Essentials+essentials.fly+Give someone fly mode.+/fly <player|mob>``

Permission with command, required and optional argument:<br>
``Essentials+essentials.fly+Give someone fly mode.+/fly <player> [world]``

#### Editing tool
If you are using [Visual Studio Code] as your editor, you can now use an extension that
provides syntax highlighting for the [permission database][permissions].

You can get it [here][extension].

---

<!-- Links -->
[Tech's Spigot Plugins]: https://www.spigotmc.org/resources/authors/techscode.29620/
[Discord]: https://discord.gg/3JuHDm8
[translations]: https://github.com/TechsCode/PluginResources/tree/master/Translations
[pull request]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
[permissions]: https://github.com/TechsCode/PluginResources/blob/master/Permissions%20Database/Database.updb
[Visual Studio Code]: https://code.visualstudio.com/
[extension]: https://marketplace.visualstudio.com/items?itemName=RLNT.uperms-db-syntax
