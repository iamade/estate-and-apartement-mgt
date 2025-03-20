**Issue**



make db-volume

connect to postgres instance
make estate-db
\list
\connect

list db relation 
\dt

**virtual env**
pipenv shell

**check files that are tracked with git**
git ls-files --others --exclude-standard

**SOS**
jane.doe@gmail.com
KaskAtg2

**localhist**
8080

**if you delete your volumes**
need to run 
```
docker network create estate_prod_nw 
```
**then run**
```
docker compose -f local.yml config
```

**running pipenv in the wrong place**
```
deactivate
pipenv --rm
```




