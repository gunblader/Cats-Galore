FILES :=                              \
    .travis.yml                       \
    cs378-idb.html                      \
    cs378-idb.log                       \
    models.py                        \
    tests.py

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
	rm -f  RunNetflix.tmp
	rm -f  TestNetflix.tmp
	rm -rf __pycache__

config:
	git config -l

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: RunNetflix.tmp TestNetflix.tmp

Netflix-tests:
	git clone https://github.com/cs373-spring-2016/Netflix-tests.git

Netflix.html: Netflix.py
	pydoc3 -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.tmp: RunNetflix.in RunNetflix.out RunNetflix.py
	./RunNetflix.py < RunNetflix.in > RunNetflix.tmp
	diff RunNetflix.tmp RunNetflix.out

TestNetflix.tmp: TestNetflix.py
	coverage3 run    --branch TestNetflix.py >  TestNetflix.tmp 2>&1
	coverage3 report -m                      >> TestNetflix.tmp
	cat TestNetflix.tmp
