import psutil

def get_open_ports():

    ports = []

    connections = psutil.net_connections(kind='inet')

    for conn in connections:

        if conn.status == "LISTEN":

            port = conn.laddr.port

            ports.append(port)

    return sorted(set(ports))