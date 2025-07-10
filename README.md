# all_configurations
configs for vscode, sublime, ohmyzsh and more

| Shortcut | Explanation |
|----------|------------------|
| Cmd + [  | shift whole line to right
| Cmd + 0 / Cmd + Shift + E  | Focus on sidebar items
| Cmd + T  | Search for function/class names
| Shift + Ctrl + Right Arrow  | Select entire function
| Ctrl + G  | Go to line
| CMD + Shift + L  | Select all occurences of object in current focus





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

#### Instal a specific version of python with brew
`brew install python@3.9`  

#### Install oh-my-zsh
`sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`  



## Important Mac apps/changes
Install these apps:
- Homebrew
- Spectacle
- Pure Paste
- Hidden Bar
- Ghostery ad blocker
- Bitwarden
- Trello
- Badgeify menu items notifications (for teams, outlook etc)
- Itsycal


## Setup github
https://docs.github.com/en/enterprise-server@3.8/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux  

https://docs.github.com/en/enterprise-server@3.8/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account  

Then, add your ssh key to your ssh config by:  
`nano ~/.ssh/config`  

and then write:  
```sh
Host *
  UseKeychain yes
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
```

## Important Mac apps/changes
Install these VSCode extensions:
- Material Icon Theme
- Git History
- Github Pull Requests
- One Light Theme
- Rainbow CSV
- Atom One Dark Theme


## Optional
Control brightness with vivid: https://www.getvivid.app  
External monitor brightness control: https://github.com/MonitorControl/MonitorControl  

## Github Flow

git flow < 4 people in team 
chunk based flow > 5 people in team 

| STEP | COMMAND / ACTION | EXPLANATION |
|------|------------------|-------------|
| 1    | `git checkout develop`<br>`git pull origin develop` | Make sure you are in the develop branch, and pull the latest changes |
| 2    | `git checkout -b feature/feature_name develop` | Create a new feature branch from the develop branch |
| 3    | Make changes to the code | |
| 4    | `git add .` | Stage all changes |
| 5    | `git commit -m 'detailed message'` | Commit the changes with a message |
| 6    | `git push origin feature/feature_name` | Push the feature branch to the remote repository |
| 7    | Create pull request on GitHub | Create a pull request targeting the `develop` branch. Assign a reviewer if necessary |
| 8    | Notify the reviewer | Send them a message |
| 9    | Reviewer merges pull request, and deletes the branch on the remote repository | The reviewer will handle merging the feature branch into `develop`, addressing any conflicts if they arise |
| 10   | `git checkout develop`<br>`git pull origin develop` | Update your local develop branch with the latest changes |
| 11   | `git branch -d feature/feature_name` | Remove branch  |


## Andere belangrijke git commands

- `git stash`: Tijdelijk opslaan van changes in een branch, breng ze terug met `git stash pop`, ziet een lijst met stashes via `git stash list` of verwijderd al je stashes gemakkelijk met `git stash clear`
- 


## Terraform commands
1. **terraform init**
   - Initializes a Terraform project, setting up the backend and downloading provider plugins.

2. **terraform plan**
   - Creates an execution plan, showing the changes Terraform will make to achieve the desired state.

3. **terraform state list**
   - Lists all resources
4. **terraform show**
   - Lists all in detail
