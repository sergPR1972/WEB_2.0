SELECT s.fullname, g.name
FROM students s 
JOIN groups g ON g.id = s.group_id
WHERE g.id = 2
ORDER BY s.fullname;
 



