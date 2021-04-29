# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk add --update

COPY ./requirements.txt /app/requirements.txt

# # Defining working directory and adding source code
WORKDIR /app
# RUN pip install --upgrade certificate
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r /app/requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "server/app_factory.py" ]