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
        print(history.urls())  # ['about:blank', 'https://www.google.com/search?q=date%20today&udm=14&sei=mAzQZ_qmLLOa0PEP6u_H6Q0']
        print(history.screenshots())  # ......
        print(history.action_names())  # ['search_google', 'done']
        print(history.extracted_content())  # ['🔍  Searched for "date today" in Google', "Successfully searched Google for today's date. The date information is visible in the search results: March 11, 2025."]
        print(history.errors())  # [None, None]
        print(history.model_actions())  # [{'search_google': {'query': 'date today'}, 'interacted_element': None}, {'done': {'text': "Successfully searched Google for today's date. The date information is visible in the search results: March 11, 2025.", 'success': True}, 'interacted_element': None}]

    await browser.close()

if __name__ == "__main__":
    asyncio.run(run_agent())
    # playwright install
