# Convert dictionary to Json format
import json
data={"name": "Harry", "age":"20"}
print(type(data))
d=json.dumps(data)
print(d)
print(type(d))


      