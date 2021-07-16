FROM python:3.6

ARG project_dir=/src/

WORKDIR $project_dir

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi","--ini","/src/uwsgi.ini"]