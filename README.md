# all_configurations
configs for vscode, sublime, ohmyzsh and more



### always do this ####

First of all launch VS Code and open the Command Palette (Cmd+Shift+P) and type ‘shell command’ to find the Shell Command: Install ‘code’ command in PATH command. Now you should be able to open iTerm and type code ~/.zshrc.
Now, you can open folders with just the command code, or with sublime text just like: subl ~/.zshrc for your zsh config

### Important Mac apps/changes
Install these apps:
1. Homebrew
2. Spectacle
3. Pure Paste
4. Hidden bar

### Github Flow ###
| STEP | COMMAND / ACTION | EXPLANATION |
|------|------------------|-------------|
| 1    | `git checkout develop` | Make sure you are in the develop branch |
| 2    | `git pull origin develop` | Pull latest code version from develop branch before making a new branch |
| 3    | `git checkout -b 'feature_add_feature_x develop'` | Create a new feature branch from the develop branch |
| 4    | Make changes to the code | |
| 5    | `git add .` | Stage all changes |
| 6    | `git commit -m 'detailed message'` | Commit the changes with a message |
| 7    | `git push origin feature_add_feature_x` | Push the feature branch to the remote repository |
| 8    | Create pull request on GitHub | MAKE SURE to change the base branch from main to develop. Then, assign a reviewer if necessary |
| 9    | Notify the reviewer | Send them a message |
| 10   | Reviewer merges pull request, and deletes the branch on the remote repository | |
| 11   | `git checkout develop`<br>`git pull origin develop` | Update your local develop branch |
| 12   | `git fetch --prune` | Fetch and prune remote-tracking branches that no longer exist |
