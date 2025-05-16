SELECT d.name AS discipline, s.fullname AS student
FROM students s  
JOIN grades g ON g.student_id = s.id    
JOIN disciplines d ON d.id = g.discipline_id
WHERE s.id = 18
GROUP BY discipline 
ORDER BY discipline;  
