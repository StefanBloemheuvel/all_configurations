# all_configurations
configs for vscode, sublime, ohmyzsh and more

| VSCode Shortcut | Explanation |
|-------------------------------|---------------------------------------------------------------------|
| Cmd + [                       | shift whole line to right
| Cmd + 0 / Cmd + Shift + E     | Focus on sidebar items
| Cmd + T                       | Search for function/class names
| Shift + Ctrl + Right Arrow    | Select entire function
| Ctrl + G                      | Go to line
| Cmd + Shift + L               | Select all occurences of object in current focus
| Cmd + L                       | Select entire line
| Cmd + \                       | Split current window in two panes
| Cmd + D                       | Select current object/word
| Ctrl + J                      | Join previous line to current line
| Cmd + Shift + .               | Get window with all functions in current script for fast navigation

| Terminal/ Git Shortcut               | Explanation                                                   |
|--------------------------------------|---------------------------------------------------------------|
| git rebase -i main                   | Interactive rebase where commits can be picked
| Ctrl + R                             | fuzzy search through previous terminal commands
| git checkout -                       | checkout previous branch
| python -m pdb script.py              | run until error then Pdb() env
| breakpoint() & interact              | gives interactive environment with multi-line support pasting
| git stach & git pop & git stash list | store changes in temp place and put back again with pop
| l . or list .                        | see where you are in the code during Pdb session


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

## Chrome extensions
- Smooth Key Scroll (for scrolling with J and K)


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

## Git Flow

git flow < 4 people in team 
chunk based flow > 5 people in team 

| STEP | COMMAND / ACTION | EXPLANATION |
|------|------------------|-------------|
| 1    | `git checkout main` | go to main |
| 2    | `git pull origin main` | pull the latest changes |
| 3    | `git checkout -b sbloemheuvel/feature_name` | Create a new feature branch from the main branch |
| 4    | Make changes to the code | |
| 5    | `git add .` | Stage all changes you made |
| 6    | `pre-commit run ` | check code quality and add neede changes with `git add .` again |
| 7    | `git commit -m 'detailed message'` | Commit the changes with a message |
| 8    | `git push origin sbloemheuvel/feature_name` | Repeat steps 4-7 untill satisfied. Push the feature branch to the remote repository |
| 9    | Create pull request on Gitlab | Create a pull request targeting the `main` branch, link is in the message in your terminal. Assign a reviewer |
| 10   | Notify the reviewer | Send them a message |
| 11   | Reviewer/you perform rebase on gitlab ui, merges pull request, and deletes the branch on the remote repository automatically |  |
| 12   | `git checkout main `<br>`git pull origin main` | Go back to main, update with the latest changes |
| 13   | `git branch -d sbloemheuvel/feature_name` | Remove branch  |


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
