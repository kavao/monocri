## step1 
stable diffusion,novelaiで漫画1ページを描画してもらうような、タグを作成してください、カラーのページにしたいです。
タグ生成の際にはmanga_tag.mdも確認し参考にしてください
タグを付けるとき、誰が、どのような体勢で、誰に、背景はこう、のようなことを各コマで明確にしてください。
メッセージは日本語で応対してください
あと、内容については、3-5コマで、済むような形で。使った場所を教えてください
英語のタグに日本語の翻訳を後に追加してください。喋るコマの場合は吹き出しだけ日本語を入れるようにしてください。
各コマのタグを個別に出すようにして､最後にそれを束ねて全ページを一気に出す形にしてください。
1コマコマごとに場所 (Location),人の状態 (Characters' States),行っているアクション (Actions)などを明確にしてください。
誰の何にどうしたといったことは、文章で表記してください。

構図の工夫、アオリとフカン、アップとヒキなども適切にコマのメリハリを付けるのに入れてください。
ここではimagineで決して画像を生成しないでください。

## step2 最終出力：JSON風フォーマット（一括生成・管理用）
人間が読むための構成案（Step 1）が確定したら、プログラムや外部ツールで一括生成・管理するためのJSON形式（Step 2） でひきつづき出力してください。
このJSONには、すべてのコマのプロンプトが「共通タグ」と「個別タグ」が結合された状態で格納されます。ネガティブプロンプトは除外します。
jsonは各ページごとに繰り返し作成します。

### JSONスキーマ例
```json
{
  "title": "作品タイトル",
  "style_preset": "画風タグ（共通）",
  "character_presets": {
    "char_key": "キャラ共通タグ"
  },
  "panels": [
    {
      "panel_id": 1,
      "prompt": "【ここに生成用の全タグ（画風+キャラ+構図+状況）をカンマ区切りで結合して入れる,セリフも入れる】",
    }
  ]
}
```
※ `prompt` フィールドには、ユーザーがそのままAI画像生成ツールにコピペして使える完全なタグ列を入れてください。

## step3 コマ割 追加出力
Step2 で出力した `panels.panel_id` と対応する、**レイアウト専用のJSON** を追加で出力してください。
このJSONは、nanobanana pro などのツールで「コマ割レイアウトとコマ番号だけ」を再現するための抽象レイヤーとして利用します。

* **必ずJSON形式のみ**を出力してください。説明文は不要です。
* 各ページごとに以下のスキーマで出力してください。
* ストーリーの詳細や台詞内容は Step1/2 で扱うため、ここには書かないでください。キャラクターはデッサン人形で。

```jsonc
{
  "page": 1,
  "page_size": "A4_vertical",             // ページの向きや想定サイズ（抽象でOK）
  "reading_direction": "right_to_left",    // 日本式の右→左
  "layout_unit": "normalized",             // 0.0〜1.0の正規化座標を使う
    "character_presets": {
    "char_key": "キャラ共通タグ"
  },
  "panels": [
    {
      "panel_id": 1,                       // Step2 の panel_id と一致
      "number_label": "①",                // コマ番号表示用（①,②,③など）
      "order": 1,                          // 読み順（右上が1など）
      "region": {
        "x": 0.05,                         // ページ左端を0.0, 右端を1.0とした相対座標
        "y": 0.05,                         // ページ上端を0.0, 下端を1.0とした相対座標
        "width": 0.4,
        "height": 0.25
      },
      "shot": "medium_shot",              // "close_up" / "bust_up" / "medium_shot" / "long_shot" など
      "camera_angle": "slightly_high",    // "eye_level" / "slightly_high" / "high_angle" / "slightly_low" / "low_angle"
      "composition": {
        "main_characters": ["hero"],      // 主に映るキャラID（Step2のキャラキーと対応）
        "character_placement": "left",    // left / center / right / foreground / background など
        "background_type": "office",      // 背景の抽象ラベル（office, classroom, street, sky など）
        "focus": "character",             // "character" or "background" or "object"
        "notes": "主人公を左寄りに立たせ、右奥に机の列を配置"
      },
      "balloon_layout": {
        "has_balloon": true,
        "balloon_position": "upper_right" // コマ内の吹き出し位置（upper_right / upper_left / center など）
      }
    }
  ]
}
```

* `region` は「だいたいこの辺にこのコマがある」という**抽象的な矩形位置**を表現してください。
* 数値は 0.0〜1.0 の少数にし、細かいピクセル値は使わないでください。
* `shot` / `camera_angle` / `composition` / `balloon_layout` は、**AI画像生成のタグではなく、AIがレイアウトを考えるための抽象情報**のみを記述してください。
* 各ページについて、このスキーマに沿ったJSONを1つずつ出力してください。
* 日本の漫画は原則 "reading_direction": "right_to_left" です。また、monochroはタグに入れないでください

## 3. さらに抽象化した「グリッド版」が欲しい場合

nanobanana 側で「3×3 グリッド」のような扱いをする場合は、座標の代わりにグリッドを使うバージョンもアリです。

```jsonc
{
  "page": 1,
  "page_size": "A4_vertical",
  "reading_direction": "right_to_left",
  "layout_unit": "grid",
  "grid": {
    "cols": 3,
    "rows": 3
  },
  "panels": [
    {
      "panel_id": 1,
      "number_label": "①",
      "order": 1,
      "grid_region": {
        "col_start": 2,
        "col_span": 2,
        "row_start": 1,
        "row_span": 1
      },
      "shot": "long_shot",
      "camera_angle": "eye_level",
      "composition": {
        "main_characters": ["hero"],
        "character_placement": "small_bottom_right",
        "background_type": "city",
        "focus": "background",
        "notes": "街並みの全景の中に主人公を小さく配置"
      },
      "balloon_layout": {
        "has_balloon": false
      }
    }
  ]
}
```

* `grid_region` に「どのマスからどの範囲を占有するか」だけを書き、あとはショットや角度などの**演出情報**を足すイメージです。
* 実座標が必要になったら、ツール側でグリッドから具体座標に変換できます。
