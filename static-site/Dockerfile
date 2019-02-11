FROM nginx

COPY wrapper.sh /

COPY templates /usr/share/nginx/html

CMD ["./wrapper.sh"]

# Instructions copied from - https://hub.docker.com/_/python/
FROM python:3-onbuild

# run the command
CMD ["python", "./app.py"]



