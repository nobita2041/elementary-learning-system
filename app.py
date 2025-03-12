import streamlit as st
import asyncio
import os
from typing import List, Dict, Tuple
from agents import Agent, Runner
import time

# タイトルとヘッダーの設定
st.set_page_config(page_title="教科横断型学習システム", page_icon="📚")
st.title("教科横断型学習システム")
st.subheader("いろんな先生に質問してみよう！")

# 各教科エージェントの実装
math_agent = Agent(
    name="Math Teacher",
    handoff_description="数学的な問題、計算、図形、数量関係などに関する質問",
    instructions="""
    あなたは小学校6年生向けの数学の先生です。
    - 問題の数学的な側面に注目して説明してください
    - 計算や図形の考え方を分かりやすく説明してください
    - 具体例を使って説明してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

science_agent = Agent(
    name="Science Teacher",
    handoff_description="自然科学、生物、物理、化学、天体などに関する質問",
    instructions="""
    あなたは小学校6年生向けの理科の先生です。
    - 自然現象や科学的な原理を説明してください
    - 実験や観察を通じた理解を促してください
    - 身近な例を使って説明してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

social_agent = Agent(
    name="Social Studies Teacher",
    handoff_description="歴史、地理、政治、経済、文化などの社会的な質問",
    instructions="""
    あなたは小学校6年生向けの社会科の先生です。
    - 歴史的な出来事や社会の仕組みを説明してください
    - 地理や文化的な背景も含めて説明してください
    - 現代との関連性を示してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

language_agent = Agent(
    name="Japanese Teacher",
    handoff_description="国語、言葉の使い方、読解、作文、表現などに関する質問",
    instructions="""
    あなたは小学校6年生向けの国語の先生です。
    - 言葉の意味や使い方を分かりやすく説明してください
    - 文章の読み方や書き方のコツを教えてください
    - 日本語の特徴や美しさを伝えてください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

english_agent = Agent(
    name="English Teacher",
    handoff_description="英語、外国語、国際コミュニケーションに関する質問",
    instructions="""
    あなたは小学校6年生向けの英語の先生です。
    - 英単語や表現を分かりやすく説明してください
    - 日本語との違いや共通点を示してください
    - 実際に使える簡単な英会話を教えてください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

art_agent = Agent(
    name="Art Teacher",
    handoff_description="美術、絵画、工作、デザイン、色彩などの芸術的な質問",
    instructions="""
    あなたは小学校6年生向けの図工・美術の先生です。
    - 絵の描き方や工作の作り方を説明してください
    - 色や形の使い方、表現方法を教えてください
    - 有名な芸術作品や芸術家について紹介してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

music_agent = Agent(
    name="Music Teacher",
    handoff_description="音楽、楽器、歌、リズム、音楽史などに関する質問",
    instructions="""
    あなたは小学校6年生向けの音楽の先生です。
    - 音楽の基礎知識や楽器の演奏方法を説明してください
    - 歌の歌い方やリズムの取り方を教えてください
    - 様々な音楽のジャンルや音楽家について紹介してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

pe_agent = Agent(
    name="PE Teacher",
    handoff_description="体育、スポーツ、運動、健康、身体の仕組みに関する質問",
    instructions="""
    あなたは小学校6年生向けの体育の先生です。
    - 運動の仕方やスポーツのルールを説明してください
    - 体の動かし方や健康維持の方法を教えてください
    - 様々なスポーツの特徴や歴史について紹介してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

tech_agent = Agent(
    name="Technology Teacher",
    handoff_description="情報技術、コンピュータ、プログラミング、デジタル機器に関する質問",
    instructions="""
    あなたは小学校6年生向けの情報・技術の先生です。
    - コンピュータやインターネットの仕組みを説明してください
    - プログラミングの基礎や考え方を教えてください
    - デジタル機器の使い方や注意点を紹介してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

life_agent = Agent(
    name="Life Skills Teacher",
    handoff_description="家庭科、生活習慣、料理、裁縫、家事などの日常生活に関する質問",
    instructions="""
    あなたは小学校6年生向けの家庭科・生活の先生です。
    - 料理の作り方や栄養について説明してください
    - 裁縫や手芸の方法を教えてください
    - 日常生活のマナーや習慣について紹介してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

environment_agent = Agent(
    name="Environmental Studies Teacher",
    handoff_description="環境問題、自然保護、エコロジー、持続可能性に関する質問",
    instructions="""
    あなたは小学校6年生向けの環境学習の先生です。
    - 環境問題の原因と影響を分かりやすく説明してください
    - 自然保護や資源の大切さを教えてください
    - 身近にできるエコ活動を紹介してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

ethics_agent = Agent(
    name="Ethics Teacher",
    handoff_description="道徳、倫理、人間関係、思いやり、価値観に関する質問",
    instructions="""
    あなたは小学校6年生向けの道徳・倫理の先生です。
    - 思いやりや協力の大切さを説明してください
    - 友達との関わり方や問題解決の方法を教えてください
    - 様々な価値観や考え方について紹介してください
    - 小学校6年生が理解できる言葉を使ってください
    """,
)

# 各エージェントと関連キーワードのリスト
AGENT_KEYWORDS = [
    (math_agent, ["計算", "数学", "図形", "割合", "グラフ", "数字"]),
    (science_agent, ["実験", "自然", "生物", "天気", "植物", "動物", "科学", "宇宙"]),
    (social_agent, ["歴史", "地理", "文化", "政治", "経済", "社会", "国", "地域"]),
    (language_agent, ["言葉", "国語", "読解", "作文", "表現", "物語", "小説"]),
    (english_agent, ["英語", "外国語", "英単語", "国際", "外国"]),
    (art_agent, ["絵", "図工", "美術", "デザイン", "色", "工作"]),
    (music_agent, ["音楽", "楽器", "歌", "リズム", "メロディ"]),
    (pe_agent, ["体育", "スポーツ", "運動", "健康", "体"]),
    (tech_agent, ["コンピュータ", "プログラミング", "インターネット", "デジタル", "技術"]),
    (life_agent, ["家庭", "料理", "裁縫", "生活", "家事"]),
    (environment_agent, ["環境", "自然保護", "エコ", "地球", "リサイクル"]),
    (ethics_agent, ["道徳", "友達", "協力", "思いやり", "人間関係"])
]

# 教科エージェントの名前と日本語名のマッピング
AGENT_JAPANESE_NAMES = {
    "Math Teacher": "算数の先生",
    "Science Teacher": "理科の先生",
    "Social Studies Teacher": "社会の先生",
    "Japanese Teacher": "国語の先生",
    "English Teacher": "英語の先生",
    "Art Teacher": "図工の先生",
    "Music Teacher": "音楽の先生",
    "PE Teacher": "体育の先生",
    "Technology Teacher": "情報の先生",
    "Life Skills Teacher": "家庭科の先生",
    "Environmental Studies Teacher": "環境学習の先生",
    "Ethics Teacher": "道徳の先生"
}

async def select_relevant_agents(question: str) -> List[Agent]:
    """
    質問に関連する3つの教科エージェントを選択します
    """
    # 各エージェントのスコアを計算
    agent_scores = []
    for agent, keywords in AGENT_KEYWORDS:
        score = 0
        for keyword in keywords:
            if keyword in question:
                score += 1
        agent_scores.append((agent, score))
    
    # スコアが高い順にエージェントをソート
    sorted_agents = sorted(agent_scores, key=lambda x: x[1], reverse=True)
    
    # 上位のエージェントを選択（スコアが0より大きいもののみ）
    selected_agents = [agent for agent, score in sorted_agents if score > 0]
    
    # 選択されたエージェントが3つ未満の場合、デフォルトのエージェントを追加
    if len(selected_agents) < 3:
        # スコアが0のエージェントも含めて上位から選択
        all_agents = [agent for agent, _ in sorted_agents]
        
        # すでに選択されているエージェント以外から追加
        for agent in all_agents:
            if agent not in selected_agents:
                selected_agents.append(agent)
                if len(selected_agents) >= 3:
                    break
        
        # それでも3つに満たない場合（通常はここには来ないはず）
        default_agents = [social_agent, science_agent, language_agent]
        for agent in default_agents:
            if agent not in selected_agents:
                selected_agents.append(agent)
                if len(selected_agents) >= 3:
                    break
    
    # 常に3つのエージェントを返す
    return selected_agents[:3]

async def process_question_streaming(question: str, placeholder):
    """
    生徒からの質問を処理し、ストリーミングで回答を表示します
    """
    # 関連する教科エージェントを選択
    relevant_agents = await select_relevant_agents(question)
    
    # 各エージェントからの回答を収集
    responses = []
    agent_names = []
    
    # 教科別の先生を紹介するコメント
    intro = f"この質問には、{', '.join([AGENT_JAPANESE_NAMES.get(agent.name, agent.name) for agent in relevant_agents])}に聞いてみました！それぞれの先生からの回答です。\n\n"
    placeholder.markdown(intro)
    
    for agent in relevant_agents:
        agent_name = AGENT_JAPANESE_NAMES.get(agent.name, agent.name)
        agent_names.append(agent_name)
        
        # 先生の名前を表示
        placeholder.markdown(f"# {agent_name}からの回答\n回答を生成中...")
        
        # エージェントからの回答を取得
        result = await Runner.run(agent, input=question)
        
        # 回答を段階的に表示（文字単位でアニメーション効果）
        response_text = result.final_output
        displayed_text = ""
        
        for char in response_text:
            displayed_text += char
            placeholder.markdown(f"# {agent_name}からの回答\n{displayed_text}")
            time.sleep(0.01)  # 表示速度の調整
        
        responses.append(f"# {agent_name}からの回答\n{result.final_output}")
    
    # 総合的な回答の生成
    final_response = intro + "\n\n".join(responses)
    return final_response

async def process_question(question: str) -> str:
    """
    生徒からの質問を処理し、3つの教科の視点から総合的な回答を生成します
    """
    # 関連する教科エージェントを選択
    relevant_agents = await select_relevant_agents(question)
    
    # 各エージェントからの回答を収集
    responses = []
    agent_names = []
    
    for agent in relevant_agents:
        result = await Runner.run(agent, input=question)
        agent_name = AGENT_JAPANESE_NAMES.get(agent.name, agent.name)
        agent_names.append(agent_name)
        responses.append(f"# {agent_name}からの回答\n{result.final_output}")
    
    # 教科別の先生を紹介するコメント
    intro = f"この質問には、{', '.join(agent_names)}に聞いてみました！それぞれの先生からの回答です。\n\n"
    
    # 総合的な回答の生成
    final_response = intro + "\n\n".join(responses)
    return final_response

# サンプル質問の提供
sample_questions = [
    "虹はどうしてできるの？",
    "日本の米作りについて教えてください",
    "分数のかけ算はどうやるの？",
    "地球温暖化とはなんですか？",
    "友達とケンカしたときはどうしたらいい？",
    "コンピュータはどうやって動くの？"
]

# サイドバーにAPIキー入力欄を追加
st.sidebar.title("設定")
api_key = st.sidebar.text_input("OpenAI APIキー", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# ストリーミングモードの切り替え
streaming_mode = st.sidebar.checkbox("ストリーミングモード", value=True, help="回答をリアルタイムで表示します")

# サイドバーにサンプル質問を表示
st.sidebar.title("サンプル質問")
for q in sample_questions:
    if st.sidebar.button(q):
        st.session_state.question = q

# 質問入力欄
if "question" not in st.session_state:
    st.session_state.question = ""
if "answer" not in st.session_state:
    st.session_state.answer = ""

question = st.text_input("質問を入力してください", value=st.session_state.question)

# 回答表示用のプレースホルダー
answer_placeholder = st.empty()

# 質問送信ボタン
if st.button("質問する"):
    if not api_key:
        st.error("OpenAI APIキーを入力してください")
    elif not question:
        st.warning("質問を入力してください")
    else:
        # 回答をリセット
        st.session_state.answer = ""
        
        if streaming_mode:
            # ストリーミングモードで回答を表示
            with st.spinner("先生たちが考えています..."):
                # 非同期関数を実行するためのヘルパー関数
                async def get_streaming_answer():
                    return await process_question_streaming(question, answer_placeholder)
                
                # 非同期関数を実行
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                answer = loop.run_until_complete(get_streaming_answer())
                loop.close()
                
                st.session_state.answer = answer
        else:
            # 通常モードで回答を表示
            with st.spinner("先生たちが考えています..."):
                # 非同期関数を実行するためのヘルパー関数
                async def get_answer():
                    return await process_question(question)
                
                # 非同期関数を実行
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                answer = loop.run_until_complete(get_answer())
                loop.close()
                
                st.session_state.answer = answer
                answer_placeholder.markdown(answer)

# フッター
st.markdown("---")
st.markdown("© 2024 教科横断型学習システム") 