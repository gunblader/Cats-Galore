FILES :=                              \
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
	rm -f  tests.tmp

status:
	make clean

test: clean tests.tmp

models.html: models.py
	pydoc3 -w models

run.tmp: models.py

tests.tmp: tests.py
	coverage run    --branch tests.py >  tests.tmp 2>&1
	coverage report -m                      >> tests.tmp
	cat tests.tmp
