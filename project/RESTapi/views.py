from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

import tensorflow as tf
from tf.keras.models import load_model
from tensorflow import keras
from rest_framework.permissions import AllowAny

# Load the pretrained model
model = load_model('models\\h5\\words\\model.h5')
