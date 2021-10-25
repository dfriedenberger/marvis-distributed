# marvis-distributed

Marvis simulation with distributed nodes (raspberry pi, external nodes, ...).

- Testing distibuted algorithm
- analyse traffic
- inject chaos

see: https://en.wikipedia.org/wiki/Distributed_algorithm

run in aws


## Installation

```
docker build -t marvis-distibuted-host -f .devcontainer/Dockerfile .
```

## Usage

Run docker image
```
docker run --rm -it --name marvis-host --cap-add=ALL -v `pwd`:/root/marvis -v /var/run/docker.sock:/var/run/docker.sock --net host --pid host --userns host --privileged marvis-distibuted-host bash
```

Start simulation 
```
cd example
python3 ping-pong-local.py
```

## Contributing

Send me your favorites. I will taste them. If I find them good they will be added to the collection. Pull requests are welcome.

## Authors and acknowledgment

- Used recipes format from  https://github.com/cnstoll/Grocery-Recipe-Format
- Collage is made with PowerPoint
- For readme file I used format from https://www.makeareadme.com/

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)


