commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1 (origin/main)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Mon Oct 21 14:55:51 2024 +0900

    my_first_commit
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Compressing objects: 100% (7/7), done.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.47 KiB | 375.00 KiB/s, done.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.47 KiB | 375.00 KiB/s, done.   
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 1.47 KiB | 375.00 KiB/s, done. 
Writing objects: 100% (7/7), 1.47 KiB | 375.00 KiB/s, do
ne.
Writing objects: 100% (7/7), 1.47 KiB | 375.00 KiB/s,
 done.
Writing objects: 100% (7/7), 1.47 KiB | 375.00 KiB/
s, done.
Total 7 (delta 5), reused 0 (delta 0), pack-reused 
0 (from 0)
remote: Resolving deltas: 100% (5/5), completed wit
h 5 local objects.
it
   7f3c8c1..0ebb8dc  main -> main
PS C:\Users\na-taniguchi\practice>

 *  履歴が復元されました 
PS C:\Users\na-taniguchi\practice>
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice> 
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice> 
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice>
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice>
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice> 
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice>
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice>
 *  履歴が復元されました 

PS C:\Users\na-taniguchi\practice> git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        modified:   app.py
        new file:   memo/gitmemo.md
        modified:   memo/memo.ipynb
        new file:   templates/amedas.html
        modified:   templates/index.html

PS C:\Users\na-taniguchi\practice> git restore --staged memo/gitmemo.md       
PS C:\Users\na-taniguchi\practice> git status
On branch main
  (use "git restore --staged <file>..." to unstage)
        modified:   amedas/amedas.py
        modified:   amedas/amedas_db.py
        new file:   templates/amedas.html
        modified:   templates/index.html

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

PS C:\Users\na-taniguchi\practice> git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
PS C:\Users\na-taniguchi\practice> git add .
PS C:\Users\na-taniguchi\practice> git status
On branch main
  (use "git restore --staged <file>..." to unstage)
        modified:   .gitignore
        modified:   amedas/amedas_db.py
        modified:   app.py
        modified:   memo/memo.ipynb
        new file:   templates/amedas.html
        modified:   templates/index.html

PS C:\Users\na-taniguchi\practice> git commit    
[main 408db42] 2024/11/7
 7 files changed, 285 insertions(+), 137 deletions(-)
 create mode 100644 templates/amedas.html
PS C:\Users\na-taniguchi\practice> git status
On branch main
nothing to commit, working tree clean
PS C:\Users\na-taniguchi\practice> git log
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Thu Nov 7 13:18:02 2024 +0900


commit 0ebb8dcc5a9d3bfc52d2776038fda05ccfe1c5d8 (origin/main)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Wed Oct 30 12:41:37 2024 +0900

    debug_db追加

commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1
PS C:\Users\na-taniguchi\practice> git pull origin main
From https://github.com/redstarht/amedas
 * branch            main       -> FETCH_HEAD
Already up to date.
PS C:\Users\na-taniguchi\practice> git push
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin main
To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

PS C:\Users\na-taniguchi\practice> git push origin main
Enumerating objects: 22, done.
Counting objects: 100% (22/22), done.
Delta compression using up to 8 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (12/12), 4.43 KiB | 454.00 KiB/s, done.
Total 12 (delta 8), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (8/8), completed with 8 local objects.
To https://github.com/redstarht/amedas.git
   0ebb8dc..408db42  main -> main
PS C:\Users\na-taniguchi\practice> git log 
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Thu Nov 7 13:18:02 2024 +0900


commit 0ebb8dcc5a9d3bfc52d2776038fda05ccfe1c5d8
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Wed Oct 30 12:41:37 2024 +0900

    debug_db追加

commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1
Author: redstarht <185753202+redstarht@users.noreply.github.com>
PS C:\Users\na-taniguchi\practice> git log --oneline
408db42 (HEAD -> main, origin/main) 2024/11/7
0ebb8dc debug_db追加
7f3c8c1 my_first_commit
PS C:\Users\na-taniguchi\practice> git log --oneline --graph
* 408db42 (HEAD -> main, origin/main) 2024/11/7
* 0ebb8dc debug_db追加
* 7f3c8c1 my_first_commit