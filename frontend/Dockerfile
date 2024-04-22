FROM busybox:1.35

RUN adduser -D stud
USER stud
WORKDIR /home/stud

COPY src/ .

EXPOSE 3000

ENTRYPOINT ["busybox"]
CMD ["httpd", "-f", "-v", "-p", "3000"]
