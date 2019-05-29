from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#1.时间表
class timetable(models.Model):
	section = models.IntegerField(primary_key=True,null=False)	#对应每天每一节
	start_time = models.TimeField(null=False)					#该节开始时间
	end_time = models.TimeField(null=False)						#该节结束时间

	class Meta:
		db_table = "timetable"
		ordering = ['section']

#2.课室表
class classroom_equipment_status(models.Model):
	classroom_id = models.CharField(max_length=20,primary_key=True,null=False) #教室编号
	classroom_size = models.IntegerField(null=False) 			    #课室规模
	equipment_type = models.IntegerField(null=False)				#设备类型

	class Meta:
		db_table = "classroom_equipment_status"

#3.用户信息表
class userinfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE) 		#用户
	user_type = models.IntegerField(null=False)						#身份信息

	class Meta:
		db_table = "userinfo"

#4.申请单表
class classroom_apply(models.Model):
	classroom_apply_id = models.CharField(max_length=10,primary_key=True,null=False)	#申请单编号
	applicant_id = models.CharField(max_length=10,null=False)		#申请人编号
	classroom_id = models.CharField(max_length=20,null=True)		#教室编号
	apply_date = models.DateField(null=False)						#需求日期
	apply_section = models.IntegerField(null=False)					#需求节数
	apply_reason = models.TextField(null=False)						#申请事由
	apply_type = models.IntegerField(null=False)					#申请类别
	edu_admin_id = models.CharField(max_length=10,null=True)		#第一审批人编号
	head_id = models.CharField(max_length=10,null=True)				#第二审批人编号
	apply_status = models.IntegerField(null=False,default=3)		#审批状态
	apply_time = models.DateTimeField(auto_now_add=True)			#申请时间

	class Meta:
		db_table = "classroom_apply"
		ordering = ['apply_time']

#5.课室使用记录表
class classroom_use_record(models.Model):
	classroom_id = models.CharField(max_length=20,null=False)		#教室编号
	use_date = models.DateField(null=False)							#使用日期
	use_section = models.IntegerField(null=False)					#使用节数

	class Meta:
		db_table = "classroom_use_record"
		unique_together = ("classroom_id","use_date","use_section")

#6.已通过的申请单表 #当表5的审批状态为已完成时，将数据移入该表
class classroom_apply_finished(models.Model):
	classroom_apply_id = models.CharField(max_length=10,primary_key=True,null=False)	#申请单编号
	applicant_id = models.CharField(max_length=10,null=False)		#申请人编号
	classroom_id = models.CharField(max_length=20,null=True)		#教室编号
	apply_date = models.DateField(null=False)						#需求日期
	apply_section = models.IntegerField(null=False)					#需求节数
	apply_reason = models.TextField(null=False)						#申请事由
	apply_type = models.IntegerField(null=False)					#申请类别
	edu_admin_id = models.CharField(max_length=10,null=True)		#第一审批人编号
	head_id = models.CharField(max_length=10,null=True)				#第二审批人编号
	

	class Meta:
		db_table = "classroom_apply_finished"
		ordering = ['apply_date']

#7.学期课程课室占用表
class course_classroom(models.Model):
	classroom_id = models.CharField(max_length=20,null=False)		#教室编号
	use_date = models.DateField(null=False)							#使用日期
	use_section = models.IntegerField(null=False)					#使用节数

	class Meta:
		db_table = "course_classroom"
		unique_together = ("classroom_id","use_date","use_section")

#8.字典变量
class status_code_directory(models.Model):
	status_code = models.IntegerField(max_length=5, null=False)   #状态代码
	status_meaning = models.CharField(max_length=20, null=False)  #状态解释
	status_type = models.CharField(max_length=5, null=False)      #状态所属类别

	class Meta:
		db_table = "status_code_irectory"
		unique_together = ("status_code", "status_type")



