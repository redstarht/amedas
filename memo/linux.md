## memo

```bash
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

tani@sngfa-c:~$ cd /contents/
tani@sngfa-c:/contents$ mkdir tani
tani@sngfa-c:/contents$ ll
total 116
drwxrwx--- 19 root dev   4096 Nov  7 16:07 ./
drwxr-xr-x 21 root root  4096 May 10 14:14 ../
drwxrwxr-x  3 tnk  tnk   4096 Oct 25 12:37 app-y-hydro2500/
drwxrwxr-x  3 krc  krc   4096 Jul 18 11:14 krc_test/
drwx------  2 root dev  16384 Jan 25  2024 lost+found/
-rw-rw-r--  1 tnk  tnk  26089 Mar 14  2024 mqtt_log
drwxrwxr-x  2 tani tani  4096 Nov  7 16:07 tani/
drwxrwx---  3 root dev   4096 Mar 14  2024 tmp/
drwxrwxr-x  3 tnk  tnk   4096 Jun  7 16:04 try_app-junsou/
drwxrwx---  3 tnk  tnk   4096 Mar 13  2024 try_broker/
drwxrwxr-x  4 root dev   4096 Feb  6  2024 try_compose/
drwxrwxr-x  3 tnk  tnk   4096 Feb 16  2024 try_db/
drwxrwx---  3 root dev   4096 Feb  1  2024 try_nginx/
drwxrwxr-x  3 tnk  tnk   4096 Feb 15  2024 try_publish/
drwxrwxr-x  3 tnk  tnk   4096 Mar 13  2024 try_subscriber/
drwxrwxr-x  3 tnk  tnk   4096 Apr  2  2024 try_tran_a/
drwxrwxr-x  3 tnk  tnk   4096 Apr  4  2024 try_tran_b/
drwxrwxr-x  3 tnk  tnk   4096 Mar 29  2024 try_tran_c/
drwxrwxr-x  3 tnk  tnk   4096 Mar 28  2024 try_xcdb/
drwxrwxr-x  2 krc  dev   4096 Feb 16  2024 .vscode/
tani@sngfa-c:/contents$ cd tani/
tani@sngfa-c:/contents/tani$ touch myfile
tani@sngfa-c:/contents/tani$ ll
total 8
drwxrwxr-x  2 tani tani 4096 Nov  7 16:08 ./
drwxrwx--- 19 root dev  4096 Nov  7 16:07 ../
-rw-rw-r--  1 tani tani    0 Nov  7 16:08 myfile
tani@sngfa-c:/contents/tani$ vi myfile
tani@sngfa-c:/contents/tani$ cat myfile
fghfdkjs
tani@sngfa-c:/contents/tani$ chmod 666 myfile
tani@sngfa-c:/contents/tani$ ll
total 12
drwxrwxr-x  2 tani tani 4096 Nov  7 16:09 ./
drwxrwx--- 19 root dev  4096 Nov  7 16:07 ../
-rw-rw-rw-  1 tani tani    9 Nov  7 16:09 myfile
tani@sngfa-c:/contents/tani$ chown tani:dev myfile
tani@sngfa-c:/contents/tani$ ll
total 12
drwxrwxr-x  2 tani tani 4096 Nov  7 16:09 ./
drwxrwx--- 19 root dev  4096 Nov  7 16:07 ../
-rw-rw-rw-  1 tani dev    27 Nov  7 16:14 myfile
tani@sngfa-c:/contents/tani$ groups tani
tani : tani sudo dev docker
tani@sngfa-c:/contents/tani$ 
```