# all_configurations
configs for vscode, sublime, ohmyzsh and more



## always do this

#### Set capslock to Escape
Settings -> keyboard --> key combinations --> special keys --> caps lock to escape
#### Add vscode and sublimne etc to PATH 
First of all launch VS Code and open the Command Palette (Cmd+Shift+P) and type ‘shell command’ to find the Shell Command: Install ‘code’ command in PATH command. Now you should be able to open iTerm and type code ~/.zshrc.
Now, you can open folders with just the command code, or with sublime text just like: subl ~/.zshrc for your zsh config

#### Make mac dock appear and dissapear faster 
defaults write com.apple.Dock autohide-delay -float 0 && killall Dock  
defaults write com.apple.dock autohide-time-modifier -int 0; killall Dock

#### Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Then, if not allowed to install due to restrictions, install:

- Sublime Text
- Alfred (activate alfred premium with key in mail)



#### Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"



## Important Mac apps/changes
Install these apps:
- Homebrew
- Spectacle
- Pure PAste
- Hidden Bar
- Ghostery ad blocker
- Bitwarden
- Trello


## Setup github
https://docs.github.com/en/enterprise-server@3.8/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux  

https://docs.github.com/en/enterprise-server@3.8/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account  

Then, add your ssh key to your ssh config by:  
'nano ~/.ssh/config'  

and then write:  

'''Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_ed25519
'''  

## Optional
Control brightness with vivid: https://www.getvivid.app  
External monitor brightness control: https://github.com/MonitorControl/MonitorControl  

## Github Flow
| STEP | COMMAND / ACTION | EXPLANATION |
|------|------------------|-------------|
| 1    | `git checkout develop` | Make sure you are in the develop branch |
| 2    | `git pull origin develop` | Pull latest code version from develop branch before making a new branch |
| 3    | `git checkout -b feature_name develop` | Create a new feature branch from the develop branch |
| 4    | Make changes to the code | |
| 5    | `git add .` | Stage all changes |
| 6    | `git commit -m 'detailed message'` | Commit the changes with a message |
| 7    | `git push origin feature_name` | Push the feature branch to the remote repository |
| 8    | Create pull request on GitHub | MAKE SURE to change the base branch from main to develop. Then, assign a reviewer if necessary |
| 9    | Notify the reviewer | Send them a message |
| 10   | Reviewer merges pull request, and deletes the branch on the remote repository | |
| 11   | `git checkout develop`<br>`git pull origin develop` | Update your local develop branch |
| 12   | `git fetch --prune` | Fetch and prune remote-tracking branches that no longer exist |
