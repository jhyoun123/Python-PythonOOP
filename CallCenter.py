class Call(object):
    def __init__(self, id, name, phone, time, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self):
        print "id: " + str(self.id)
        print "name: " + str(self.name)
        print "phone: " + str(self.phone)
        print "time: " + str(self.time)
        print "reason: " + str(self.reason)

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queueSize = len(calls)
    def add(self, call):
        self.calls.append(call)
    def remove(self)
        self.calls.remove(0)
    def info(self):
        for call in calls:
            print call.name
            print call.phone
        print queueSize