SELECT s.fullname, g2.name, d.name, g.grade
FROM students s 
JOIN groups g2 ON g2.id = s.group_id
JOIN grades g ON g.student_id = s.id  
JOIN disciplines d ON d.id = g.discipline_id
WHERE g2.id = 2 AND d.id = 8
ORDER BY g.grade DESC, s.fullname;