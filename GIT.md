# Basic GIT commands
'''
git config --global user.name "Mona Lisa"
git config --global user.email "email@example.com"

git clone url
git push

git status

git add .
git commit

git branch dev (create dev branch)
git branch (displays branches, * indicates active)
git checkout branchName 
'''

## Merge dev to Master
'''
- Master must be active
git merge dev
git diff
git commit -a
gitk
git branch -d dev

(git branch -D dev removes without checking that its incorporated into Master)
'''
