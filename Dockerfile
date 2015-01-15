FROM texastribune/base
MAINTAINER marcosvanetta@gmail.com

ADD . /app/
WORKDIR /app/
RUN pip install -r requirements.txt

CMD python emission_events/manage.py updateemissions
