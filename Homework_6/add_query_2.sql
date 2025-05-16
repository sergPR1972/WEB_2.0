SELECT s.fullname AS student, g2.name AS name_group, d.name AS discipline, g.grade, g.date_of AS date_last
FROM grades g
JOIN students s ON s.id = g.student_id  
JOIN disciplines d ON d.id = g.discipline_id
JOIN groups g2 ON g2.id = s.group_id 
WHERE g2.id= 1 AND d.id = 7 AND g.date_of IN (SELECT MAX(date_of) FROM grades WHERE discipline_id = d.id )
GROUP BY student;