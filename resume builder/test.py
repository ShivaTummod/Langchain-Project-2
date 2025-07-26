from generator import generate_custom_resume

resume = "I'm a Python developer with Django experience."
jd = "Looking for a backend developer skilled in Python, Django, REST API, and SQL."

output = generate_custom_resume(resume, jd)
print(output)
