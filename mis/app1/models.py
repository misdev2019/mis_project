from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#课室表
class classroom_equipment_status(models.Model):
	classroom_id = models.CharField(max_length=20,primary_key=True,null=False) #教室编号
	classroom_size = models.IntegerField(null=False) 			    #课室规模
	equipment_type = models.IntegerField(null=False)				#设备类型

	class Meta:
		db_table = "classroom_equipment_status"

class userinfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE) 		#用户
	user_type = models.IntegerField(null=False)						#身份信息

	class Meta:
		db_table = "userinfo"

class classroom_apply(models.Model):
	classroom_apply_id = models.CharField(max_length=10,primary_key=True,null=False)	#申请单编号
	applicant_id = models.CharField(max_length=10,null=False)		#申请人编号
	classroom_id = models.CharField(max_length=20,null=True)		#教室编号
	apply_date = models.DatetimeField(null=False)					#教室需要的日期时间
	apply_reason = models.TextFeild(null=False)						#申请事由
	apply_type = models.IntegerField(null=False)					#申请类别
	edu_admin_id = models.CharField(max_length=10,null=True)		#第一审批人编号
	head_id = models.CharField(max_length=10,null=True)				#第二审批人编号
	apply_status = models.IntegerField(null=False,default=3)		#审批状态
	apply_time = models.DatetimeField(auto_now_add=True)			#申请时间

	class Meta:
		db_table = "classroom_apply"
		ordering = ['apply_time']

class classroom_use_record(models.Model):
	classroom_id = models.CharField(max_length=20,null=False)		#教室编号
	use_time = models.DatetimeField(null=False)						#使用时间

	class Meta:
		db_table = "classroom_use_record"
		