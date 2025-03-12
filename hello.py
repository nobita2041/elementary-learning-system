import asyncio
from agents import Agent, Runner

async def main():
    agent = Agent(
        name="Hello World",
        instructions="You are a helpful agent.",
    )

    # ストリーミング実行
    result = Runner.run_streamed(agent, input="Hello, how are you?")
    async for event in result.stream_events():
        if event.type == "raw_response_event":
            # 生のレスポンスイベントを処理
            print(event.data.delta, end="", flush=True)
        elif event.type == "run_item_stream_event":
            # アイテムが生成されたときの処理
            print(f"Generated item: {event.item.output}")

if __name__ == "__main__":
    asyncio.run(main())

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.