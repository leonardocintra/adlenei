from django.test import TestCase

from comprovante.models import Arma

class ArmaModelTest(TestCase):
    def setUp(self):
        self.arma = Arma.objects.create(
            descricao = 'TS9',
            marca = 'Taurus',
            calibre = '9mm',
        )
    
    def test_create(self):
        self.assertTrue(Arma.objects.exists())

    def test_calibre_is_not_blank(self):
        field = Arma._meta.get_field('calibre')
        self.assertFalse(field.blank)

    def test_marca_is_not_blank(self):
        field = Arma._meta.get_field('marca')
        self.assertFalse(field.blank)

    def test_descricao_is_not_blank(self):
        field = Arma._meta.get_field('descricao')
        self.assertFalse(field.blank)
    
    def test_str(self):
        self.assertEqual('TS9', str(self.arma))

    