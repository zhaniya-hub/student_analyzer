# Student Analyzer

Student Analyzer — студенттердің бағаларын талдауға арналған Python библиотекасы.

## Мүмкіндіктері

- Орташа бағаны есептеу
- Студенттің статусын анықтау
- Студент туралы толық ақпарат шығару

## Орнату

Бұл жобаны GitHub арқылы жүктеп алуға болады.

## Қолдану

```python
from student_analyzer import calculate_average, get_status

grades = [85, 90, 78, 92]

average = calculate_average(grades)

print(average)
print(get_status(average))