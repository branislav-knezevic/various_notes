# Notes and usefull command related to git

## Sources

https://www.youtube.com/watch?v=FdZecVxzJbk

## File history

`git log <path_to_file>` shows the history of commits on the specific file
`git log Dockerfile`
`git show <git_hash>:<path_to_file>` shows how files looked like in a specific commit
`git show jfi22i9sdjf9sdf9j29jfd9fj:Dockerfile`
`git show HEAD@{year-month-day}:<path_to_file>` shows how file looked like on specific date
`git show HEAD@{2020-11-23}:Dockerfile`
`git log --stat` shows files which were changed in each commit
`git reflog` history of commands made

### Reverting to old commit in history

`git reflog` show history
`git checkout <some_old_commit>` this will be in detached state, branch needs to be created out of it
`git branch <new_desired_branch>` those old chanes will be on this branch now.
Next merge this branch where ever needed.

Other option:
`git revert <some_old_commit>` adds new commit on top of existing ones but revert

## Committing

`git commit --amend -m "<new_message>"` updating last commit message
`git commit --amend` gives an option to edit a message but also includes any files added to staging
`git clean -df` removes any untracked files

## Cherrypicking

`git log` to get commit ids
`git checkout <desired_branch>`
`git checkout feature_branch`
`git cherry-pick <commit_id>` copies commit from original branch to the desired one
`git cherry-pick aa12314`
`git checkout <original_branch>` get back to "wrong" branch
`git checkout master`
`git reset <commit_before_wrong_commit>` delete commit on wrong branch - changed files will be still shown with `git
status`
`git reset --hard <commit_before_wrong_commit>` this will delete all made changes. Untracked files will still be there

## File diff

`git diff <commit_1> <commit_2>` show differences between two commits
`git diff-tree -p <git_hash>` shows chages from specific commit
`git diff-tree -p aefbc427d6b567ca1d2f10398d936985bb587824`

## Branches

`git branch -D <branch_name>` delete local branch  
`git push origin --delete <branch_name>` delete remote branch
