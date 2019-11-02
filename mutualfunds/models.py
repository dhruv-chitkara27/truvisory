from django.db import models
# Create your models here.
class users(models.Model):
    name = models.TextField()
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=254)
    contact = models.BigIntegerField()
    marital = models.TextField()
    retire = models.PositiveSmallIntegerField()

class income(models.Model):
    email = models.ForeignKey(users, on_delete=models.CASCADE)
    sal_and_bonus = models.IntegerField()
    sal_ends = models.PositiveSmallIntegerField()
    exp_sal_growth_in_per = models.PositiveSmallIntegerField()
    rent = models.IntegerField()
    rent_ends = models.PositiveSmallIntegerField()
    exp_growth = models.PositiveSmallIntegerField()
    business=models.IntegerField()
    business_ends=models.PositiveSmallIntegerField()
    business_growth=models.PositiveSmallIntegerField()
    other = models.IntegerField()
    other_ends=models.PositiveSmallIntegerField()
    other_growth = models.PositiveSmallIntegerField()

class expenses(models.Model):
    email = models.ForeignKey(users, on_delete=models.CASCADE)
    regular = models.IntegerField()
    regular_ends = models.PositiveSmallIntegerField()
    exp_inf_reg = models.PositiveSmallIntegerField()
    uti = models.IntegerField()
    uti_ends = models.PositiveSmallIntegerField()
    exp_inf_uti = models.PositiveSmallIntegerField()
    grocery=models.IntegerField()
    grocery_ends=models.PositiveSmallIntegerField()
    exp_inf_groc=models.PositiveSmallIntegerField()
    mon_leisure = models.IntegerField()
    leisure_ends=models.PositiveSmallIntegerField()
    exp_les_inf = models.PositiveSmallIntegerField()
    me = models.IntegerField()
    me_ends=models.PositiveSmallIntegerField()
    me_inf = models.PositiveSmallIntegerField()
    ds = models.IntegerField()
    ds_ends=models.PositiveSmallIntegerField()
    exp_les_inf = models.PositiveSmallIntegerField()
