FROM alpine:latest

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

RUN apk add --no-cache curl
RUN apk add --no-cache socat

COPY ./curl.sh /curl.sh

CMD ["/curl.sh"]
