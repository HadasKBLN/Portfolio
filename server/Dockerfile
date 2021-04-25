# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk add --update
# RUN pip install --no-cache-dir pipenv


COPY ./requirements.txt /app/requirements.txt


# # Defining working directory and adding source code
WORKDIR /app
# RUN pip install --upgrade certificate
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /app/requirements.txt

COPY . /app
# COPY server.py ./

# # Install API dependencies
# # RUN pipenv install

# # Start app
# EXPOSE 5000
# ENTRYPOINT ["/usr/src/app/server.py"]

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]