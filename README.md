# ETL service for transform asterisk subscribers to xml address book (for Yealink phones)

The service works continuously after launch, the LOOP_TIMEUT parameter is responsible for the update time, the phone
book is available at http://host/yeabook/book.xml

## Before launch:
 ```shell
git clone https://github.com/paQQuete/yealinkRemoteBook.git
``` 
 - install Docker https://docs.docker.com/engine/install/
 - create and fill '.env' file
```shell
cd ~/yealinkRemoteBook/yeabook 
vim .env
```
## .env
 - ASTERISK_HOST=asterisk host ip address (for example, ASTERISK_HOST=10.0.0.1)
 - ASTERISK_SSH_PORT=SSH port (default 22)
 - ASTERISK_USERNAME=username to SSH auth
 - ASTERISK_PASSWORD=password
 - LOOP_TIMEOUT=timeout in seconds for restart ETL process

## First run
```shell
sudo docker-compose up --build
```

## Running
```shell
sudo docker-compose up
```
