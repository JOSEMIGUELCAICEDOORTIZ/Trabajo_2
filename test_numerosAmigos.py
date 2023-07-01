import pytest
from numerosAmigos import numeros_amigos
# Para que los números sean amigos el divisor del número uno tiene que ser el número 2 y viceversa

# Para probar la función de los números amigos se hicieron 10 tests, 5 destinados para funcionar y 5 destinados a fallar

# Pruebas destinadas a funcionar
# En esta prueba son amigos 
def test_1():
    assert numeros_amigos(17296,18416) == "17296 y 18416 son amigos"
# En esta prueba son amigos     
def test_2():
    assert numeros_amigos(9363584,9437056) == "9363584 y 9437056 son amigos"
# En esta prueba no son amigos     
def test_3():
    assert numeros_amigos(12,35) == "12 y 35 no son amigos"
# En esta prueba no son amigos     
def test_4():
    assert numeros_amigos(31,255) == "31 y 255 no son amigos"
# En esta prueba no son amigos 
def test_5():
    assert numeros_amigos(27,18) == "27 y 18 no son amigos"
    
# Pruebas destinadas a fallar
# En esta prueba no son amigos
def test_6():
    assert not numeros_amigos(680,195) == "680 y 195 son amigos"
# En esta prueba son amigos
def test_7():
    assert not numeros_amigos(220,284) == "220 y 284 no son amigos"
# En esta prueba no son amigos
def test_8():
    assert not numeros_amigos(40,100) == "40 y 100 son amigos"
# En esta prueba no son amigos
def test_9():
    assert not numeros_amigos(12,20) == "12 y 20 son amigos"
# En esta prueba son amigos   
def test_10():
    assert not numeros_amigos(522405,525915) == "522405 y 525915 no son amigos"

if __name__ == '__main__':
    #Se ejecutan las pruebas
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    test_10()