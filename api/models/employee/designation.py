from django.db import models
from api.models.agedout_model import AgedoutModel
from api.models.main_model import MainModel
from api.models.model_base import ModelBase


class Designation(MainModel, ModelBase, AgedoutModel):
    name = models.CharField(max_length=100, unique=True)