ARG PROJECT_TAG=

FROM ghcr.io/diselab/marvis:base${PROJECT_TAG:+-$PROJECT_TAG}

RUN pip install scp


WORKDIR /root/marvis
ENV PATH=${PATH}:/root/marvis/tools \
    PYLXD_WARNINGS=
RUN ln -s /root/marvis/marvis /usr/local/lib/python3.7/site-packages/marvis

