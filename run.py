from git import Git
r = Git("F:\\elstec")
r.execute('git add .')
r.execute('git commit -a')
r.execute('git push -u origin main')
