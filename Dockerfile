FROM python:3-onbuild

EXPOSE 8088
CMD [ "python", "./src/main.py" ]
