'''bash
PS C:\Users\DELL\z\dev\amedas> git status
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
PS C:\Users\DELL\z\dev\amedas> git log
commit 408db42e230a23ca79e08d4277f6c2ada68fb730 (HEAD -> main, origin/main, origin/HEAD)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Thu Nov 7 13:18:02 2024 +0900

    2024/11/7

commit 0ebb8dcc5a9d3bfc52d2776038fda05ccfe1c5d8
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Wed Oct 30 12:41:37 2024 +0900

    debug_db追加
commit 7f3c8c13c34d7a98d81fecf98d61d465c914f2c1
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Mon Oct 21 14:55:51 2024 +0900

    my_first_commit
PS C:\Users\DELL\z\dev\amedas> git pull
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 6 (delta 4), reused 6 (delta 4), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 2.46 KiB | 41.00 KiB/s, done.
From https://github.com/redstarht/amedas
   408db42..a64eba5  main       -> origin/main
Updating 408db42..a64eba5
Fast-forward
 .gitignore       |   3 +-
 memo/gitmemo.md  | 193 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
 memo/gitmemo2.md | 155 ++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 349 insertions(+), 2 deletions(-)
 create mode 100644 memo/gitmemo.md
 create mode 100644 memo/gitmemo2.md
PS C:\Users\DELL\z\dev\amedas> git log
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
commit a64eba54a838dfa39dca0cea8f33615f616332bf (HEAD -> main, origin/main, origin/HEAD)
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Thu Nov 7 13:42:57 2024 +0900

    2024/11/7 change .gitignore *md

commit 408db42e230a23ca79e08d4277f6c2ada68fb730
Author: redstarht <185753202+redstarht@users.noreply.github.com>
Date:   Thu Nov 7 13:18:02 2024 +0900
'''