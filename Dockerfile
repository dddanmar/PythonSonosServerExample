# asdf
FROM grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild
ONBUILD RUN mod_wsgi-docker-build
#FROM mod_wsgi-docker
RUN apt-get update && \
    apt-get install -y libxml2-dev libxslt1-dev 
RUN apt-get install -y python-lxml
RUN pip install lxml
#This will fail below if virutalenv isn't installed (local dev)
#Can be ignored as ElasticBeanstsalk requires this
RUN mkdir -p /.whiskey/virtualenv/lib/python2.7/site-packages/
RUN ln -s /usr/local/python/lib/python2.7/site-packages/lxml/ /.whiskey/virtualenv/lib/python2.7/site-packages/lxml

CMD [ "sonos_soap.wsgi" ]

EXPOSE 80
