from django.contrib.auth.models import User;
from django.db import models

# Create your models here.
class FineTunedModel(models.Model):
    MODEL_CHOICES = [
        ('ada', 'Ada'),
        ('babbage', 'Babbage'),
        ('curie', 'Curie'),
        ('davinci', 'Davinci'),
    ]

    model_name = models.CharField(max_length=100)
    base_model = models.CharField(max_length=100, choices=MODEL_CHOICES)

    # OpenAI의 Fine-tuning할 ChatGPT 모델 정보를 추가합니다?
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fine_tuned_models', null=True)
    file_id = models.CharField(max_length=200, null=True, blank=True)
    fine_tune_id = models.CharField(max_length=200, null=True, blank=True)
    fine_tuned_model = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.model_name


class TrainingData(models.Model):
    fine_tuned_model = models.ForeignKey(FineTunedModel, on_delete=models.CASCADE, related_name='training_data')
    prompt = models.TextField()
    completion = models.TextField()

    # fine-tuning 여부를 체크하기 위한 요소 추가
    is_fine_tuned = models.BooleanField(default=False)
    will_be_fine_tuned = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_datas', null=True)
    
    def __str__(self):
        return f"{self.fine_tuned_model.model_name}의 훈련 데이터"
    
# FineTunedModel은 세부 모델을 나타내고, TrainingData는 특정 세부 모델과 연결된 훈련 데이터를 나타냅니다. 

#TrainingData 모델의 fine_tuned_model 필드는 FineTunedModel 모델과의 일대다 관계를 설정하는 외래 키입니다.