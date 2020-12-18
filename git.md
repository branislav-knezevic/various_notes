# Notes and usefull command related to git

## File history

`git log <path_to_file>` shows the history of commits on the specific file
`git log Dockerfile`
`git show <git_hash>:<path_to_file>` shows how files looked like in a specific commit
`git show jfi22i9sdjf9sdf9j29jfd9fj:Dockerfile`
`git show HEAD@{year-month-day}:<path_to_file>` shows how file looked like on specific date
`git show HEAD@{2020-11-23}:Dockerfile`
`git diff-tree -p <git_hash>` shows chages from specific commit
`git diff-tree -p aefbc427d6b567ca1d2f10398d936985bb587824`
