import asyncio
from datetime import datetime
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from environment import get_disaster_status

class SensorAgent(Agent):
    class MonitorEnvironment(PeriodicBehaviour):
        async def run(self):
            # Acts as the percept to sense the env
            severity, value = get_disaster_status()

            # Timestamp for logs
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            
            #Logs event status
            log_entry = f"{timestamp} <<>> [Sensor] Reading: {value}cm | Status: {severity}"
            print(log_entry)

            # Text output file for event logs
            with open("disaster_event_logs.txt", "a") as f:
                f.write(log_entry + "\n")
            
            if severity == "High":
                alert = f"{timestamp} !! [ALERT] High damage severity detected!"
                print(alert)
                # Logs high disaster events into a separate log file
                with open("disaster_logs.txt", "a") as f:
                    f.write(alert + "\n")

    # Function to have the agent run every 5 seconds for updates
    async def setup(self):
        print(f">> SensorAgent {self.jid} starting environment monitoring ...")
        self.add_behaviour(self.MonitorEnvironment(period=5))

async def main():
    jid = "sensoragent@localhost"
    password = "sensorpass"

    agent = SensorAgent(jid, password)
    agent.verify_security = False
    
    await agent.start(auto_register=True)
    
    print("<> SensorAgent active. Press Ctrl+C to stop.")
    try:
        while agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())