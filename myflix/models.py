from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class Stream(models.Model):
    CATEGORIA = (
        ('F', 'Filme'),
        ('S', 'Série'),
        ('D', 'Documentário'),
    )
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=False)
    categoria = models.CharField(max_length=1, choices=CATEGORIA, default='F')

    def __str__(self):
        return self.codigo

# Ajustando a classe Lista
class Lista(models.Model):
    # O nome da classe referenciada deve ser idêntico (User e Stream)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        # Como Lista não tem 'codigo', o ideal é mostrar a relação
        return f"{self.user.nome} - {self.stream.descricao}"
