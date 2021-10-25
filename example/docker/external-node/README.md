# external node

Docker container which is reachable via ssh and provides unbuntu with shell and docker cli.

## Installation
```
docker build -t external-node .
``` 
## Usage 
```
docker run --rm --name external-node-1 -v //var/run/docker.sock:/var/run/docker.sock --cap-add=ALL -d -p 22:22 external-node
```

### FAQ

Q: I get the error "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!".
A: Run "ssh-keygen -R localhost"

Q: I do not have a '.ssh/id_rsa.pub' file
A: ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ""

Q: I would like to log in without a password.
A: 'ssh-copy-id -i ~/.ssh/id_rsa.pub test@localhost' 


