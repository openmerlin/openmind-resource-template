```python
# Use pipeline
from openmind import pipeline
pipe = pipeline("[task]", model="[repo]", trust_remote_code=True, framework="[framework]")
pipe("人工智能是什么")
```