class BaseAgent:
    def __init__(self, agent_id, required_units):
        self.agent_id = agent_id
        self.required_units = required_units
        self.state = "READY"
        self.received_ack = False
        self.memory = []  # Log of received messages

    def record_interaction(self, msg):
        self.memory.append(msg)

    def has_seen(self, msg_type):
        return any(m["type"] == msg_type for m in self.memory)

    def run(self, resource_pool, ipc, tick):
        msg = ipc.receive(self.agent_id)
        if msg:
            self.record_interaction(msg)

            if msg["type"] == "DATA_REQ":
                print(f"[{self.agent_id}] Got DATA_REQ → sending ACK.")
                ipc.send(self.agent_id, msg["sender"], "Acknowledged", "ACK", priority=1, tick=tick)
                self.state = "RESPONDING"

            elif msg["type"] == "ACK":
                print(f"[{self.agent_id}] Got ACK → sending EXEC.")
                ipc.send(self.agent_id, msg["sender"], "Executing task now.", "EXEC", priority=1, tick=tick)
                self.received_ack = True

            elif msg["type"] == "EXEC":
                print(f"[{self.agent_id}] Received EXEC → marking peer as active.")

        elif not self.received_ack:
            target = "A2" if self.agent_id == "A1" else "A1"
            print(f"[{self.agent_id}] Sending DATA_REQ to {target}")
            ipc.send(self.agent_id, target, "Requesting permission to run.", "DATA_REQ", priority=2, tick=tick)
            self.state = "WAITING_FOR_ACK"

        elif resource_pool.request(self.agent_id, self.required_units):
            print(f"[{self.agent_id}] Got resources → Running task.")
            self.state = "RUNNING"
            resource_pool.release(self.agent_id, self.required_units)
            self.state = "COMPLETED"

        else:
            self.state = "BLOCKED"
