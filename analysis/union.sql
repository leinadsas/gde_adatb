-- 1. Alap statisztikák minden ration_id-hoz
SELECT 
    cs.ration_id AS id,
    'Alap_stat' AS tipus,
    'Atlag_homerseklet' AS mert_ertek,
    AVG(cs.temp_6) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

UNION ALL

SELECT 
    cs.ration_id AS id,
    'Alap_stat' AS tipus,
    'Maximalis_homerseklet' AS mert_ertek,
    MAX(cs.temp_6) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

UNION ALL

SELECT 
    cs.ration_id AS id,
    'Alap_stat' AS tipus,
    'Meresekszam' AS mert_ertek,
    COUNT(cs.temp_6) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

UNION ALL

-- 2. Kockázati mutatók - 95-120°C közötti értékek
SELECT 
    cs.ration_id AS id,
    'Kockazat_95_120' AS tipus,
    'Meresekszam_95_120' AS mert_ertek,
    COUNT(CASE WHEN cs.temp_6 BETWEEN 95 AND 120 THEN 1 END) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

UNION ALL

SELECT 
    cs.ration_id AS id,
    'Kockazat_95_120' AS tipus,
    'Arany_95_120_szazalek' AS mert_ertek,
    ROUND((COUNT(CASE WHEN cs.temp_6 BETWEEN 95 AND 120 THEN 1 END) * 100.0 / COUNT(cs.temp_6)), 2) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

UNION ALL

-- 3. Kritikus mutatók - 120°C feletti értékek
SELECT 
    cs.ration_id AS id,
    'Kritikus_120_felett' AS tipus,
    'Meresekszam_120_felett' AS mert_ertek,
    COUNT(CASE WHEN cs.temp_6 > 120 THEN 1 END) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

UNION ALL

SELECT 
    cs.ration_id AS id,
    'Kritikus_120_felett' AS tipus,
    'Arany_120_felett_szazalek' AS mert_ertek,
    ROUND((COUNT(CASE WHEN cs.temp_6 > 120 THEN 1 END) * 100.0 / COUNT(cs.temp_6)), 2) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

UNION ALL

-- 4. Összes kockázati mérés (95°C felett)
SELECT 
    cs.ration_id AS id,
    'Osszes_kockazat_95_felett' AS tipus,
    'Arany_95_felett_osszes_szazalek' AS mert_ertek,
    ROUND((COUNT(CASE WHEN cs.temp_6 > 95 THEN 1 END) * 100.0 / COUNT(cs.temp_6)), 2) AS ertek
FROM cool_system cs
LEFT JOIN rations r ON cs.ration_id = r.ration_id
GROUP BY cs.ration_id

ORDER BY 1, 2, 3;