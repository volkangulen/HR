SELECT [Doctor],[Professor],[Singer],[Actor]
FROM 
(SELECT ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) as RN,
Name, Occupation FROM Occupations O)P  
PIVOT
(
MAX(P.Name)
 FOR Occupation IN ([Doctor],[Professor],[Singer],[Actor])
) AS PVT
 ORDER BY PVT.RN