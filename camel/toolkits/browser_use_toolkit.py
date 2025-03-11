import asyncio
from browser_use import Agent, Browser
from langchain_openai import ChatOpenAI


async def run_agent():
    browser = Browser()
    # Use specific browser context (preferred method)
    async with await browser.new_context() as context:
        agent = Agent(
            task="Search google for date today.",
            llm=ChatOpenAI(model="gpt-4o"),
            browser_context=context  # Use persistent context
        )

        # Run the agent
        history = await agent.run()
        print(history.urls())
        print(history.screenshots())
        print(history.action_names())
        print(history.extracted_content())
        print(history.errors())
        print(history.model_actions())

    await browser.close()

if __name__ == "__main__":
    asyncio.run(run_agent())
    # playwright install
