from django.db import models

# Create your models here.

class TaichiStyle(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    code = models.CharField(default="x",max_length=6,verbose_name="編碼")
    title = models.CharField(max_length=200,verbose_name="線路名稱")
    description = models.CharField(max_length=200,verbose_name="說明")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "線路"
        verbose_name_plural = "線路"
        
    # Set is a keyword
class TaichiSet(models.Model):
    taichistyle = models.ForeignKey(TaichiStyle, on_delete=models.CASCADE)
    num = models.IntegerField(default=0,verbose_name="第幾式")
    title = models.CharField(max_length=200,verbose_name="名稱")
    description = models.CharField(max_length=200,verbose_name="說明")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "招式"
        verbose_name_plural = "招式"
    
class TaichiMove(models.Model):
    taichiset = models.ForeignKey(TaichiSet, on_delete=models.CASCADE)
    num = models.IntegerField(default=0,verbose_name="第幾動")
    title = models.CharField(max_length=200,verbose_name="口訣")
    description = models.CharField(max_length=200,verbose_name="要求")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "動作"
        verbose_name_plural = "動作"