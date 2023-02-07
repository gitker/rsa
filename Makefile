
all:
	gcc rsa.c -o rsa_test
	./get_rr.py
	./rsa_test
