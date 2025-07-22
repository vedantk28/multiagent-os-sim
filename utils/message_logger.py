class MessageLogger:
    def __init__(self):
        self.history=[]
    def log(self, sender, receiver, msg_type, content, ticks):
        self.history.append({
            "tick": ticks,
            "from": sender,
            "to": receiver,
            "type": msg_type,
            "content": content
        })    

    def print_log(self):
        print("\n Message log:")
        for entry in self.history:
            print(f"[T{entry['tick']}] {entry['from']} -> {entry['to']}  [{entry['type']}]: {entry['content']}")    