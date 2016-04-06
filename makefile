FILES :=                              \
    .travis.yml                       \
    cs378-idb.html                      \
    cs378-idb.log                       \
    python_web_app/app/models.py                        \
    python_web_app/app/tests.py

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: run.tmp tests.tmp

models.html: models.py
	pydoc3 -w models

IDB1.log:
	git log > IDB1.log

run.tmp: models.py

tests.tmp: tests.py
	coverage3 run    --branch tests.py >  tests.tmp 2>&1
	coverage3 report -m                      >> tests.tmp
	cat tests.tmp
