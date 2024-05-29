#!/bin/bash

docker build -t bravo-image .

docker run -it --network=host bravo-image
