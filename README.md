## This repository is to enable us work together as a team
### BOOTCAMP KTLL

This repository is for files used in sessions of the bootcamp ktll.
It will immediately tell someone what we have been doing and how to
join the bootcamp.

## COMMAND LINE PROMPT
The commands that are here will work naturally for all unix based users
but for windows users, they will need to use git bash for these commands

### CREATE A NEW DIRECTORY
```
mkdir new-directory name
```

### CHANGE DIRECTORY
```
cd new-directory
```

### CREATE A NEW FILE
```
touch new-file
```

### SOME GIT COMMANDS
GIT is a version control system that tracks changes in a file.
GITHUB is an online service that allows developers to create, store, manage and share their code.
It uses GIT to implement version control system.

You can create a repository in GITHUB then clone the repo to your local system and work from your
local system. Then you can push your new files and changes to old files to the online repository 
on GITHUB.


So after creating a repository on GITHUB, you can clone it to your local system using the command
```
git clone link-to-your-online-repository-on-github
```

Then you change directory into the new directory that has been created from the last command. You
can then start creating new files inside the new directory. 
After creating a new file, git needs to know about the file so you use the code
```
git add filename
```

After adding the file to git, you need to commit all changes you make to the file
so you use the command
```
git commit -m 'the commint message, telling everyone what changes you made to the file' filename
```

After commiting the changes made to a file, you will then push the file(s) to your online repository
```
git push
```
If it is the first time you are doing the push, you will likely be using the command
```
git push -u origin your-branch-name
```



