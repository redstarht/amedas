

PS C:\Users\na-taniguchi\practice> 
PS C:\Users\na-taniguchi\practice> 
PS C:\Users\na-taniguchi\practice> git config
error: no action specified
PS C:\Users\na-taniguchi\practice> git log
commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1 (HEAD -> main, origin/main)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Mon Oct 21 14:55:51 2024 +0900

    my_first_commit
set mark: ...skipping...
commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1 (HEAD -> main, origin/main)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Mon Oct 21 14:55:51 2024 +0900

    my_first_commit
...skipping...
~
~
~
~
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Mon Oct 21 14:55:51 2024 +0900

    my_first_commit
PS C:\Users\na-taniguchi\practice>
PS C:\Users\na-taniguchi\practice>
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice> 
 *  履歴が復元されました 

On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        modified:   app.py
        modified:   memo/memo.ipynb
        modified:   simple_amedas.ipynb

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a
        amedas/DELETE FROM t_weather_log.sql

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice>





  (use "git add <file>..." to include in what will be committed)
        a
        amedas/DELETE FROM t_weather_log.sql

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice>

  (use "git add <file>..." to include in what will be committed)
        a
        amedas/DELETE FROM t_weather_log.sql

no changes added to commit (use "git add" and/or "git commit -a")
  (use "git add <file>..." to include in what will be committed)
        a
        amedas/DELETE FROM t_weather_log.sql

  (use "git add <file>..." to include in what will be committed)
        a
        amedas/DELETE FROM t_weather_log.sql
  (use "git add <file>..." to include in what will be committed)
        a
  (use "git add <file>..." to include in what will be committed)
  (use "git add <file>..." to include in what will be committed)
        a
        amedas/DELETE FROM t_weather_log.sql
no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice> git restore memo/memo.ipynb
PS C:\Users\na-taniguchi\practice> git restore simple_amedas.ipynb
PS C:\Users\na-taniguchi\practice> git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        modified:   app.py

Untracked files:
        a
        amedas/DELETE FROM t_weather_log.sql

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice> git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   amedas/amedas_db.py
        modified:   app.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        amedas/DELETE FROM t_weather_log.sql

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice> git status  
On branch main
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        modified:   app.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice> git commit -m "debug_db追加"
On branch main
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        modified:   app.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice> git status
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   .gitignore
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        modified:   app.py
no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\na-taniguchi\practice> git add .
PS C:\Users\na-taniguchi\practice> git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .gitignore
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        modified:   app.py

[main 0ebb8dc] debug_db追加
 4 files changed, 89 insertions(+), 20 deletions(-)
PS C:\Users\na-taniguchi\practice> git logs
git: 'logs' is not a git command. See 'git --help'.

The most similar command is
        log
PS C:\Users\na-taniguchi\practice> git log
commit 0ebb8dcc5a9d3bfc52d2776038fda05ccfe1c5d8 (HEAD -> main)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Wed Oct 30 12:41:37 2024 +0900

Date:   Wed Oct 30 12:41:37 2024 +0900

    debug_db追加


    debug_db追加

    debug_db追加

commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1 (origin/main)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Mon Oct 21 14:55:51 2024 +0900

commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1 (origin/main)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Mon Oct 21 14:55:51 2024 +0900


    my_first_commit
    my_first_commit
PS C:\Users\na-taniguchi\practice> git push origin main
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.47 KiB | 375.00 KiB/s, done.
Total 7 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
To https://github.com/redstarht/amedas.git
   7f3c8c1..0ebb8dc  main -> main
PS C:\Users\na-taniguchi\practice>