import redis


class InteractiveDatastore(object):
    def __init__(self):
        # type: () -> None
        self.r = redis.Redis()
        self.ds = None
        self.select_datastore()

    def clear_all(self):
        # type: () -> None
        self.r.flushall()

    def clear_current(self):
        # type: () -> None
        for i in range(self.r.llen(self.ds)):
            self.r.lpop(self.ds)

    def select_datastore(self):
        # type: () -> None
        keys = self.r.keys()
        print "Data stores available"
        for n, k in enumerate(keys):
            print "\t{}. {}".format(n + 1, k)
        self.ds = raw_input("Enter datastore desired: ")
        if self.ds not in keys:
            print "new datastore {} added.".format(self.ds)
        act = raw_input("Add or View: ")
        if act[0].lower() == "a":
            self.add_data()
        elif act[0].lower() == "v":
            self.view_datastore()

    def view_datastore(self):
        # type: () -> None
        if self.ds is None:
            return
        print "Datastore:", self.ds
        for i in range(self.r.llen(self.ds)):
            print "\t-[" + self.r.lindex(self.ds, i)

    def add_data(self):
        # type: () -> None
        again = 'y'
        while again == 'y':
            self.r.rpush(self.ds, raw_input("Enter some text:"))
            again = raw_input("Add again?:")[0].lower()


ids = InteractiveDatastore()
end = False
while not end:
    ids.select_datastore()
    # d = raw_input("Select option")

