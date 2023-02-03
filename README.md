# rsa
精简的rsa实现，大部分代码来自mbedtls。相比于一般的rsa库，该库需要提前计算一个RR值（只和N有关），
计算RR的方法在get_rr.c. 和原生的mbedts库相比，公钥的加解密速度与之相当，私钥的加解密则要慢
数倍。优点是代码比较简短，可以集成到各种存储受限的嵌入式平台，速度也尚可。计算模余幂乘的主要算法
为蒙哥利马算法，和原始的蒙哥利马算法相比，通过迭代算法进行了加速。