## step1 
stable diffusion,novelaiで漫画1ページを描画してもらうような、タグを作成してください、カラーのページにしたいです。
nanobanana, GptImage1のようなツールでもそのまま使えることを考えています。
タグ生成の際にはmanga_tag.mdも確認し参考にしてください
タグを付けるとき、誰が、どのような体勢で、誰に、背景はこう、のようなことを各コマで明確にしてください。
メッセージは日本語で応対してください
あと、内容については、3-7コマで、済むような形で。使った場所を教えてください
英語のタグに日本語の翻訳を後に追加してください。喋るコマの場合は吹き出しだけ日本語を入れるようにしてください。
各コマのタグを個別に出すようにして､最後にそれを束ねて全ページを一気に出す形にしてください。
1コマコマごとに場所 (Location),人の状態 (Characters' States),行っているアクション (Actions)などを明確にしてください。
誰の何にどうしたといったことは、文章で表記してください。

構図の工夫、アオリとフカン、アップとヒキなども適切にコマのメリハリを付けるのに入れてください。
ここではimagineで決して画像を生成しないでください。
日本の漫画のコマ割りについては必ず指定してください

「自然言語で状況説明＋箇条書きでコマを並べる」スタイル
```
## step1 
縦長マンガ、1ページ6〜8コマ、少年ジャンプ風の迫力あるバトルシーン、日本の漫画のコマ割り
登場人物：黒髪の剣士「零」（傷だらけ、目が鋭い）、金髪の魔法使い少女「ルナ」

コマ1: 見開き大ゴマ気味、零が剣を構えて敵の群れを睨む、背景に炎、迫力重視
セリフ：「来い…全部まとめて斬ってやる」
tag:  
dynamic wide angle manga panel, shonen jump style, dramatic low angle shot, black-haired scarred swordsman Rei gripping sword tightly, sharp intense eyes glaring forward, surrounded by shadowy enemy horde, blazing fire background, intense atmosphere, action manga, detailed lineart, speed lines, high contrast, epic battle opening scene

コマ2: ルナが後ろで魔法陣を展開、青い光エフェクト
セリフ：「零！援護するよ！」
tag:  
shonen manga style, beautiful blonde magical girl Luna standing behind, casting large glowing blue magic circle, intricate rune patterns, cyan light particles and sparkles, determined expression, wind blowing hair, support magic scene, dramatic backlighting, detailed magical effects, anime screentone

コマ3〜5: 連続アクション（斬撃→爆発→敵の悲鳴）
tag:  
fast-paced action sequence, 3 consecutive manga panels in one image, dynamic speed lines,  
panel1: Rei performing powerful diagonal sword slash, motion blur, impact frame, black hair flowing,  
panel2: massive explosion of fire and smoke after slash connects, debris flying,  
panel3: enemies screaming in pain, distorted faces, being blown away, dramatic shading, shonen jump battle intensity, monochrome + selective color, kinetic energy

コマ6: 零が血まみれで立っている、ルナが駆け寄る、決めポーズ
tag:  
final victory pose manga panel, shonen jump climax scene, bloodied black-haired swordsman Rei standing tall breathing heavily, sword planted in ground, sharp eyes looking forward, wounds and torn clothes, blonde magical girl Luna running towards him worriedly, reaching out, dramatic back view of enemies defeated in background, dust and smoke, powerful atmosphere, detailed shading, heroic moment, intense emotion

```

## step2 
nanobanana, GptImage1のようなツールで、コマ割りと抽象度をのみ出す形
抽象度を上げる、「何をしている」という具体的な行動や接触描写を排除し、純粋に構図・位置関係・アングル・表情の配置だけに絞る
日本の漫画のコマ割りについては必ず指定してください

以下のような出力でお願いします

```
## step2 
縦長カラーマンガ、1ページ5コマ、日本の漫画のコマ割り

コマ1: フカンlong shot、1人の男性に３人(A,B,C)女性が集まる

コマ2: アオリclose up、Aが中心の人物に近づく

コマ3: 横アングルmedium shot、Bが背後から中心の人物に近づく

コマ4: eye level dynamic、Cが右側から中心の人物に近づく

コマ5: Dutch angle bust up大コマ、ABCに囲まれた、真ん中の人物が笑顔になる
```


