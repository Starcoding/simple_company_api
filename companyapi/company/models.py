from django.db import models
from django.core.validators import RegexValidator

letters_only = RegexValidator(r"^[a-zA-ZА-Яа-я ]*$", ("Разрешены только буквы!"))


class Employee(models.Model):
    first_name = models.CharField(
        verbose_name="Имя сотрудника",
        max_length=255,
        validators=[letters_only],
    )
    second_name = models.CharField(
        verbose_name="Фамилия сотрудника",
        db_index=True,
        max_length=255,
        validators=[letters_only],
    )
    surname = models.CharField(
        verbose_name="Отчество сотрудника",
        max_length=255,
        validators=[letters_only],
    )
    photo = models.ImageField(verbose_name="Фотография сотрудника", blank=True)
    job_title = models.CharField(verbose_name="Должность сотрудника", max_length=80)
    salary = models.DecimalField(
        verbose_name="Зарплата сотрудника", decimal_places=2, max_digits=10
    )
    age = models.IntegerField(verbose_name="Возраст сотрудника")
    department = models.ForeignKey(
        "Department",
        verbose_name="Департамент сотрудника",
        on_delete=models.SET_NULL,
        null=True,
        related_name="department",
    )

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.surname} | {self.job_title} | {self.department}"

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"
        unique_together = (("id", "department"),)


class Department(models.Model):
    name = models.CharField(verbose_name="Название депарамента", max_length=80)
    head_of_department = models.ForeignKey(
        Employee,
        verbose_name="Начальник департамента",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="head_of_department",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "департамент"
        verbose_name_plural = "департаменты"
