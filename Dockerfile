FROM lockermanwxlf/mega-python-bindings

ENV PYTHONUNBUFFERED=1

EXPOSE 80

WORKDIR /app/

COPY ./requirements.txt ./app/* ./

RUN pip3 install -r requirements.txt

RUN mkdir cache

CMD [ "python3", "-u", "main.py"]