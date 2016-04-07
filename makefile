FILES :=                              \
    .travis.yml                       \
    cs378-idb.html                      \
    cs378-idb.log

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

sub: 
	 cd python-web-app/app && $(MAKE) test 

IDB1.log:
	git log > IDB1.log
