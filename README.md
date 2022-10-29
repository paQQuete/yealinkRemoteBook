# ETL service for transform asterisk subscribers to xml address book (for Yealink phones)

The service works continuously after launch, the LOOP_TIMEOUT parameter is responsible for the update time, the phone
book is available at http://host/yeabook/book.xml

## Before launch:
 ```shell
git clone https://github.com/paQQuete/yealinkRemoteBook.git
``` 
 - install Docker https://docs.docker.com/engine/install/
 - install Docker Compose https://docs.docker.com/compose/install/
 - create and fill '.env' file
```shell
cd ~/yealinkRemoteBook/yeabook 
vim .env
```
## .env
 ```shell
 ASTERISK_HOST=asterisk host ip address (for example, ASTERISK_HOST=10.0.0.1)
 ASTERISK_SSH_PORT=SSH port (default 22)
 ASTERISK_USERNAME=username to SSH auth
 ASTERISK_PASSWORD=password
 LOOP_TIMEOUT=timeout in seconds for restart ETL process
 ```

## First run
```shell
cd ~/yealinkRemoteBook && sudo docker-compose up --build
```
or
```shell
cd ~/yealinkRemoteBook && sudo docker-compose up -d --build
```
run in detach mode (to avoid attaching a process to a running terminal)

## Running
```shell
cd ~/yealinkRemoteBook && sudo docker-compose up
```
or
```shell
cd ~/yealinkRemoteBook && sudo docker-compose up -d
```
run in detach mode (to avoid attaching a process to a running terminal)
