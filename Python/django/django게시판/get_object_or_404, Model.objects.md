# Model.objects

### Model.objects.all()
queryset 전체를 부른다.
Model.objects.values() 라고도 사용하는 듯

### Model.objects.get()
조건에 해당하는 결과 값 하나만! 불러온다. 

### Model.objects.filter()
조건에 해당하는 결과 불러오고 검색 결과가 2개 이상이 나올 수 있다.

# get_object_or_404
```python
get_object_or_404(Model, pk=pk)
# 이 코드는 아래 코드와 같은 로직이다.
try::
    model = Model.objects.get(pk=pk)
except:
    raise Http404
```
만약 model에서 에러 발생시 Http404에러 발생