from paramiko.client import SSHClient
from scp import SCPClient

class Device:
    def __init__(self, hostname,username):
        self.hostname = hostname
        self.username = username

    def get_ip(self):
        #Todo transform hostname to ip
        return self.hostname

    def transfer(self,local_source_folder,remote_target_folder):
        try:
            with SSHClient() as ssh:
                ssh.load_system_host_keys()
                print("connect ",self.hostname,self.username)
                ssh.connect(self.hostname,username=self.username,allow_agent=False)

                scp = SCPClient(ssh.get_transport())
                print("transfer",local_source_folder,remote_target_folder)
                scp.put(local_source_folder, recursive=True, remote_path=remote_target_folder)

                scp.close()

                #stdin, stdout, stderr = ssh.exec_command("docker container ls -a --format '{{json .}}'")
                #for line in stderr.readlines():
                #    print("Error",line)
                #for line in stdout.readlines():
                #    print(line)
        except Exception as e:
            print(e) 
    def build_docker(self,image_name,remote_folder):
        try:
            with SSHClient() as ssh:
                ssh.load_system_host_keys()
                print("connect ",self.hostname,self.username)
                ssh.connect(self.hostname,username=self.username,allow_agent=False)



                stdin, stdout, stderr = ssh.exec_command("docker build -t {} {}".format(image_name,remote_folder))
                for line in stderr.readlines():
                    print("Error",line)
                for line in stdout.readlines():
                    print(line)
        except Exception as e:
            print(e) 

    def run_docker(self,image_name,container_name):
        try:
            with SSHClient() as ssh:
                ssh.load_system_host_keys()
                print("connect ",self.hostname,self.username)
                ssh.connect(self.hostname,username=self.username,allow_agent=False)

                stdin, stdout, stderr = ssh.exec_command("docker run -d --rm --name {} {}".format(container_name,image_name))
                for line in stderr.readlines():
                    print("Error",line)
                for line in stdout.readlines():
                    print(line)
        except Exception as e:
            print(e) 

