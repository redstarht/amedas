以下のコマンドを実行して、Git に名前とメールアドレスを設定しましょう。

1. 全体に適用する場合（--global を付ける）
Git を使うすべてのリポジトリで同じユーザー情報を使う場合は、--global オプションを付けて設定します：

```bash
コードをコピーする
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
上記のコマンドを実行すると、以降はこの PC で Git を使うすべてのリポジトリに、指定したユーザー情報が適用されます。

2. 特定のリポジトリだけに適用する場合
特定のリポジトリにだけユーザー情報を設定したい場合は、--global を省略して以下のように実行します：

```bash
コードをコピーする
git config user.name "Your Name"
git config user.email "your-email@example.com"
```
これにより、現在のリポジトリ内でのみ設定が適用されます。

設定の確認
設定した内容を確認したい場合は、以下のコマンドで現在のユーザー情報を確認できます：

```bash
コードをコピーする
git config --list
```
または特定の設定を確認したい場合は、以下のように指定します：

```bash
コードをコピーする
git config user.name
git config user.email
これでユーザー情報が正しく設定され、コミットを実行できるようになります。
```