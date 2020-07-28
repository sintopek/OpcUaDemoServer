import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "TreeNode1")
    myvar = myobj.add_variable(idx, "Variable1", 6.7)
    myvar2 = myobj.add_variable(idx, "Variable2", 7.8)
    myobj2 = objects.add_object(idx, "TreeNode2")
    myvar3 = myobj2.add_variable(idx, "Variable3", 9.0)

    myvar.set_writable()    # Set MyVariable to be writable by clients
    myvar2.set_writable()
    myvar3.set_writable()

    # starting!
    server.start()

    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            # myvar.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
