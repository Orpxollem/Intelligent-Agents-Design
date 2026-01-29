import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


class BasicAgent(Agent):
    class HelloBehaviour(CyclicBehaviour):
        async def run(self):
            print(f"<> Agent {self.agent.jid} is running...")
            await asyncio.sleep(5)

    async def setup(self):
        print(">> Starting BasicAgent...")
        self.add_behaviour(self.HelloBehaviour())


async def main():
    jid = "basicagent@localhost"
    password = "basicpass"

    agent = BasicAgent(jid, password)
    
    agent.verify_security = False 
    
    await agent.start(auto_register=False)

    print(">> Agent started successfully. Press Ctrl+C to stop.")
    while agent.is_alive():
        await asyncio.sleep(1)

    await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
