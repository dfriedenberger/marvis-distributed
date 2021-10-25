import json
from paramiko.client import SSHClient

with SSHClient() as ssh:
        ssh.load_system_host_keys()
        ssh.connect("192.168.2.206",username="pirate",allow_agent=False)



        stdin, stdout, stderr = ssh.exec_command("docker container ls -a --format '{{json .}}'")
        for line in stderr.readlines():
            print("Error",line)
        for line in stdout.readlines():
            print(line)