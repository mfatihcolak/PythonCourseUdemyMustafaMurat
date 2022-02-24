#"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.

class Kareler():
    def __init__(self,max =  0):
        self.max = max
        self.kuvvet=1

    def __iter__(self):
        return self
    def __next__(self):
        if (self.kuvvet <= self.max):
            sonuc = self.kuvvet ** 2
            self.kuvvet +=1
            return sonuc
        else:
            raise StopIteration
kare = Kareler(10)
iteration = iter(kare)
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))

