
all:
	gcc rsa.c -o rsa_test
	gcc get_rr.c -o get_rr
	./get_rr
	./rsa_test