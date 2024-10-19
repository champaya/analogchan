# Analogchan へようこそ！

## 何ができるの？

**Analogchan** は、あなたの写真をレトロなドット風アートに変換するアプリです。画像をアップロードして、簡単な設定をするだけで、アスキーアートのような懐かしさを感じるアナログな表現に変わります。

![Image1](/docs/2.gif)

## 使い方はとっても簡単！

1. **画像を選ぶ**: あなたのお気に入りの写真をアップロードします。
2. **設定を選ぶ**: 解像度や色、文字の種類をカスタマイズして、仕上がりを自分好みに調整します。
3. **結果を確認**: ボタンを押して変換結果を表示し、仕上がりを楽しみましょう。

## 使い方のステップ

1. **Analogchanを開く**:
   アプリを開いたら、ホームページが表示されます。

2. **画像をアップロード**:
   「画像をアップロード」ボタンをクリックし、変換したい写真を選んでください。

3. **設定をカスタマイズ**:
   - **解像度**: 画像をどれだけ粗くするか決めます。解像度を下げると、粗い画像となるためおすすめしておりません。
   - **閾値**: 明るい部分と暗い部分の表示を調整します。値を高くするほど、暗い部分が増えます。
   - **表示色**: 結果の色を5種類から選べます（白、黒、緑、紫、オレンジ）。
   - **表示文字**: 明るい部分や暗い部分に使う文字を4種類指定できます。デフォルトの「.」「+」「*」「0」もおすすめです！

4. **結果を確認する**:
   設定が終わったら、「実行」ボタンをクリック。結果が画面に表示されます！


## アプリを使うには？

### ステップ1: dockerをインストール
このアプリはdocker上で動作します。dockerをインストールしていない場合は、[こちら](https://www.docker.com/products/docker-desktop/)からインストールしてください。
dockerを起動するとサインイン画面が表示されます。サインインもお願いします。

### ステップ2: ソースコードをダウンロード
GitHubからソースコードをダウンロードしてください。

下記のコマンドを実行してください。

```bash
git clone https://github.com/your-username/analogchan.git
```

もしくは、zipファイルをダウンロードしてください。

### ステップ3: アプリを起動
ダウンロードしたフォルダに移動して、下記のコマンドを実行してください。

```bash
docker compose up -d
```
この画面が表示されるはずです。

![Image1](/docs/1.png)

### ステップ4: アプリにアクセス

ブラウザを開いて、`http://localhost:8000` にアクセスしてください。
アプリが起動されます。

### ステップ5: アプリを終了

アプリを終了する場合は、下記のコマンドを実行してください。

```bash
docker-compose down --rmi all --volumes --remove-orphans
```

---

## よくある質問 (FAQ)

### Q: どんな画像でも使えますか？
A: はい、どんな画像でも変換できます。ただし、大きすぎる画像はPCのリソースを使いすぎるためおすすめしておりません。

### Q: 結果が思ったように表示されません。
A: 設定を色々変えてみてください。解像度や表示文字、閾値を調整すると、仕上がりが変わります。

### Q: 結果が表示されないんですが？
A: ブラウザの設定でJavaScriptが有効になっているか確認してください。それでも解決しない場合は、ページをリロードしてみてください。

### Q: アプリが起動しないんですが？
A: dockerが起動しているか確認してください。windowsの場合は、`docker desktop`が起動しているか確認してください。

---

## お問い合わせ

何か問題が発生した場合やご質問がある場合は、`issue`のご登録でお知らせください。

## ライセンス

商用目的での利用はお控えください。