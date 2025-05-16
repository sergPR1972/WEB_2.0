SELECT d.name AS discipline, s.fullname AS student, t.fullname AS teacher
FROM disciplines d  
JOIN teachers t ON t.id = d.teacher_id
JOIN grades g ON g.discipline_id = d.id 
JOIN students s  ON s.id = g.student_id     
WHERE s.id = 10 AND t.id = 2
GROUP BY discipline 
ORDER BY discipline;  
