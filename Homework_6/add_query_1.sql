SELECT t.fullname AS teacher, s.fullname AS student, ROUND(AVG(g.grade), 2) AS average_grade 
FROM teachers t   
JOIN disciplines d ON d.teacher_id = t.id 
JOIN grades g ON g.discipline_id = d.id 
JOIN students s  ON s.id = g.student_id     
WHERE s.id = 49 AND t.id = 2
GROUP BY teacher;  

