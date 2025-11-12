-- Lekérdezés a statisztikailag abnormális olvasztások azonosítására 
SELECT 
    R.ration_id,
    R.start_date_time,
    MAX(CAST(C.temp_6 AS REAL)) AS Panel6_MAX_HO 
FROM 
    rations R
JOIN 
    cool_system C ON R.ration_id = C.ration_id
GROUP BY 
    R.ration_id
HAVING 
    -- ALLEKÉRDEZÉS: Csak azokat az olvasztásokat mutatja, ahol a Panel 6 max hője meghaladja 
    -- az összes olvasztás során mért maximális hőmérsékletek átlagát.
    MAX(CAST(C.temp_6 AS REAL)) > (
        SELECT 
            AVG(MaxHomerseklet)
        FROM 
            -- Belső tábla, ami az összes Olvasztás maximális hőmérsékletét számolja
            (SELECT MAX(CAST(temp_6 AS REAL)) AS MaxHomerseklet FROM cool_system GROUP BY ration_id) AS OsszesOlvasztasMax
    )
ORDER BY 
    Panel6_MAX_HO DESC; 