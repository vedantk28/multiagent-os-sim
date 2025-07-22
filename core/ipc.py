from collections import defaultdict
from queue import PriorityQueue
from utils.message_logger import MessageLogger

class MessageBus:
    def __init__(self):
        self.mailboxes = defaultdict(PriorityQueue)
        self.logger = MessageLogger()

    def send(self, sender_id, receiver_id, message, msg_type="INFO", priority=0, tick=0):
        self.mailboxes[receiver_id].put((
            -priority,  # PriorityQueue is min-heap, so higher priority = lower number
            {
                "sender": sender_id,
                "type": msg_type,
                "content": message
            }
        ))
        self.logger.log(sender_id, receiver_id, msg_type, message, tick)
        print(f"[IPC] {sender_id} ➡ {receiver_id} [{msg_type}]: '{message}'")

    def broadcast(self, sender_id, receivers, message, msg_type="INFO", priority=0, tick=0):
        for receiver_id in receivers:
            self.send(sender_id, receiver_id, message, msg_type, priority, tick)

    def receive(self, agent_id):
        if not self.mailboxes[agent_id].empty():
            _, msg = self.mailboxes[agent_id].get()
            print(f"[IPC] {agent_id} received [{msg['type']}] from {msg['sender']}: '{msg['content']}'")
            return msg
        print(f"[IPC] {agent_id} mailbox empty.")
        return None

    def print_log(self):
        self.logger.print_log()
