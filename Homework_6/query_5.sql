SELECT d.name, t.fullname
FROM disciplines d
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2
ORDER BY d.name;
 



