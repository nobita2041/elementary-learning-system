# 教科横断型学習システム

教科横断型問題解決をサポートするAIシステムです。様々な教科の視点から質問に回答します。

## 特徴

- 12の教科エージェント（算数、理科、社会、国語、英語、図工、音楽、体育、情報、家庭科、環境学習、道徳）
- 質問内容に応じて最適な2〜3つの教科の視点から回答
- 小学校6年生に適した説明レベル
- 教科間のつながりを意識した総合的な説明
- Streamlitを使用したWebインターフェース

## セットアップ

1. リポジトリをクローン
```bash
git clone https://github.com/yourusername/cross-subject-learning-system.git
cd cross-subject-learning-system
```

2. 仮想環境のセットアップ
```bash
uv venv
source .venv/bin/activate  # Windowsの場合: .venv\Scripts\activate
```

3. 依存パッケージのインストール
```bash
uv pip install -r requirements.txt
```

4. OpenAI APIキーの設定
APIキーはWebインターフェースで入力するか、環境変数として設定できます。
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## 使い方

1. Streamlitアプリケーションの起動
```bash
streamlit run app.py
```

2. ブラウザで http://localhost:8501 にアクセス

3. サイドバーにOpenAI APIキーを入力

4. 質問を入力するか、サンプル質問から選択

5. 「質問する」ボタンをクリックして回答を取得

## 対応している教科

- 算数：計算、図形、割合などの数学的概念
- 理科：自然現象、実験、生物などの科学的概念
- 社会：歴史、地理、文化などの社会的概念
- 国語：言葉の使い方、読解、作文など
- 英語：英単語、表現、国際コミュニケーション
- 図工：絵画、工作、デザイン、色彩など
- 音楽：楽器、歌、リズム、音楽史など
- 体育：スポーツ、運動、健康、身体の仕組み
- 情報：コンピュータ、プログラミング、デジタル機器
- 家庭科：料理、裁縫、生活習慣など
- 環境学習：環境問題、自然保護、エコロジー
- 道徳：人間関係、思いやり、価値観など

## 技術スタック

- Python
- OpenAI Agents SDK
- Streamlit
- asyncio

## ライセンス

MIT

## 注意事項

- OpenAI APIキーが必要です
- 教育目的での使用を想定しています
- 小学校6年生向けの説明レベルに調整されています 