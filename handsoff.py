from agents import Agent, Runner
import asyncio

# スペイン語
spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
)

# 英語
english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)

# 日本語
japanese_agent = Agent(
    name="Japanese agent",
    instructions="You only speak Japanese.",
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent, japanese_agent],
)


async def main():
    result = await Runner.run(triage_agent, input="こんにちは、お元気ですか？")
    print(result.final_output)
    # こんにちは、お元気ですか？


if __name__ == "__main__":
    asyncio.run(main())
